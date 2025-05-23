from pydantic import BaseModel, Field
import typing
from typing import Any
import nodetool.metadata.types
import nodetool.metadata.types as types
from nodetool.dsl.graph import GraphNode


class CircleNode(GraphNode):
    """
    Generate SVG circle element.
    svg, shape, vector, circle
    """

    cx: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Center X coordinate"
    )
    cy: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Center Y coordinate"
    )
    radius: int | GraphNode | tuple[GraphNode, str] = Field(
        default=50, description="Radius"
    )
    fill: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"), description="Fill color"
    )
    stroke: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="none"), description="Stroke color"
    )
    stroke_width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Stroke width"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Circle"


class ClipPath(GraphNode):
    """
    Create clipping paths for SVG elements.
    svg, clip, mask

    Use cases:
    - Mask parts of elements
    - Create complex shapes through clipping
    - Apply visual effects using masks
    """

    clip_content: types.SVGElement | GraphNode | tuple[GraphNode, str] = Field(
        default=None, description="SVG element to use as clip path"
    )
    content: types.SVGElement | GraphNode | tuple[GraphNode, str] = Field(
        default=None, description="SVG element to clip"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.ClipPath"


class Document(GraphNode):
    """
    Combine SVG elements into a complete SVG document.
    svg, document, combine

    Use cases:
    - Combine multiple SVG elements into a single document
    - Set document-level properties like viewBox and dimensions
    - Export complete SVG documents
    """

    content: (
        str
        | nodetool.metadata.types.SVGElement
        | list[nodetool.metadata.types.SVGElement]
        | GraphNode
        | tuple[GraphNode, str]
    ) = Field(default=[], description="SVG content")
    width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=800, description="Document width"
    )
    height: int | GraphNode | tuple[GraphNode, str] = Field(
        default=600, description="Document height"
    )
    viewBox: str | GraphNode | tuple[GraphNode, str] = Field(
        default="0 0 800 600", description="SVG viewBox attribute"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Document"


class DropShadow(GraphNode):
    """
    Apply drop shadow filter to SVG elements.
    svg, filter, shadow, effects
    """

    std_deviation: float | GraphNode | tuple[GraphNode, str] = Field(
        default=3.0, description="Standard deviation for blur"
    )
    dx: int | GraphNode | tuple[GraphNode, str] = Field(
        default=2, description="X offset for shadow"
    )
    dy: int | GraphNode | tuple[GraphNode, str] = Field(
        default=2, description="Y offset for shadow"
    )
    color: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"),
        description="Color for shadow",
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.DropShadow"


class EllipseNode(GraphNode):
    """
    Generate SVG ellipse element.
    svg, shape, vector, ellipse
    """

    cx: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Center X coordinate"
    )
    cy: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Center Y coordinate"
    )
    rx: int | GraphNode | tuple[GraphNode, str] = Field(
        default=100, description="X radius"
    )
    ry: int | GraphNode | tuple[GraphNode, str] = Field(
        default=50, description="Y radius"
    )
    fill: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"), description="Fill color"
    )
    stroke: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="none"), description="Stroke color"
    )
    stroke_width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Stroke width"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Ellipse"


class GaussianBlur(GraphNode):
    """
    Apply Gaussian blur filter to SVG elements.
    svg, filter, blur, effects
    """

    std_deviation: float | GraphNode | tuple[GraphNode, str] = Field(
        default=3.0, description="Standard deviation for blur"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.GaussianBlur"


import nodetool.nodes.lib.svg


class Gradient(GraphNode):
    """
    Create linear or radial gradients for SVG elements.
    svg, gradient, color

    Use cases:
    - Add smooth color transitions
    - Create complex color effects
    - Define reusable gradient definitions
    """

    GradientType: typing.ClassVar[type] = nodetool.nodes.lib.svg.Gradient.GradientType
    gradient_type: nodetool.nodes.lib.svg.Gradient.GradientType = Field(
        default=nodetool.nodes.lib.svg.Gradient.GradientType.LINEAR,
        description="Type of gradient",
    )
    x1: float | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Start X position (linear) or center X (radial)"
    )
    y1: float | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Start Y position (linear) or center Y (radial)"
    )
    x2: float | GraphNode | tuple[GraphNode, str] = Field(
        default=100, description="End X position (linear) or radius X (radial)"
    )
    y2: float | GraphNode | tuple[GraphNode, str] = Field(
        default=100, description="End Y position (linear) or radius Y (radial)"
    )
    color1: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"),
        description="Start color of gradient",
    )
    color2: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#FFFFFF"),
        description="End color of gradient",
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Gradient"


class LineNode(GraphNode):
    """
    Generate SVG line element.
    svg, shape, vector, line
    """

    x1: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Start X coordinate"
    )
    y1: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Start Y coordinate"
    )
    x2: int | GraphNode | tuple[GraphNode, str] = Field(
        default=100, description="End X coordinate"
    )
    y2: int | GraphNode | tuple[GraphNode, str] = Field(
        default=100, description="End Y coordinate"
    )
    stroke: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"),
        description="Stroke color",
    )
    stroke_width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Stroke width"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Line"


class PathNode(GraphNode):
    """
    Generate SVG path element.
    svg, shape, vector, path
    """

    path_data: str | GraphNode | tuple[GraphNode, str] = Field(
        default=PydanticUndefined, description="SVG path data (d attribute)"
    )
    fill: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"), description="Fill color"
    )
    stroke: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="none"), description="Stroke color"
    )
    stroke_width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Stroke width"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Path"


class PolygonNode(GraphNode):
    """
    Generate SVG polygon element.
    svg, shape, vector, polygon
    """

    points: str | GraphNode | tuple[GraphNode, str] = Field(
        default=PydanticUndefined, description="Points in format 'x1,y1 x2,y2 x3,y3...'"
    )
    fill: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"), description="Fill color"
    )
    stroke: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="none"), description="Stroke color"
    )
    stroke_width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Stroke width"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Polygon"


class RectNode(GraphNode):
    """
    Generate SVG rectangle element.
    svg, shape, vector, rectangle
    """

    x: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="X coordinate"
    )
    y: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Y coordinate"
    )
    width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=100, description="Width"
    )
    height: int | GraphNode | tuple[GraphNode, str] = Field(
        default=100, description="Height"
    )
    fill: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"), description="Fill color"
    )
    stroke: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="none"), description="Stroke color"
    )
    stroke_width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Stroke width"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Rect"


class SVGToImage(GraphNode):
    """
    Create an SVG document and convert it to a raster image in one step.
    svg, document, raster, convert

    Use cases:
    - Create and rasterize SVG documents in a single operation
    - Generate image files from SVG elements
    - Convert vector graphics to bitmap format with custom dimensions
    """

    content: (
        str
        | nodetool.metadata.types.SVGElement
        | list[nodetool.metadata.types.SVGElement]
        | GraphNode
        | tuple[GraphNode, str]
    ) = Field(default=[], description="SVG content")
    width: int | GraphNode | tuple[GraphNode, str] = Field(
        default=800, description="Document width"
    )
    height: int | GraphNode | tuple[GraphNode, str] = Field(
        default=600, description="Document height"
    )
    viewBox: str | GraphNode | tuple[GraphNode, str] = Field(
        default="0 0 800 600", description="SVG viewBox attribute"
    )
    scale: int | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Scale factor for rasterization"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.SVGToImage"


import nodetool.nodes.lib.svg


class Text(GraphNode):
    """
    Add text elements to SVG.
    svg, text, typography

    Use cases:
    - Add labels to vector graphics
    - Create text-based logos
    - Generate dynamic text content in SVGs
    """

    SVGTextAnchor: typing.ClassVar[type] = nodetool.nodes.lib.svg.SVGTextAnchor
    text: str | GraphNode | tuple[GraphNode, str] = Field(
        default="", description="Text content"
    )
    x: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="X coordinate"
    )
    y: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Y coordinate"
    )
    font_family: str | GraphNode | tuple[GraphNode, str] = Field(
        default="Arial", description="Font family"
    )
    font_size: int | GraphNode | tuple[GraphNode, str] = Field(
        default=16, description="Font size"
    )
    fill: types.ColorRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ColorRef(type="color", value="#000000"), description="Text color"
    )
    text_anchor: nodetool.nodes.lib.svg.SVGTextAnchor = Field(
        default=nodetool.nodes.lib.svg.SVGTextAnchor.START,
        description="Text anchor position",
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Text"


class Transform(GraphNode):
    """
    Apply transformations to SVG elements.
    svg, transform, animation

    Use cases:
    - Rotate, scale, or translate elements
    - Create complex transformations
    - Prepare elements for animation
    """

    content: types.SVGElement | GraphNode | tuple[GraphNode, str] = Field(
        default=None, description="SVG element to transform"
    )
    translate_x: float | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="X translation"
    )
    translate_y: float | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Y translation"
    )
    rotate: float | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Rotation angle in degrees"
    )
    scale_x: float | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="X scale factor"
    )
    scale_y: float | GraphNode | tuple[GraphNode, str] = Field(
        default=1, description="Y scale factor"
    )

    @classmethod
    def get_node_type(cls):
        return "lib.svg.Transform"
