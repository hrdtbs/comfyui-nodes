# Resolution Selector

Stable Diffusionモデルで一般的に推奨される解像度を簡単に選択できるノードです。

## ノード一覧

### Resolution Selector
リストから解像度を選択し、幅(width)と高さ(height)を出力します。
SD1.5, SDXL, Illustrious モデルに対応したプリセットが含まれています。

#### 入力 (Inputs)
- **resolution** (STRING): ドロップダウンから選択します。
  - SD1.5: 512x512, 768x512, 512x768 など
  - SDXL / Illustrious: 1024x1024, 1152x896, 1216x832 など

#### 出力 (Outputs)
- **width** (INT): 選択された解像度の幅。
- **height** (INT): 選択された解像度の高さ。
