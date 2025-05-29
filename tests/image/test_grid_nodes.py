import pytest
from io import BytesIO
from PIL import Image

from nodetool.metadata.types import ImageRef
from nodetool.nodes.lib.grid import SliceImageGrid, CombineImageGrid
from nodetool.workflows.processing_context import ProcessingContext

buffer = BytesIO()
Image.new("RGB", (100, 100), color="blue").save(buffer, format="PNG")
DUMMY_IMAGE = ImageRef(data=buffer.getvalue())


@pytest.mark.asyncio
async def test_slice_image_grid(context: ProcessingContext):
    node = SliceImageGrid(image=DUMMY_IMAGE, columns=2, rows=2)
    tiles = await node.process(context)
    assert len(tiles) == 4
    for tile in tiles:
        pil = await context.image_to_pil(tile)
        assert pil.size == (50, 50)


@pytest.mark.asyncio
async def test_combine_image_grid(context: ProcessingContext):
    slice_node = SliceImageGrid(image=DUMMY_IMAGE, columns=2, rows=2)
    tiles = await slice_node.process(context)
    combine_node = CombineImageGrid(tiles=tiles, columns=2)
    combined = await combine_node.process(context)
    pil = await context.image_to_pil(combined)
    assert pil.size == (100, 100)


@pytest.mark.asyncio
async def test_combine_image_grid_no_tiles(context: ProcessingContext):
    node = CombineImageGrid(tiles=[], columns=2)
    with pytest.raises(ValueError):
        await node.process(context)
