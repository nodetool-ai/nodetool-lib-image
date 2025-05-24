# Nodetool Image Library

This package provides a set of reusable nodes for [Nodetool](https://github.com/nodetool-ai/nodetool). The nodes are implemented using [nodetool-core](https://github.com/nodetool-ai/nodetool-core) and can be used inside the Nodetool UI or in custom workflows.

## Node Catalog

### Pillow Operations

* **Blend** – blend two images with adjustable alpha.
* **Composite** – composite two images using a mask.

**Drawing**

* **Background** – create a blank image of a given size and color.
* **RenderText** – draw text on an image.
* **GaussianNoise** – generate an image filled with Gaussian noise.

**Enhance**

* **AutoContrast** – automatically adjust contrast.
* **Sharpness** – control image sharpness.
* **Equalize** – apply histogram equalization.
* **Contrast** – adjust contrast level.
* **EdgeEnhance** – emphasize edges.
* **Sharpen** – sharpen an image.
* **RankFilter** – rank based filtering.
* **UnsharpMask** – sharpen using the unsharp mask technique.
* **Brightness** – adjust brightness.
* **Color** – adjust color balance.
* **Detail** – enhance fine details.
* **AdaptiveContrast** – CLAHE based contrast enhancement.

**Filters**

* **Invert** – invert colors.
* **Solarize** – apply solarization.
* **Posterize** – reduce number of colors.
* **Expand** – add a border around an image.
* **Blur** – Gaussian blur.
* **Contour** – contour detection filter.
* **Emboss** – emboss effect.
* **FindEdges** – edge detection.
* **Smooth** – smooth an image.
* **Canny** – Canny edge detection.
* **ConvertToGrayscale** – convert to grayscale.
* **GetChannel** – extract a single color channel.

### SVG Generation

Nodes for creating and manipulating SVG graphics:

* **RectNode**, **CircleNode**, **EllipseNode**, **LineNode**, **PolygonNode**, **PathNode** – basic shapes.
* **Text** – add text elements.
* **GaussianBlur**, **DropShadow**, **Gradient**, **Transform**, **ClipPath** – SVG filters and effects.
* **Document** – build an SVG document from elements.
* **SVGToImage** – rasterize an SVG document to an image.

### OCR

* **PaddleOCRNode** – run Optical Character Recognition using PaddleOCR with support for many languages.

### Image Grids

* **SliceImageGrid** – cut an image into a grid of tiles.
* **CombineImageGrid** – recombine tiles back into a single image.

## Installation

Install directly in the Nodetool UI or with the CLI:

```bash
nodetool-package install nodetool-ai/nodetool-lib-image
```

## Example

```python
from nodetool.nodes.lib.pillow.enhance import AutoContrast
from nodetool.nodes.lib.pillow.filter import Blur

# enhance an image
node1 = AutoContrast(image=input_img)
node2 = Blur(image=node1.output, radius=2)
```

See the [Nodetool](https://github.com/nodetool-ai/nodetool) documentation for details on how to build full workflows.

## License

AGPL
