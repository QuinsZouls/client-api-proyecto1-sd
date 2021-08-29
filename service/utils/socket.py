import os
MSGLEN = os.getenv('SERVER_URL', 1024)
def socketMessage(s, msg):
  totalsent = 0
  while totalsent < MSGLEN:
      sent = s.send(msg[totalsent:])
      if sent == 0:
          raise RuntimeError("socket connection broken")
      totalsent = totalsent + sent
def socketCatchMessaje(s):
  chunks = []
  bytes_recd = 0
  while bytes_recd < MSGLEN:
      chunk = s.recv(min(MSGLEN - bytes_recd, 2048))
      if chunk == b'':
          raise RuntimeError("socket connection broken")
      chunks.append(chunk)
      bytes_recd = bytes_recd + len(chunk)
  return b''.join(chunks)

def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE - BUFF_SIZE * 0.1:
            # either 0 or end of data
            break
    return data