import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6340))

msg="hello"
msg_len=len(msg)
msg=str(msg_len)+msg
sock.send(msg.encode('utf-8'))

msg_raw=sock.recv(20) # data receive
msg=msg_raw.decode("utf-8", "ignore")
print('msg received=', msg)

sock.close()