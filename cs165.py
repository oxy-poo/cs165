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

inter = hashlib.md5(b)

print(intermediate)
"""
for (i=0; i<1000; i++) {
  ctx1 = "";
  if (i & 1) ctx1 += password;
  else ctx1 += ctx;

  if (i % 3) ctx1 += salt;

  if (i % 7) ctx1 += password;

  if (i & 1) ctx1 += ctx;
  else ctx1 += password;

  ctx = str_md5(ctx1);
 }
 """
for i in range(1000):
	#inter = hashlib.md5()
	#print(i)
	if i & 1:
		inter.update(pw)
	else:
		inter.update(inter.digest())
	if i % 3:
		inter.update(salt)
	if i % 7:
		inter.update(pw)
	if i & 1:
		inter.update(inter.digest())
	else:
		inter.update(pw)
		
		
print(inter.hexdigest())
		

 
 
