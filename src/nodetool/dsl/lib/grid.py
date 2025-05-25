from pydantic import Field
import nodetool.metadata.types as types
from nodetool.dsl.graph import GraphNode


class CombineImageGrid(GraphNode):
    """
    Combine a grid of image tiles into a single image.
    image, grid, combine, tiles

    Use cases:
    - Reassemble processed image chunks
    - Create composite images from smaller parts
    - Merge tiled image data from distributed processing
    """

    tiles: list[types.ImageRef] | GraphNode | tuple[GraphNode, str] = Field(
        default=[], description="List of image tiles to combine."
    )
    columns: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Number of columns in the grid."
    )

    @classmethod
    def get_node_type(cls):
        return "lib.grid.CombineImageGrid"


class SliceImageGrid(GraphNode):
    """
    Slice an image into a grid of tiles.
    image, grid, slice, tiles

    Use cases:
    - Prepare large images for processing in smaller chunks
    - Create image puzzles or mosaic effects
    - Distribute image processing tasks across multiple workers
    """

    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="The image to slice into a grid.",
    )
    columns: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Number of columns in the grid."
    )
    rows: int | GraphNode | tuple[GraphNode, str] = Field(
        default=0, description="Number of rows in the grid."
    )

    @classmethod
    def get_node_type(cls):
        return "lib.grid.SliceImageGrid"
