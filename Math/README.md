# Math

ComfyUI用のシンプルな数学演算ノードセットです。

## ノード一覧

### MathAdd

2つの整数を加算するシンプルなノードです。

**入力 (Inputs)**
* `a` (INT): 1つ目の整数。デフォルトは0。
* `b` (INT): 2つ目の整数。デフォルトは0。

**出力 (Outputs)**
* `result` (INT): `a` と `b` の合計値。

### MathSubtract

2つの整数を減算するシンプルなノードです。

**入力 (Inputs)**
* `a` (INT): 1つ目の整数。デフォルトは0。
* `b` (INT): 2つ目の整数。デフォルトは0。

**出力 (Outputs)**
* `result` (INT): `a` から `b` を引いた値。

### MathMultiply

2つの整数を乗算するシンプルなノードです。

**入力 (Inputs)**
* `a` (INT): 1つ目の整数。デフォルトは0。
* `b` (INT): 2つ目の整数。デフォルトは0。

**出力 (Outputs)**
* `result` (INT): `a` と `b` の積。

### MathDivide

2つの整数を除算するシンプルなノードです。

**入力 (Inputs)**
* `a` (INT): 1つ目の整数。デフォルトは0。
* `b` (INT): 2つ目の整数。デフォルトは1。

**出力 (Outputs)**
* `result` (FLOAT): `a` を `b` で割った値。0で割った場合は0.0を返します。

### MathModulus

2つの整数の剰余を計算するシンプルなノードです。

**入力 (Inputs)**
* `a` (INT): 1つ目の整数。デフォルトは0。
* `b` (INT): 2つ目の整数。デフォルトは1。

**出力 (Outputs)**
* `result` (INT): `a` を `b` で割った余り。0で割った場合は0を返します。

### MathExpression

数式を評価するノードです。Pythonの標準的な数学関数や `a`, `b`, `c` 変数を使用できます。

**入力 (Inputs)**
* `expression` (STRING): 評価する数式 (例: `(a + b) * c`, `sqrt(a**2 + b**2)`).
* `a` (FLOAT): 変数 `a` の値。デフォルトは0.0。
* `b` (FLOAT): 変数 `b` の値。デフォルトは0.0。
* `c` (FLOAT): 変数 `c` の値。デフォルトは0.0。

**出力 (Outputs)**
* `result_int` (INT): 計算結果の整数部分（切り捨てなどではなく、単純な型変換）。
* `result_float` (FLOAT): 計算結果の浮動小数点数。

**使用可能な関数・定数**
* 基本演算: `+`, `-`, `*`, `/`, `**` (累乗), `%` (剰余)
* 変数: `a`, `b`, `c`
* 組み込み関数: `abs`, `min`, `max`, `round`, `sum`, `pow`
* Mathモジュール関数: `sin`, `cos`, `tan`, `sqrt`, `pi`, `e`, `floor`, `ceil` など

### MathClamp

値を指定された最小値と最大値の間に制限（クランプ）するノードです。

**入力 (Inputs)**
* `value` (FLOAT): 制限対象の値。
* `min` (FLOAT): 最小値。
* `max` (FLOAT): 最大値。

**出力 (Outputs)**
* `result_int` (INT): クランプされた値（整数）。
* `result_float` (FLOAT): クランプされた値（浮動小数点数）。

### MathRemap

値をある範囲から別の範囲へリニアマッピング（線形補間）するノードです。オプションでクランプも可能です。

**入力 (Inputs)**
* `value` (FLOAT): 変換対象の値。
* `input_min` (FLOAT): 入力範囲の最小値。
* `input_max` (FLOAT): 入力範囲の最大値。
* `output_min` (FLOAT): 出力範囲の最小値。
* `output_max` (FLOAT): 出力範囲の最大値。
* `clamp` (BOOLEAN): 計算結果を出力範囲内に制限するかどうか。デフォルトはFalse。

**出力 (Outputs)**
* `result_int` (INT): マッピングされた値（整数）。
* `result_float` (FLOAT): マッピングされた値（浮動小数点数）。
