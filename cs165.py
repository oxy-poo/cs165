import hashlib
import struct
#print "Hello, Init"
pw = "zhgnnd".encode('utf-8')
salt = "hfT7jp2q".encode('utf-8')

magic = "$1$".encode('utf-8')
pwlen = len(pw)
itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

a = hashlib.md5(pw + salt + pw).digest()
print("alternate sum:",hashlib.md5(pw + salt + pw).hexdigest())
print("alternate sum digest:",a)
b = pw + magic + salt + a[:6]
print(b)
lp = len(pw)
while lp != 0:
	if(lp & 1):
		b+= b'\0'
	else:
		b+= struct.pack("B",pw[0])
	lp>>=1
print(b)
		
intermediate = hashlib.md5(b).hexdigest()

print(intermediate)

	
