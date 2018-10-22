from pwn import *
CUR_PORT = 10002
r = remote('localhost',CUR_PORT)
send_msg = chr(0) + chr(0)*15
print("send msg: ",send_msg)
r.sendline(send_msg)
msg_00 = r.recv()
print("recv msg: ", msg_00)
hashed_msg = msg_00[1:16]
mac = msg_00[16:]
print("hashed_msg: ",hashed_msg)
print("mac: ",mac)
