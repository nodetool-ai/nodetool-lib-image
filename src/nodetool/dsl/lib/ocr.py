from pydantic import Field
import typing
import nodetool.metadata.types as types
from nodetool.dsl.graph import GraphNode

import nodetool.nodes.lib.ocr


class PaddleOCRNode(GraphNode):
    """
    Performs Optical Character Recognition (OCR) on images using PaddleOCR.
    image, text, ocr, document

    Use cases:
    - Text extraction from images
    - Document digitization
    - Receipt/invoice processing
    - Handwriting recognition
    """

    OCRLanguage: typing.ClassVar[type] = nodetool.nodes.lib.ocr.OCRLanguage
    image: types.ImageRef | GraphNode | tuple[GraphNode, str] = Field(
        default=types.ImageRef(type="image", uri="", asset_id=None, data=None),
        description="The image to perform OCR on",
    )
    language: nodetool.nodes.lib.ocr.OCRLanguage = Field(
        default=nodetool.nodes.lib.ocr.OCRLanguage.ENGLISH,
        description="Language code for OCR",
    )

    @classmethod
    def get_node_type(cls):
        return "lib.ocr.PaddleOCR"
