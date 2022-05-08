import io
import sys

_INPUT = """\
6
5
1 2 3 4 5
1 2 2 4 3
7
1 1
2 2
2 3
3 3
4 4
4 5
5 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  Q=int(input())
  a=set()
  b=set()
  aa=[]
  bb=[]
  al=[0]
  bl=[0]
  for i in range(N):
    if A[i] not in a:
      aa.append(A[i])
      a.add(A[i])
      al.append(al[-1]+1)
    else: al.append(al[-1])
    if B[i] not in b:
      bb.append(B[i])
      b.add(B[i])
      bl.append(bl[-1]+1)
    else: bl.append(bl[-1])
  az=set()
  bz=set()
  aaz=set()
  bbz=set()
  z=[1]
  for i in range(min(len(aa),len(bb))):
    if aa[i] not in aaz and bb[i] not in bbz:
      aaz.add(aa[i])
      bbz.add(bb[i])
      if aa[i] in bz: bz.remove(aa[i])
      else: az.add(aa[i])
      if bb[i] in az: az.remove(bb[i])
      else: bz.add(bb[i])
    elif aa[i] not in aaz and bb[i] in bbz:
      aaz.add(aa[i])
      if aa[i] in bz: bz.remove(aa[i])
      else: az.add(aa[i])
    elif aa[i] in aaz and bb[i] not in bbz:
      bbz.add(bb[i])
      if bb[i] in az: az.remove(bb[i])
      else: bz.add(bb[i])
    if len(az)==0 and len(bz)==0: z.append(1)
    else: z.append(0)
  for i in range(Q):
    x,y=map(int,input().split())
    if al[x]==bl[y] and z[al[x]]==1: print('Yes')
    else: print('No')