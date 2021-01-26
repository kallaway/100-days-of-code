import React from "react";

function App() {
  const books = [
    { id: 1, title: "超入門" },
    { id: 2, title: "開発 現場の教科書" },
    { id: 3, title: "ビギナーズガイド" },
  ];
  const listItems = (library, library2) =>
    books.map((book) => (
      <li key={book.id}>
        {library}
        {library2}
        {book.title}
      </li>
    ));
  return (
    <div>
      <ul>{listItems("Vue.js", "bbb")}</ul>
    </div>
  );
}

export default App;
