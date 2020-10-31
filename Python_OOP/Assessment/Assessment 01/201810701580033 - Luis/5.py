'''
Student name: Luis Zhou
Student ID: 2018100701580033
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
r = int(input('How many sensors are currently collecting data ?:'))
t_list=[]
for i in range(1,r+1):
     a=float(input('Enter temperature '+str(i)+':'))
     t_list.append(a)
print('Average temperature: '+str(sum(t_list)%r))
s=0
for j in t_list:
    if j>=10 and j<=20:
        s=s+1
print('Maximum temperature: '+str(max(t_list)))
print('Number of temperatures between 10 and 20: '+str(s))

