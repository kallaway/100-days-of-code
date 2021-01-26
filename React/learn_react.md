# React の用語

- コンポーネント 部品。JavaScript または TypeScript で定義する
  - 関数コンポーネント
- JSX
  - JavaScript 構文の拡張
  - JavaScript に HTML のような構文を書ける
  - JSX は JS に変換する必要がある
- state（状態）
- ライフサイクル
  - マウント（描画）されてから、アンマウント（破棄）するまでの過程
  - マウント → 更新 → アンマウント
- フック
  - 関数コンポーネントで利用できる関数
  - カスタムフック 自作のフック
  - コンポーネント内で重複するロジックをフックとして切り出すことで、複数のコンポーネントで共通利用できる
  - コードの見通しがよくなる
  - フックはただの関数

## Create React App とは

- React アプリケーションの開発環境を構築できる Facebook の公式ツール
  - かんたんに環境を構築できる
  - エラーの警告を出力してくれる
- Node.js が必要

```sh
> node -v
v12.16.1

> npm -v
6.13.4

> yarn -v
1.22.4
```

- React アプリケーションの開発環境を構築する

```sh
> npx create-react-app react-starter
```

### npx コマンドに関して

- create-react-app コマンドを使用するために、npx を使用
- ローカルにインストールされていないパッケージをインストールしてから実行してくれるコマンド
- コマンド実行後はパッケージが破棄されるので、create-react-app は残らない

## アプリケーション起動

```sh
cd react-starter
yarn start
```

- 不要なファイルを削除する

*2021/01/25 終了*

---
*2021/01/26開始*

# Reactの基礎

## JSX

- 式を埋め込むには、`{}`で囲む
  

```jsx
import React from 'react';

/* 1. JavaScript 式を埋め込む */
function add(a, b) {
  return a + b;
}

function App() {
  const message = 'React';

  return (
    <div>
      <p>Hello {message}</p>
      <p>1 + 2 = {add(1, 2)}</p>
    </div>
  );
}

export default App;
```

## JSXのルール

- ルート要素は1つだけ
  - タグが深くならないように、`<></>`フラグメントを使用する
- 全てのタグを閉じる
  - `<br>`などの閉じていないタグが存在するとエラー
- classなどの属性は利用できず、代替の属性を利用する必要がある
  - `class` → `className`を使う

## コンポーネント

- 関数宣言やアロー関数で定義する
- コンポーネント名の最初は必ず大文字にする (hello不可)
- 定義されたコンポーネントは、`<Hello />`のように使用する

```jsx
function Hello() {
  return <h1>Hello React</h1>;
}


function App() {
  return (
    <div>
      <Hello />
    </div>
  );
}
```

### props


```jsx
//props.name を受け突る
function Hello({ name }) {
  return <p>Hello, {name}</p>;
}
function App() {
  const message = 'Angular';
  return (
    <div>
      {/* "React" を Props として渡す */}
      <Hello name="React" />
      {/* "Vue.js" を Props として渡す */}
      <Hello name="Vue.js" />

      <Hello name={message} />
    </div>
  );
}
```

- propsをまとめて渡す

```jsx
function Hello({ firstName, lastName }) {
  return <p>Hello, {firstName} {lastName}</p>;
}
function App() {
  const data = {
    firstName: 'John',
    lastName: 'Doe'
  };
  return (
    <div>
      <Hello {...data} />
    </div>
  );
}
```

## 条件分岐

- 条件に応じたJSXを返す
- `&&`演算子を利用する
- 三項演算子を利用する
- 即時関数を利用する

### 条件に応じたJSXを返す

```jsx
function Hello({ isReact }) {
  if (isReact) {
    return <p>Hello React</p>;
  }

  return <p>Hello Vue.js</p>;
}

function App() {
  const isReact = false;

  return <Hello isReact={isReact} />;
}
```

### `&&`演算子を利用する

```jsx
function App() {
  const isReact = true;
  return (
    <div>
      {isReact && <p>Hello React</p>}
      {!isReact && <p>Hello Vue.js</p>}
    </div>
  );
}
```

### 三項演算子を利用する

```jsx
function App() {
  const isReact = true;
  return isReact ? <p>Hello React</p> : <p>Hello Vue.js</p>;
}
```

### 即時関数を利用する

```jsx
function App() {
  const isReact = false;
  return (
    <div>
      {(() => {
        if (isReact) {
          return <p>Hello React</p>;
        }
        return <p>Hello Vue.js</p>;
      })()}
    </div>
  );
}
```

## 繰り返し描画

- mapを埋め込む
- mapの実行結果が格納された変数を埋め込む
- mapの実行結果を返す関数を埋め込む


### mapを埋め込む

- key属性を指定することを強く推奨されている

```jsx
function App() {
  const books = [
    { id: 1, title: 'React.js&Next.js超入門' },
    { id: 2, title: 'React開発 現場の教科書' },
    { id: 3, title: 'Reactビギナーズガイド' }
  ];

  return (
    <ul>
      {books.map(book => (
        // key 属性は必ず指定する
        <li key={book.id}>{book.title}</li>
      ))}
    </ul>
  );
}
```

### mapの実行結果が格納された変数を埋め込む

```jsx
function App() {
  const books = [
    { id: 1, title: 'React.js&Next.js超入門' },
    { id: 2, title: 'React開発 現場の教科書' },
    { id: 3, title: 'Reactビギナーズガイド' }
  ];
  const listItems = books.map(book => <li key={book.id}>{book.title}</li>);
  return (
    <div>
      <ul>{listItems}</ul>
    </div>
  );
}
```

### mapの実行結果を返す関数を埋め込む

```jsx
function App() {
  const books = [
    { id: 1, title: '超入門' },
    { id: 2, title: '開発 現場の教科書' },
    { id: 3, title: 'ビギナーズガイド' }
  ];
  const listItems = library =>
    books.map(book => (
      <li key={book.id}>
        {library}
        {book.title}
      </li>
    ));
  return (
    <div>
      <ul>{listItems('Vue.js')}</ul>
    </div>
  );
}
```
