import io
import sys

_INPUT = """\
6
5 5
1
2
3
4
5
7 7
7
7
7
7
7
7
7
10 6
1
5
2
9
6
6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,Q=map(int,input().split())
  pos=list(range(N))
  ans=list(range(N))
  for _ in range(Q):
    x=int(input())-1
    if pos[x]==N-1: p,q=pos[x],pos[x]-1
    else: p,q=pos[x],pos[x]+1
    pos[ans[q]],pos[ans[p]],ans[p],ans[q]=pos[ans[p]],pos[ans[q]],ans[q],ans[p]
  print(*[ans[i]+1 for i in range(N)])