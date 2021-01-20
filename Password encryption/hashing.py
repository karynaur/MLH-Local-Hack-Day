"""
##String hashing
-generate a p
-generate a m
-hashing
---hash=0,pow=1
---iterate through ASCII of characters in string and multiply by p**index
---return hash%m 

"""
s='hello'

def hashing(s,p):
  num=0
  m=9283742
  for i,c in enumerate(s):
    num=num+(ord(c)*(p**i))
  return num%m 

print(hashing(s,5))
