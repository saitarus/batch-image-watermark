# Batch Image Watermark & Optimizer 🖼️

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Image%20Processing-Pillow-blue.svg)](https://python-pillow.org/)
[![CI](https://github.com/saitarus/batch-image-watermark/actions/workflows/ci.yml/badge.svg)](https://github.com/saitarus/batch-image-watermark/actions)

**アスペクト比維持リサイズ・正方形余白パディング・半透明透かし合成・JPEG/WebP一括最適化 CLI**

A high-performance batch image processor that resizes images with aspect-ratio padding, applies semi-transparent watermarks, and optimizes files for e-commerce and web publishing using Python (Pillow).

---

## 🌟 主な特徴 (Features)

1. **アスペクト比維持 ＆ 正方形パディング (Smart Resizing)**
   - 画像の歪みを一切生じさせず、LANCZOS 高品質リサンプリングでリサイズ。
   - 余白を指定色（デフォルト: 白 `#FFFFFF`）で自動補正し、EC や SNS に最適な完全正方形（1:1）キャンバスに出力。
2. **半透明テキスト透かし合成 (Alpha Composite Watermarking)**
   - アルファチャンネル（RGBA）を用いた美しい半透明ウォーターマーク（ロゴ/コピーライト）の重ね合わせ。
   - 画像サイズに応じた柔軟な配置位置（右下、中央等）。
3. **ディレクトリ一括バッチ処理 (Fast Batch Processing)**
   - フォルダ内の画像（JPEG, PNG, WebP, BMP）を一括巡回し、自動最適化保存。
   - 画像圧縮最適化（`optimize=True`）により、画質を保ったままファイルサイズを最小化。

---

## 📁 ディレクトリ構成 (Architecture)

```text
batch-image-watermark/
├── tests/
│   └── test_processor.py     # 単体テスト (リサイズ・パディング・透かし合成)
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI
├── processor.py              # Pillow 画像処理コアモジュール
├── cli.py                    # ディレクトリ一括処理 CLI ツール
├── requirements.txt          # 依存パッケージ (Pillow, pytest, flake8)
├── .gitignore                # 画像・成果物除外設定
├── LICENSE                   # MIT ライセンス
└── README.md                 # 本ドキュメント
```

---

## 🚀 クイックスタート (Quick Start)

### 1. リポジトリのクローンとインストール

```bash
git clone https://github.com/saitarus/batch-image-watermark.git
cd batch-image-watermark
pip install -r requirements.txt
```

### 2. 一括画像処理の実行

```bash
# 入力フォルダ内の画像を 1000x1000 の正方形に余白補正し、透かしを入れて output/ に保存
python cli.py ./images --output_dir ./output --watermark "© 2026 saitarus" --size 1000
```

---

## 📄 ライセンス (License)

本プロジェクトは [MIT License](LICENSE) のもとで公開されています。
