# AnatomyGuard

MediaPipeを使用して人物の解剖学的構造（現在は手のみ）を検出し、異常な形状を修正するためのノード群です。

## 依存関係 (Dependencies)

このノード群を使用するには、以下のPythonパッケージが必要です。
* `mediapipe`
* `opencv-python`

## ノード一覧

### 1. AnatomyDetectionMesh

入力画像から手を検出し、ランドマークデータを出力します。

**入力 (Inputs)**
* `image` (IMAGE): 検出対象の画像。

**出力 (Outputs)**
* `hand_data` (HAND_DATA): 検出された手のランドマーク情報を含むデータ構造。

---

### 2. AnatomyLogicEvaluator

検出された手の形状を幾何学的に評価し、不自然な場合（指の角度や関節距離など）に修正用のマスクを生成します。

**入力 (Inputs)**
* `hand_data` (HAND_DATA): `AnatomyDetectionMesh` からの出力。
* `threshold` (FLOAT): 異常判定の感度しきい値。値が小さいほど厳しく判定されます。デフォルトは `0.05`。

**出力 (Outputs)**
* `condition` (BOOLEAN): 全ての手が正常と判定された場合は `True`、異常がある場合は `False`。
* `mask` (MASK): 異常と判定された手の領域を示すマスク画像。

---

### 3. IterativeAnatomyRefiner

生成されたマスク領域に対して、Inpainting（修復）を行い、解剖学的に正しい画像を生成しようと試みます。

**入力 (Inputs)**
* `image` (IMAGE): 元画像。
* `mask` (MASK): `AnatomyLogicEvaluator` からのマスク。
* `model` (MODEL): 修復に使用するモデル。
* `seed` (INT): シード値。
* `steps` (INT): サンプリングステップ数。
* `cfg` (FLOAT): CFGスケール。
* `denoise` (FLOAT): デノイズ強度。通常は `1.0` (完全書き換え) に近い値を使用します。
* `vae` (VAE, optional): VAEモデル。
* `positive` (CONDITIONING, optional): 正のプロンプト条件。
* `negative` (CONDITIONING, optional): 負のプロンプト条件。
* `controlnet_stack` (CONTROLNET_STACK, optional): ControlNetスタック（現在は未使用の可能性があります）。

**出力 (Outputs)**
* `refined_image` (IMAGE): 修復後の画像。
