N=int(input())
for i in range(N):
  says=input()
  ln=len(says)
  if("Simon says" in says):
    print(says[10:])
