# Anatomy Guard

生成された画像内の手や身体の構造を検証し、崩れている箇所を自動的に修正するためのノード群です。
MediaPipe を使用して手のランドマークを検出し、その妥当性を評価します。

## 前提条件
このノードを使用するには以下のライブラリが必要です（`requirements.txt` に含まれています）。
- mediapipe
- opencv-python

## ノード一覧

### Anatomy Detection Mesh
入力画像から手を検出し、内部データ形式に変換します。

#### 入力 (Inputs)
- **image** (IMAGE): 手を検出したい画像。

#### 出力 (Outputs)
- **hand_data**: 検出された手のランドマーク情報などを含むデータ。

---

### Anatomy Logic Evaluator
検出された手のデータに基づいて、解剖学的な正しさ（指の角度や重なりなど）を評価します。

#### 入力 (Inputs)
- **hand_data**: `Anatomy Detection Mesh` からの出力。
- **threshold** (FLOAT): 判定の厳しさ（0.0～1.0）。値が小さいほど厳しく判定します。

#### 出力 (Outputs)
- **condition** (BOOLEAN):手が正常と判断されれば `True`、異常があれば `False`。
- **mask** (MASK): 異常と判断された手の領域マスク。

---

### Iterative Anatomy Refiner
異常と判定された領域（マスク部分）に対して再生成（インペイント）を行い、修正を試みます。

#### 入力 (Inputs)
- **image** (IMAGE): 元の画像。
- **mask** (MASK): 修正対象のマスク。
- **model** (MODEL): チェックポイントモデル。
- **seed** (INT): シード値。
- **steps** (INT): サンプリングステップ数。
- **cfg** (FLOAT): CFGスケール。
- **denoise** (FLOAT): Denoise強度。
- **vae** (Optional): VAE。
- **positive** (Optional): ポジティブプロンプト。
- **negative** (Optional): ネガティブプロンプト。

#### 出力 (Outputs)
- **refined_image** (IMAGE): 修正後の画像。
