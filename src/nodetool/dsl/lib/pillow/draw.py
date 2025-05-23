from pydantic import BaseModel, Field
import typing
from typing import Any
import nodetool.metadata.types
import nodetool.metadata.types as types
from nodetool.dsl.graph import GraphNode


class Background(GraphNode):
    """
    The Background Node creates a blank background.
    image, background, blank, base, layer
    This node is mainly used for generating a base layer for image processing tasks. It produces a uniform image, having a user-specified width, height and color. The color is given in a hexadecimal format, defaulting to white if not specified.

    #### Applications
    - As a base layer for creating composite images.
    - As a starting point for generating patterns or graphics.
    - When blank backgrounds of specific colors are required for visualization tasks.
    """

    width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description=None
    )
    height: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description=None
    )
    color: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#FFFFFF"), description=None
    )

    @classmethod
    def get_node_type(cls):
        return "lib.pillow.draw.Background"


class GaussianNoise(GraphNode):
    """
    This node creates and adds Gaussian noise to an image.
    image, noise, gaussian, distortion, artifact

    The Gaussian Noise Node is designed to simulate realistic distortions that can occur in a photographic image. It generates a noise-filled image using the Gaussian (normal) distribution. The noise level can be adjusted using the mean and standard deviation parameters.

    #### Applications
    - Simulating sensor noise in synthetic data.
    - Testing image-processing algorithms' resilience to noise.
    - Creating artistic effects in images.
    """

    mean: float | GraphNode | tuple[GraphNode, str] = Field(
        default=0.0, description=None
    )
    stddev: float | GraphNode | tuple[GraphNode, str] = Field(
        default=1.0, description=None
    )
    width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description=None
    )
    height: int | GraphNode | tuple[GraphNode, str] = Field(
        default=512, description=None
    )

    @classmethod
    def get_node_type(cls):
        return "lib.pillow.draw.GaussianNoise"


import nodetool.nodes.lib.pillow.draw
import nodetool.nodes.lib.pillow.draw


class RenderText(GraphNode):
    """
    This node allows you to add text to images.
    text, font, label, title, watermark, caption, image, overlay
    This node takes text, font updates, coordinates (where to place the text), and an image to work with. A user can use the Render Text Node to add a label or title to an image, watermark an image, or place a caption directly on an image.

    The Render Text Node offers customizable options, including the ability to choose the text's font, size, color, and alignment (left, center, or right). Text placement can also be defined, providing flexibility to place the text wherever you see fit.

    #### Applications
    - Labeling images in a image gallery or database.
    - Watermarking images for copyright protection.
    - Adding custom captions to photographs.
    - Creating instructional images to guide the reader's view.
    """

    TextFont: typing.ClassVar[type] = nodetool.nodes.lib.pillow.draw.RenderText.TextFont
    TextAlignment: typing.ClassVar[type] = (
        nodetool.nodes.lib.pillow.draw.RenderText.TextAlignment
    )
    text: str | GraphNode | tuple[GraphNode, str] = Field(
        default="", description="The text to render."
    )
    font: nodetool.nodes.lib.pillow.draw.RenderText.TextFont = Field(
        default=nodetool.nodes.lib.pillow.draw.RenderText.TextFont.DejaVuSans,
        description="The font to use.",
    )
    x: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="The x coordinate."
    )
    y: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="The y coordinate."
    )
    size: int | GraphNode | tuple[GraphNode, str] = Field(
        default=12, description="The font size."
    )
    color: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"),
        description="The font color.",
    )
    align: nodetool.nodes.lib.pillow.draw.RenderText.TextAlignment = Field(
        default=nodetool.nodes.lib.pillow.draw.RenderText.TextAlignment.LEFT,
        description=None,
    )
    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="The image to render on.",
    )

    @classmethod
    def get_node_type(cls):
        return "lib.pillow.draw.RenderText"
