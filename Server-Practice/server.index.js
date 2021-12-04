const http = require("http");
// const { getAllData } = require("./controller/controller");

const raysSoloServer = http.createServer(function(request, response) {
  const { method, url } = request;
  if (method === "GET" && url === "/api/data") {
    console.log("request for all data change");
    //getAllData(request, response);
  }
});

raysSoloServer.listen(8101, function() {
  console.log("Ray's Server - Listening for requests");
});
