#!/usr/bin/python3 -u

import random
from Crypto.Util.number import *
import gmpy2

a = 0xe64a5f84e2762be5
chunk_size = 64

def gen_prime(bits):
  s = random.getrandbits(chunk_size)

  while True:
    s |= 0xc000000000000001
    p = 0
    for _ in range(bits // chunk_size):
      p = (p << chunk_size) + s
      s = a * s % 2**chunk_size
    if gmpy2.is_prime(p):
      return p

#n = gen_prime(1024) * gen_prime(1024)
e = 65537
#flag = open("output.txt", "rb").read()
#print('n =', hex(n))
#print('e =', hex(e))
#print('c =', hex(pow(bytes_to_long(flag), e, n)))
#remainder=int(0x6a12d56e26e460f456102c83c68b5cf355b2e57d5b176b32658d07619ce8e542d927bbea12fb8f90d7a1922fe68077af0f3794bfd26e7d560031c7c9238198685ad9ef1ac1966da39936b33c7bb00bdb13bec27b23f87028e99fdea0fbee4df721fd487d491e9d3087e986a79106f9d6f5431522270200c5d545d19df446dee6baa3051be6332ad7e4e6f44260b1594ec8a588c0450bcc8f23abb0121bcabf7551fd0ec11cd61c55ea89ae5d9bcc91f46b39d84f808562a42bb87a8854373b234e71fe6688021672c271c22aad0887304f7dd2b5f77136271a571591c48f438e6f1c08ed65d0088da562e0d8ae2dadd1234e72a40141429f5746d2d41452d916)
#print("n")
#print(int(0xab802dca026b18251449baece42ba2162bf1f8f5dda60da5f8baef3e5dd49d155c1701a21c2bd5dfee142fd3a240f429878c8d4402f5c4c7f4bc630c74a4d263db3674669a18c9a7f5018c2f32cb4732acf448c95de86fcd6f312287cebff378125f12458932722ca2f1a891f319ec672da65ea03d0e74e7b601a04435598e2994423362ec605ef5968456970cb367f6b6e55f9d713d82f89aca0b633e7643ddb0ec263dc29f0946cfc28ccbf8e65c2da1b67b18a3fbc8cee3305a25841dfa31990f9aab219c85a2149e51dff2ab7e0989a50d988ca9ccdce34892eb27686fa985f96061620e6902e42bdd00d2768b14a9eb39b3feee51e80273d3d4255f6b19))
#fe=remainder+(1*n)
#n
#21649957502641796205288656579513462059525691658468568351723034242279652352259066090435480799497299539096422703581551457678818699482055282001795442572247785213734483148891551039454836799079383725334417512508010058707173681984531865513047286412531957295552927735398160287952733301329579177902519164858200117212832126402051458410402534801436851065903131818388962672928832910725739249686424648157036116458049738155378527444780584371588546032681756986546703781249424542690906952706864717086511696295723146015745090637890152280757145107712599796769043622341929904861904987001742066207076333587428952432020191737227302103833
#factor
#140189898764964771014395337052217942922030714831246663724040348430876610053872119346252717513589034099650476024286393279227520833268967590616316891177774642257051100333899647986001046974520758813471028484403531176483903462820015495157097336019754097785418837408137377591594663770969883538220048263000887622211
#f=pow(fe,pow(e,-1))

#print(long_to_bytes(f))
#primefile = open("primes","r")
#for _ in range(1000):
#  prime = gen_prime(1024)
#  write = str( prime) + "\n"
#  primefile.write(write)

n=21649957502641796205288656579513462059525691658468568351723034242279652352259066090435480799497299539096422703581551457678818699482055282001795442572247785213734483148891551039454836799079383725334417512508010058707173681984531865513047286412531957295552927735398160287952733301329579177902519164858200117212832126402051458410402534801436851065903131818388962672928832910725739249686424648157036116458049738155378527444780584371588546032681756986546703781249424542690906952706864717086511696295723146015745090637890152280757145107712599796769043622341929904861904987001742066207076333587428952432020191737227302103833

#for i in range(10000):
#  prime=gen_prime(1024)
#  if(n%prime==0):
#    print(prime)
for i in range(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
  if gmpy2.is_prime(i):
    if(n%i==0):
      print(i)
      break
  else:
    if(i%100000000000000000==0):
      print("progress= ",i)
    continue
