# size = int(input("ENter size :"))
# l1 = []
# for i in range(size):
#     x=input()
#     if type(x)==int:
#         l1.append(x)
#     else:
#         pass
# print(l1)

# l = [int(x) for x in l1 if x != ""]
#
# print([x for x in range(l[0], l[-1]) if x not in l])
# s='a+aa+aaa+aaaa'
# x=(input())
# e=s.replace('a',x)
# print(eval(e))
# print(eval(s))
# sum=0
#
# for i in s.split('+'):
#     sum+=sum+int('%s'%i)
#
# print(sum)
# a='2'
# n1=int('%s%s%s'%(a,a,a))
# print(n1)
# print(eval('2+22'))
s='as we said \n in the call'
x='call'
y='note'
z='\ns'
ta=s.maketrans(x,y,z)
re=s.translate(ta)
print(re)
