import socketio

# Standard Python library
sio = socketio.Client()

@sio.event
def connect():
    print('Connection established')
    sio.send('Hello from Python')

@sio.event
def message(data):
    print('Message received from server:', data)

@sio.event
def disconnect():
    print('Disconnected from server')

if __name__ == '__main__':
    sio.connect('http://node-app:3000')
    sio.wait()
