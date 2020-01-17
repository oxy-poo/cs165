from hashlib import md5

#print "Hello, Init"
pw = "zhgnnd"
salt = "hfT7jp2q"

magic = "$1$"
pwlen = len(pw)
itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

da = md5()
da.update(pw)
da.update(magic)
da.update(salt)

print(da)

db = md5()
db.update(pw)
db.update(salt)
db.update(pw)
print(db)
final = db.digest()

i = pwlen
while i > 0:
  if(pwlen > 16):
    da.update(final)
    
  else:
    da.update(final[0:pwlen])
  i-=16
    

i = pwlen
while i:
  if i % 2 == 1:
    da.update(final[0])
  else:
    da.update(pw[0])
  i>>=1
dc = da.digest()
print(dc)

for i in xrange(1000):
  #print i
  tmp = md5()
  if i % 2 == 0:
    tmp.update(dc)
  else:
    tmp.update(pw)
  if i % 3 == 0:
    tmp.update(salt)
  if i % 7 == 0:
    tmp.update(pw)
  if i % 2 == 0:
    tmp.update(pw)
  else:
    tmp.update(dc)
  dc = tmp.digest()

print(len(dc))
print(tmp)

final = ''
bytes_order = [11,4,10,5,3,9,15,2,8,14,1,7,13,0,6,12]
print final