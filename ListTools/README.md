# ListTools

リスト操作に関連するノード群です。

## Nodes

### List Get Item (ListGetItem)
リストから指定したインデックスの要素を取得します。
- **Inputs**:
  - `list_input`: 任意のリスト (AnyType)
  - `index`: 取得したい要素のインデックス (INT)
- **Outputs**:
  - `item`: 指定されたインデックスの要素

### List Length (ListLength)
リストの長さを取得します。
- **Inputs**:
  - `list_input`: 任意のリスト (AnyType)
- **Outputs**:
  - `length`: リストの要素数 (INT)
