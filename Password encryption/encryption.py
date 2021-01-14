import string
import numpy as np
import argparse

char=list(string.ascii_lowercase)+list(string.ascii_uppercase)+list('_')+list(map(str,range(10)))
token=list(range(len(char)))

def encryption(raw):
    raw=list(raw)
    K=int(np.random.randn()%len(char))
    encrypted=[]
    for i in raw:
        no=char.index(i)
        encrypted.append(token[(no+K)%len(char)])
    encrypted.append(K)
    return encrypted

def decryption(encrypted):
    K=encrypted.pop()
    decrypted=[]
    for i in encrypted:
        no=token.index(i)
        decrypted.append(char[(no-K)%len(char)])
    return decrypted

parser=argparse.ArgumentParser()
parser.add_argument('-p','--password',nargs='*',help='<Required> Set flag',required=True)
arg=parser.parse_args()


print(a:=encryption(str(arg.password[0])))
print(decryption(a))
