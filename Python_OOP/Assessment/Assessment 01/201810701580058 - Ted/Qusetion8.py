# Qusetion8
'''
Student Name: Ted
ID: 201810701580058
Class: Net 182
'''

dic={}
dic['Australia']=22.5
dic['China']=36.4
dic['Malaysia']=38.4
dic['New Zealand']=18.2
a=[]
b=0
sum=0
for i in dic.values():
    sum+=i
for f in dic.values():
    a.append(f)
for i in a:
    if i>=20 and i<=30:
        b+=1
for i in dic:
    print(i+' : '+str(dic[i]))
print()
print('Average temperature: '+str('%.2f' % (sum/len(a))))
print('Maximum temperature: '+str('%.2f' % (max(dic.values()))))
print('Number of temperatures between 20 and 30: '+str(b))