import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import pytest
from PIL import Image
from processor import ImageProcessor


def test_resize_with_padding():
    # 400x200 の横長画像をシミュレート
    img = Image.new("RGB", (400, 200), (255, 0, 0))
    processor = ImageProcessor(target_size=(500, 500), bg_color=(255, 255, 255))
    res = processor.resize_with_padding(img)

    assert res.size == (500, 500)
    # 上下余白（背景色 255, 255, 255）が維持されていること
    assert res.getpixel((0, 0)) == (255, 255, 255)


def test_apply_watermark():
    img = Image.new("RGB", (300, 300), (200, 200, 200))
    processor = ImageProcessor()
    watermarked = processor.apply_watermark(img, "SAMPLE WATERMARK")

    assert watermarked.size == (300, 300)
    assert watermarked.mode == "RGB"
