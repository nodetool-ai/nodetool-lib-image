# Nodetool Image Library

A powerful image processing library that provides a collection of nodes for SVG manipulation, OCR (Optical Character Recognition), and image grid operations.

## Features

### SVG Manipulation

The library provides a comprehensive set of nodes for creating and manipulating SVG elements:

- Basic Shapes

  - Rectangle (`RectNode`)
  - Circle (`CircleNode`)
  - Ellipse (`EllipseNode`)
  - Line (`LineNode`)
  - Polygon (`PolygonNode`)
  - Path (`PathNode`)

- Text and Typography

  - Text elements with customizable properties (`Text`)
  - Support for different font families, sizes, and alignments

- Effects and Styling

  - Gaussian Blur (`GaussianBlur`)
  - Drop Shadow (`DropShadow`)
  - Gradients (`Gradient`)
  - Transformations (`Transform`)
  - Clipping Paths (`ClipPath`)

- Document Management
  - SVG Document creation and manipulation (`Document`)
  - SVG to raster image conversion (`SVGToImage`)

### Optical Character Recognition (OCR)

The library includes powerful OCR capabilities using PaddleOCR:

- Support for multiple languages including:

  - Latin script languages (English, French, German, Spanish, etc.)
  - Cyrillic script languages (Russian, Bulgarian, Ukrainian, etc.)
  - CJK languages (Chinese, Japanese, Korean)
  - Arabic script languages
  - Indic scripts

- Use cases:
  - Text extraction from images
  - Document digitization
  - Receipt/invoice processing
  - Handwriting recognition

### Image Grid Operations

Tools for handling large images and tiled processing:

- `SliceImageGrid`: Split images into customizable grids

  - Control over columns and rows
  - Support for overlap between tiles
  - Useful for processing large images in chunks

- `CombineImageGrid`: Merge image tiles back into a single image
  - Automatic handling of grid layout
  - Perfect for reassembling processed chunks

## Usage Examples

### Creating an SVG Shape

```python
rect_node = RectNode(
    x=10,
    y=10,
    width=100,
    height=50,
    fill=ColorRef(value="#FF0000"),
    stroke=ColorRef(value="#000000"),
    stroke_width=2
)
```

### Performing OCR

```python
ocr_node = PaddleOCRNode(
    image=image_ref,
    language=OCRLanguage.ENGLISH
)
```

### Processing Large Images

```python
# Slice image into grid
slice_node = SliceImageGrid(
    image=large_image,
    columns=3,
    rows=3
)

# Process tiles...

# Recombine processed tiles
combine_node = CombineImageGrid(
    tiles=processed_tiles,
    columns=3
)
```

## Installation

Install in the Nodetool UI or manually:

```bash
nodetool-package install nodetool-ai/nodetool-lib-image
```

## Dependencies

- PIL/Pillow
- PaddleOCR
- Pydantic

## License

AGPL
