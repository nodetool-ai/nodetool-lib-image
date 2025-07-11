from enum import Enum
import PIL.Image
import PIL.ImageDraw
import PIL.ImageEnhance
import PIL.ImageFilter
import PIL.ImageFont
import PIL.ImageOps
from nodetool.workflows.processing_context import ProcessingContext
from nodetool.nodes.lib.pillow.enhance import (
    canny_edge_detection,
)
from nodetool.metadata.types import ImageRef
from nodetool.workflows.base_node import BaseNode
from pydantic import Field


class Invert(BaseNode):
    """
    Invert the colors of an image.
    image, filter, invert

    - Create negative versions of images for visual effects
    - Analyze image data by bringing out hidden details
    - Preprocess images for operations that work better on inverted colors
    """

    image: ImageRef = Field(
        default=ImageRef(), description="The image to adjust the brightness for."
    )

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        res = PIL.ImageOps.invert(image)
        return await context.image_from_pil(res)


class Solarize(BaseNode):
    """
    Apply a solarize effect to partially invert image tones.
    image, filter, solarize

    - Create surreal artistic photo effects
    - Enhance visual data by making certain elements more prominent
    - Add a unique style to images for graphic design
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to solarize.")
    threshold: int = Field(
        default=128, ge=0, le=255, description="Threshold for solarization."
    )

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        res = PIL.ImageOps.solarize(image, threshold=self.threshold)
        return await context.image_from_pil(res)


class Posterize(BaseNode):
    """
    Reduce the number of colors in an image for a poster-like effect.
    image, filter, posterize

    - Create graphic art by simplifying image colors
    - Apply artistic effects to photographs
    - Generate visually compelling content for advertising
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to posterize.")
    bits: int = Field(
        default=4, ge=1, le=8, description="Number of bits to posterize to."
    )

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        res = PIL.ImageOps.posterize(image, bits=self.bits)
        return await context.image_from_pil(res)


class Expand(BaseNode):
    """
    Add a border around an image to increase its size.
    image, border, expand

    - Make images stand out by adding a colored border
    - Create framed photo effects
    - Separate image content from surroundings
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to expand.")
    border: int = Field(default=0, ge=0, le=512, description="Border size.")
    fill: int = Field(default=0, ge=0, le=255, description="Fill color.")

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        res = PIL.ImageOps.expand(image, border=self.border, fill=self.fill)
        return await context.image_from_pil(res)


class Blur(BaseNode):
    """
    Apply a Gaussian blur effect to an image.
    image, filter, blur

    - Soften images or reduce noise and detail
    - Make focal areas stand out by blurring surroundings
    - Protect privacy by blurring sensitive information
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to blur.")
    radius: int = Field(default=2, ge=0, le=128, description="Blur radius.")

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        res = image.filter(PIL.ImageFilter.GaussianBlur(self.radius))
        return await context.image_from_pil(res)


class Contour(BaseNode):
    """
    Apply a contour filter to highlight image edges.
    image, filter, contour

    - Extract key features from complex images
    - Aid pattern recognition and object detection
    - Create stylized contour sketch art effects
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to contour.")

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        return await context.image_from_pil(image.filter(PIL.ImageFilter.CONTOUR))


class Emboss(BaseNode):
    """
    Apply an emboss filter for a 3D raised effect.
    image, filter, emboss

    - Add texture and depth to photos
    - Create visually interesting graphics
    - Incorporate unique effects in digital artwork
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to emboss.")

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        return await context.image_from_pil(image.filter(PIL.ImageFilter.EMBOSS))


class FindEdges(BaseNode):
    """
    Detect and highlight edges in an image.
    image, filter, edges

    - Analyze structural patterns in images
    - Aid object detection in computer vision
    - Detect important features like corners and ridges
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to find edges.")

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        return await context.image_from_pil(image.filter(PIL.ImageFilter.FIND_EDGES))


class Smooth(BaseNode):
    """
    Apply smoothing to reduce image noise and detail.
    image, filter, smooth

    - Enhance visual aesthetics of images
    - Improve object detection by reducing irrelevant details
    - Aid facial recognition by simplifying images
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to smooth.")

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        return await context.image_from_pil(image.filter(PIL.ImageFilter.SMOOTH))


class Canny(BaseNode):
    """
    Apply Canny edge detection to an image.
    image, filter, edges

    - Highlight areas of rapid intensity change
    - Outline object boundaries and structure
    - Enhance inputs for object detection and image segmentation
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to canny.")
    low_threshold: int = Field(default=100, ge=0, le=255, description="Low threshold.")
    high_threshold: int = Field(
        default=200, ge=0, le=255, description="High threshold."
    )

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        res = canny_edge_detection(image, self.low_threshold, self.high_threshold)
        return await context.image_from_pil(res)


class ConvertToGrayscale(BaseNode):
    """
    Convert an image to grayscale.
    image, grayscale

    - Simplify images for feature and edge detection
    - Prepare images for shape-based machine learning
    - Create vintage or monochrome aesthetic effects
    """

    image: ImageRef = Field(default=ImageRef(), description="The image to convert.")

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        return await context.image_from_pil(image.convert("L"))


class GetChannel(BaseNode):
    """
    Extract a specific color channel from an image.
    image, color, channel, isolate, extract

    - Isolate color information for image analysis
    - Manipulate specific color components in graphic design
    - Enhance or reduce visibility of certain colors
    """

    class ChannelEnum(str, Enum):
        RED = "R"
        GREEN = "G"
        BLUE = "B"

    image: ImageRef = Field(
        default=ImageRef(), description="The image to get the channel from."
    )
    channel: ChannelEnum = ChannelEnum.RED

    async def process(self, context: ProcessingContext) -> ImageRef:
        image = await context.image_to_pil(self.image)
        res = image.getchannel(self.channel.value)
        return await context.image_from_pil(res)
