import argparse

def utf8len(s):
    return len(s.encode('utf-8'))*8

def SHA(s):

  h0 = 0x67452301
  h1 = 0xEFCDAB89
  h2 = 0x98BADCFE
  h3 = 0x10325476
  h4 = 0xC3D2E1F0
  
  byte=''
  ml=utf8len(s)
  for i in s:
    byte+='{0:08b}'.format(ord(i))
  
  bit=byte+'1'
  pad=bit
  while len(pad)%512 != 448:
    pad+="0"
  pad+='{0:064b}'.format(len(bit)-1)

  def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

  def rol(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

  for i in chunks(pad,512):
    word=chunks(i,32)
    w=[0]*80
    for j in range(80):
      if j<16:w[j]=int(word[j],2)
      else:w[j]=rol(w[j-3]^w[j-8]^w[j-14]^w[j-16],1)

      a = h0
      b = h1
      c = h2
      d = h3
      e = h4
      
      for i in range(80):
        if 0 <= i <= 19:
           f = (b & c) | ((~b) & d)
           k = 0x5A827999
        elif 20 <= i <= 39:
           f = b ^ c ^ d
           k = 0x6ED9EBA1
        elif 40 <= i <= 59:
           f = (b & c) | (b & d) | (c & d) 
           k = 0x8F1BBCDC
        elif 60 <= i <= 79:
           f = b ^ c ^ d
           k = 0xCA62C1D6                   
        temp=rol(a,5) + f + e + k + w[i] & 0xffffffff
        e=d
        d=c
        c=rol(a,30)
        b=a
        a=temp
      h0 = h0 + a & 0xffffffff
      h1 = h1 + b & 0xffffffff
      h2 = h2 + c & 0xffffffff
      h3 = h3 + d & 0xffffffff
      h4 = h4 + e & 0xffffffff
  return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)  
  


parser=argparse.ArgumentParser()
parser.add_argument('-p','--password',nargs='*',help='<Required> Set flag',required=True)
arg=parser.parse_args()


print(a:=SHA(str(arg.password[0])))

