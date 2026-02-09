# Resolution Selector

SD 1.5, SDXL, Illustriousなどの主要な画像生成モデル向けの解像度プリセットを選択できるノードです。

## ノード一覧

### ResolutionSelector

プリセットリストから解像度を選択し、幅（Width）と高さ（Height）を出力します。

**入力 (Inputs)**
* `resolution` (STRING): 解像度プリセットのドロップダウンリスト。例: `SDXL / Illustrious - 1024x1024 (1:1)`

**出力 (Outputs)**
* `width` (INT): 選択された解像度の幅。
* `height` (INT): 選択された解像度の高さ。

**対応プリセット**
* SD 1.5 (512x512, 768x512, 512x768)
* SDXL / Illustrious (1024x1024, 1152x896, 896x1152 など多数)
