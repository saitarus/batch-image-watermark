# -*- coding: utf-8 -*-
"""
Batch Image Watermark CLI
ディレクトリ内の画像を一括で正方形リサイズ＆透かし合成・最適化保存
"""

import os
import sys
import argparse
from processor import ImageProcessor

SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}


def batch_process(input_dir: str, output_dir: str, watermark: str = "", size: int = 1000):
    if not os.path.isdir(input_dir):
        print(f"[Error] Input directory not found: {input_dir}", file=sys.stderr)
        return False

    os.makedirs(output_dir, exist_ok=True)
    processor = ImageProcessor(target_size=(size, size))

    files = [f for f in os.listdir(input_dir) if os.path.splitext(f.lower())[1] in SUPPORTED_EXTS]
    print(f"Found {len(files)} image(s) to process in {input_dir}")

    success_count = 0
    for filename in files:
        in_path = os.path.join(input_dir, filename)
        base, _ = os.path.splitext(filename)
        out_path = os.path.join(output_dir, f"{base}.jpg")

        if processor.process_file(in_path, out_path, watermark=watermark if watermark else None):
            success_count += 1
            print(f" -> Processed: {filename}")

    print(f"Finished: {success_count}/{len(files)} image(s) successfully processed.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Batch Image Watermark & Square Resizer")
    parser.add_argument("input_dir", help="Directory containing source images")
    parser.add_argument("--output_dir", default="./output", help="Destination output directory")
    parser.add_argument("--watermark", default="", help="Optional watermark text")
    parser.add_argument("--size", type=int, default=1000, help="Square canvas dimension (pixels)")
    args = parser.parse_args()

    batch_process(args.input_dir, args.output_dir, watermark=args.watermark, size=args.size)


if __name__ == "__main__":
    main()
