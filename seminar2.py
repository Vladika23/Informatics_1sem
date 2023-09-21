#task1
# n=int(input())
# a=list()
# for i in range(n-1):
#     a.append(int(input()))
# print(((1+n)//2)*n-sum(a))

# #task2
# n=int(input())
# s=input()
# f=''
# for i in range(0,len(s)-n+1,n):
#     k=s[i:i+n]
#     f+=k[::-1]
# print(f)

#task3
# s=input()
# l=len(s)
# p=False
# m=True
# f=s[0:l//2]
# if f[::-1]==s[(l+1)//2:len(s)]:
#     p=True
# signf='AHIMOTUVWXY18EJSZ3L25'
# signs='AHIMOTUVWXY183L25EJSZ'
# lis=list(s)
# for i in range(len(s)):
#     if lis[i] in signf:
#         lis[i]=signs[signf.index(lis[i])]
#     else:
#         m=False
#         break
# k=''.join(lis)
# if k[::-1]!=s:
#     m=False
# if p==1 and m==1:
#     print(s,'is a mirroed palindome')
# elif p==1 and m==0:
#     print(s,'is a regular palindome')
# elif p==0 and m==1:
#     print(s, 'is a mirroed string')
# elif p==0 and m==0:
#     print(s, 'is not a palindrome')

#task4
# s=input()
# [print(s[i:i+2][::-1],end='') for i in range(0,len(s)-1,2)]
# [print(s[-1]) for i in range(1) if len(s)%2!=0]

# #task5
# # s=list(input())
# # s[1:len(s)]=s[0:len(s)-1]
# # print(s)
# s=input()
# print(s[-1],end='')
# [print(s[i],end='') for i in range(0,len(s)-1)]

#task6
# s=input()
# for i in s:
#     if s.count(i)==1:
#         print(i,end=' ')

#task7
# s=input()
# max=0
# t=''
# for i in s:
#     if s.count(i)>max:
#         max=s.count(i)
#         t=i
# print(t)

#task8
c=int(input())
s=input()
cm=0
cb=0
for i in range(c):
    for j in range(c):
        if int(s[j])<int(s[i]):
            cm+=1
        if int(s[j])>int(s[i]):
            cb+=1
    if cm==cb:
        print(i)
        break
    cm=0
    cb=0

#task9

