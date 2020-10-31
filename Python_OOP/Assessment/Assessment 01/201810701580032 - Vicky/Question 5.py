#Question 5
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

a= int(input('How many sensors are currently collecting data ?:'))
t_list=[]
for i in range(1,a+1):
     a=float(input('Enter temperature '+str(i)+':'))
     t_list.append(a)
print('Average temperature: '+str(sum(t_list) % a))

s=0
for j in t_list:
    if j>=10 and j<=20:
        s=s+1
print('Maximum temperature: '+str(max(t_list)))
print('Number of temperatures between 10 and 20: '+str(s))