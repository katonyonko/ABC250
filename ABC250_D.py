import io
import sys

_INPUT = """\
6
250
1
123456789012345
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  from bisect import bisect_right
  def Eratosthenes(n):
    prime=[]
    furui=list(range(2,n+1))
    while furui[0]<math.sqrt(n):
      prime.append(furui[0])
      furui=[i for i in furui if i%furui[0]!=0]
    return prime+furui
  N=int(input())
  prime=Eratosthenes(10**6+1)
  ans=0
  for i in range(len(prime)):
    q=prime[i]
    ans+=min(bisect_right(prime,N//(q**3)),i)
  print(ans)