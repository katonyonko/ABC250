import io
import sys

_INPUT = """\
6
4 3 2
5 1 5
4 4 1
1 4 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,A,B=map(int,input().split())
  for i in range(A*N):
    print(*['.' if j//B%2==i//A%2 else '#' for j in range(B*N)],sep='')