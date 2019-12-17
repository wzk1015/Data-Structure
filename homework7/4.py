import re
a=input()
ans=None
pat1=r"<a.*></a>"
pat2=r'".*"'
link=""

if (re.search(pat1,a)!=None):
    link=re.search(pat1,a).group()
    ans=re.search(pat2,link).group()
    if ans!=None:
        ans=ans[1:-1]

if ans==None or len(ans)==0:
    print("ValueError")
else: 
    print(ans)