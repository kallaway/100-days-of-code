const http = require("http");

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/plain" });
    return res.end("Hello Worlds\n");
  }
  if (req.url === "/about") {
    return res.end("About me\n");
  }
  res.end(`<h1>Oops</h1>
  <h2>404 Not Found</h2>`);
});

server.listen(5000, () => {
  console.log("listening on *:5000");
});
