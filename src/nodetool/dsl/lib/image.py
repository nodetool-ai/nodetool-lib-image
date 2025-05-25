from pydantic import BaseModel, Field
import typing
from typing import Any
import nodetool.metadata.types
import nodetool.metadata.types as types
from nodetool.dsl.graph import GraphNode


class BatchToList(GraphNode):
    """Convert a batch image into a list of images."""

    batch: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Batch of images",
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.BatchToList"


class Crop(GraphNode):
    """Crop an image region."""

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image to crop",
    )
    left: int | GraphNode | tuple[GraphNode, str] = Field(default=0, description="Left")
    top: int | GraphNode | tuple[GraphNode, str] = Field(default=0, description="Top")
    right: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Right"
    )
    bottom: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Bottom"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.Crop"


class Fit(GraphNode):
    """Resize and crop an image to fit the given size."""

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image to fit",
    )
    width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description="Target width"
    )
    height: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description="Target height"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.Fit"


class GetMetadata(GraphNode):
    """Return basic image metadata."""

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image to inspect.",
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.GetMetadata"


class ImageOutput(GraphNode):
    """Workflow output for images."""

    value: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image value",
    )
    name: str | GraphNode | tuple[GraphNode, str] = Field(
        default="", description="The parameter name for the workflow."
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.ImageOutput"


class Paste(GraphNode):
    """Paste one image onto another."""

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Base image",
    )
    paste: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image to paste",
    )
    left: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Left position"
    )
    top: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Top position"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.Paste"


class Resize(GraphNode):
    """Resize an image to specific dimensions."""

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image to resize",
    )
    width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description="Width"
    )
    height: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description="Height"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.Resize"


class SaveImage(GraphNode):
    """Save an image reference."""

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image to save.",
    )
    folder: types.FolderRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.FolderRef(type="folder", uri="", asset_id=None, data=None),
        description="Target folder.",
    )
    name: str | GraphNode | tuple[GraphNode, str] = Field(
        default="image.png", description="File name"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.SaveImage"


class Scale(GraphNode):
    """Scale an image by a factor."""

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="Image to scale",
    )
    scale: float | GraphNode | tuple[GraphNode, str] = Field(
        default=1.0, description="Scale factor"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.image.Scale"
