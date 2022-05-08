import io
import sys

_INPUT = """\
6
3 4
2 2
3 4
1 3
3 4
3 4
1 10
1 5
8 1
8 1
1 1
1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W=map(int,input().split())
  R,C=map(int,input().split())
  ans=0
  if 1<R: ans+=1
  if R<H: ans+=1
  if 1<C: ans+=1
  if C<W: ans+=1
  print(ans)