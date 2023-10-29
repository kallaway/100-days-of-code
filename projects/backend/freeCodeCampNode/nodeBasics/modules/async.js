const http = require("http");

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Hello World\n");
  }
  if (req.url === "/about") {
    res.end("About me\n");
  }
  res.end(`<h1>Oops</h1>
  <h2>404 Not Found</h2>`);
});

server.listen(5000, () => {
  console.log("listening on *:5000");
});
