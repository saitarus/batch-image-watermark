# -*- coding: utf-8 -*-
"""
Batch Image Processor & Watermark Engine
アスペクト比維持リサイズ、正方形パディング、半透明透かし合成、WebP/JPEG最適化
"""

import os
from typing import Tuple, Optional
from PIL import Image, ImageDraw, ImageFont, ImageEnhance


class ImageProcessor:
    def __init__(self, target_size: Tuple[int, int] = (1000, 1000), bg_color: Tuple[int, int, int] = (255, 255, 255)):
        self.target_size = target_size
        self.bg_color = bg_color

    def resize_with_padding(self, image: Image.Image) -> Image.Image:
        """アスペクト比を維持しながら縮小/拡大し、指定背景色で余白を埋めて正方形に仕上げる"""
        img = image.convert("RGB")
        target_w, target_h = self.target_size

        # 元画像の比率を維持したリサイズ
        img.thumbnail((target_w, target_h), Image.Resampling.LANCZOS)

        # パディング用の新規キャンバス作成
        new_img = Image.new("RGB", (target_w, target_h), self.bg_color)
        paste_x = (target_w - img.width) // 2
        paste_y = (target_h - img.height) // 2
        new_img.paste(img, (paste_x, paste_y))
        return new_img

    def apply_watermark(
        self,
        base_image: Image.Image,
        watermark_text: str,
        opacity: float = 0.35,
        font_size: int = 36,
        position: str = "bottom-right"
    ) -> Image.Image:
        """半透明テキスト透かしを合成"""
        img = base_image.convert("RGBA")
        txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        try:
            # 汎用フォント読み込み
            font = ImageFont.load_default()
        except Exception:
            font = None

        # 描画位置の算出
        alpha = int(255 * opacity)
        text_color = (128, 128, 128, alpha)

        w, h = img.size
        # デフォルトは右下余白
        if position == "bottom-right":
            pos = (w - 200, h - 50)
        elif position == "center":
            pos = (w // 2 - 80, h // 2 - 20)
        else:
            pos = (20, 20)

        draw.text(pos, watermark_text, fill=text_color, font=font)
        combined = Image.alpha_composite(img, txt_layer)
        return combined.convert("RGB")

    def process_file(
        self,
        input_path: str,
        output_path: str,
        watermark: Optional[str] = None,
        quality: int = 85,
        output_format: str = "JPEG"
    ) -> bool:
        """単一画像の処理と保存"""
        try:
            with Image.open(input_path) as img:
                processed = self.resize_with_padding(img)
                if watermark:
                    processed = self.apply_watermark(processed, watermark)

                os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
                processed.save(output_path, format=output_format, quality=quality, optimize=True)
                return True
        except Exception as e:
            print(f"[Error] Failed to process {input_path}: {e}")
            return False
