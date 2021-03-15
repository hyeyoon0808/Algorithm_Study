import sys

input=sys.stdin.readline
case=0
day = {}

while(True):
    l, p, v = map(int, input().split())
    if l+p+v == 0:
        break
    else:
        case+=1
        #c=(v//p)*l+(v%p)
        c=(v//p)*l
        c+=min((v%p), l)
        day[case]=c

for key in day:
    val = day[key]
    print("Case %d: %d" % (key,val))