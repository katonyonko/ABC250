import io
import sys

_INPUT = """\
6
5
3 0
2 3
-1 3
-3 1
-1 -1
4
400000000 400000000
-400000000 400000000
-400000000 -400000000
400000000 -400000000
6
-816 222
-801 -757
-165 -411
733 131
835 711
-374 979
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
    N=int(input())
    P=[list(map(int,input().split())) for _ in range(N)]
    P=[(P[i][0]-P[0][0],P[i][1]-P[0][1]) for i in range(N)]
    A=0
    for i in range(N-2): A+=abs(P[i+1][0]*P[i+2][1]-P[i+2][0]*P[i+1][1])
    ans=10**100
    tmp=0
    now=1
    for i in range(N):
        while tmp<A:
            ans=min(ans,abs(A-tmp))
            tmp+=4*abs((P[now][0]-P[i][0])*(P[(now+1)%N][1]-P[i][1])-(P[(now+1)%N][0]-P[i][0])*(P[now][1]-P[i][1]))
            now=(now+1)%N
        ans=min(ans,abs(A-tmp))
        tmp-=4*abs((P[(i+1)%N][0]-P[i][0])*(P[now][1]-P[i][1])-(P[now][0]-P[i][0])*(P[(i+1)%N][1]-P[i][1]))
    print(ans)