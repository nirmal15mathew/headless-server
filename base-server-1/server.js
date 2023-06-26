const { Server } = require("socket.io");

const io = new Server({ /* options */ });

export default function start_server() {

    console.log("Server started")
    console.log("Listening on port: %d", 3000)
    io.on("connection", (socket) => {
        console.log(`Client connected ${socket.id}`)
        socket.send("Hello from raspberry pi")
    });

    io.listen(3000);
}