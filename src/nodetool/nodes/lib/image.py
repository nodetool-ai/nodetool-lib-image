from PIL import Image, ImageOps
from pydantic import Field

from nodetool.metadata.types import ImageRef, FolderRef
from nodetool.workflows.base_node import BaseNode, OutputNode
from nodetool.workflows.processing_context import ProcessingContext


class SaveImage(BaseNode):
    """Save an image reference."""

    image: ImageRef = Field(default=ImageRef(), description="Image to save.")
    folder: FolderRef = Field(default=FolderRef(), description="Target folder.")
    name: str = Field(default="image.png", description="File name")

    async def process(self, context: ProcessingContext) -> ImageRef:
        # In this simplified implementation we just return the original image.
        return self.image

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["image"]


class GetMetadata(BaseNode):
    """Return basic image metadata."""

    image: ImageRef = Field(default=ImageRef(), description="Image to inspect.")

    async def process(self, context: ProcessingContext) -> dict:
        img = await context.image_to_pil(self.image)
        width, height = img.size
        return {"width": width, "height": height}

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["image"]


class BatchToList(BaseNode):
    """Convert a batch image into a list of images."""

    batch: ImageRef = Field(default=ImageRef(), description="Batch of images")

    async def process(self, context: ProcessingContext) -> list[ImageRef]:
        if isinstance(self.batch.data, list):
            results: list[ImageRef] = []
            for data in self.batch.data:
                if isinstance(data, bytes):
                    results.append(await context.image_from_bytes(data))
            return results
        return []

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["batch"]


class Paste(BaseNode):
    """Paste one image onto another."""

    image: ImageRef = Field(default=ImageRef(), description="Base image")
    paste: ImageRef = Field(default=ImageRef(), description="Image to paste")
    left: int = Field(default=0, description="Left position")
    top: int = Field(default=0, description="Top position")

    async def process(self, context: ProcessingContext) -> ImageRef:
        base = await context.image_to_pil(self.image)
        overlay = await context.image_to_pil(self.paste)
        base.paste(overlay, (self.left, self.top))
        return await context.image_from_pil(base)

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["image", "paste"]


class Fit(BaseNode):
    """Resize and crop an image to fit the given size."""

    image: ImageRef = Field(default=ImageRef(), description="Image to fit")
    width: int = Field(default=512, ge=1, description="Target width")
    height: int = Field(default=512, ge=1, description="Target height")

    async def process(self, context: ProcessingContext) -> ImageRef:
        img = await context.image_to_pil(self.image)
        img = ImageOps.fit(img, (self.width, self.height))
        return await context.image_from_pil(img)

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["image", "width", "height"]


class Scale(BaseNode):
    """Scale an image by a factor."""

    image: ImageRef = Field(default=ImageRef(), description="Image to scale")
    scale: float = Field(default=1.0, ge=0.0, description="Scale factor")

    async def process(self, context: ProcessingContext) -> ImageRef:
        img = await context.image_to_pil(self.image)
        w, h = img.size
        img = img.resize((int(w * self.scale), int(h * self.scale)))
        return await context.image_from_pil(img)

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["image", "scale"]


class Resize(BaseNode):
    """Resize an image to specific dimensions."""

    image: ImageRef = Field(default=ImageRef(), description="Image to resize")
    width: int = Field(default=512, ge=1, description="Width")
    height: int = Field(default=512, ge=1, description="Height")

    async def process(self, context: ProcessingContext) -> ImageRef:
        img = await context.image_to_pil(self.image)
        img = img.resize((self.width, self.height))
        return await context.image_from_pil(img)

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["image", "width", "height"]


class Crop(BaseNode):
    """Crop an image region."""

    image: ImageRef = Field(default=ImageRef(), description="Image to crop")
    left: int = Field(default=0, ge=0, description="Left")
    top: int = Field(default=0, ge=0, description="Top")
    right: int = Field(default=1, ge=1, description="Right")
    bottom: int = Field(default=1, ge=1, description="Bottom")

    async def process(self, context: ProcessingContext) -> ImageRef:
        img = await context.image_to_pil(self.image)
        img = img.crop((self.left, self.top, self.right, self.bottom))
        return await context.image_from_pil(img)

    @classmethod
    def get_basic_fields(cls) -> list[str]:
        return ["image", "left", "top", "right", "bottom"]


class ImageOutput(OutputNode):
    """Workflow output for images."""

    value: ImageRef = Field(default=ImageRef(), description="Image value")

    async def process(self, context: ProcessingContext) -> ImageRef:
        return self.value
