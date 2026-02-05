# ComfyUI Custom Node Repository

このリポジトリは、[ComfyUI](https://github.com/comfyanonymous/ComfyUI) 用のカスタムノードを配置するための自分用リポジトリです。カスタムノードの作成方法を理解するための参考実装とドキュメントを含んでいます。

## Math: 基本的な計算ノード

`Math` ディレクトリに単純なカスタムノードの参考実装を用意しました。基本的な整数の加算を行います。

### 構造

実装は標準的なComfyUIカスタムノードの構造に従っています：

- `Math/nodes.py`: ノードクラスの定義 (`MathAdd`) を含みます。
  - `INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION`, `CATEGORY` を定義しています。
- `Math/__init__.py`: ノードを登録します。
  - `NODE_CLASS_MAPPINGS` と `NODE_DISPLAY_NAME_MAPPINGS` をエクスポートしています。

### 使い方

このノードをComfyUIで使用するには：

1. このリポジトリをComfyUIの `custom_nodes` ディレクトリにクローンします：
   ```bash
   cd ComfyUI/custom_nodes
   git clone <このリポジトリのURL>
   ```
2. ComfyUIを再起動します。
3. カテゴリ `h2nodes` -> `Math` -> `Math Add` の下にノードが表示されます。

## Wireless: ワイヤレスデータ転送

`Wireless` ディレクトリに、ノード間でワイヤレスにデータを転送するためのノード実装を追加しました。"Anything Everywhere" に相当する機能を提供しますが、JavaScriptによる自動接続ではなく、明示的な送信(Send)と受信(Receive)のノードペアを使用します。

### ノード

- **Wireless Send**: 任意のデータを受け取り、指定したキーでグローバルに保存します。
  - カテゴリ: `h2nodes` -> `Wireless`
- **Wireless Receive**: 指定したキーに対応するデータを取得して出力します。
  - カテゴリ: `h2nodes` -> `Wireless`

### 使い方

1. `Wireless Send` ノードを配置し、`key` を設定してデータを `data` 入力に接続します。
2. `Wireless Receive` ノードを配置し、同じ `key` を設定します。
3. **注意**: ComfyUIの実行順序はワイヤー接続に依存するため、`Receive` ノードが `Send` ノードより後に実行されることを保証する必要があります。必要に応じて `Receive` ノードの `trigger` 入力に、`Send` ノードより前の処理の結果を接続するなどして順序を制御してください。

## リソースとベストプラクティス

カスタムノードの開発には、以下のリソースが推奨されます：

- **公式ウォークスルー**: [ComfyUI Custom Nodes Walkthrough](https://docs.comfy.org/custom-nodes/walkthrough)
  - カスタムノードを作成するための主要なガイドです。
- **公式レジストリ概要**: [ComfyUI Registry Documentation](https://docs.comfy.org/registry/overview)
  - ノードの公開や標準仕様に関する情報です。
- **ComfyUI Manager**: [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
  - カスタムノードを管理するための有名な拡張機能です。その構造も参考になります。
- **公式リポジトリ**: [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- **公式Example集**: [ComfyUI Examples](https://comfyanonymous.github.io/ComfyUI_examples/)
