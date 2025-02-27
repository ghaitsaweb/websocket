# websocket
this code build express.js with socket IO

server.js (Node.js Server)
-Create server HTTP and socket.io
-accept connected form client and create message time client connect
-read event message from client,and then send response 'echo message'
-write message if client disconnected
-server running on port 3000

client.py(Python Client)
-with library socketio for connected to server node js
-event connected , client send message 'Hello from python"
-event accept mesage, this print message from server
-event disconnected, print message
-connected to server js with Docker Compose



