'''
Student name: Luis Zhou
Student ID: 2018100701580033
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

d={'Australia':22.5,'China':36.4,'Malaysia':38.4,'New Zealand':18.2}
print('Australia:'+str(d['Australia']))
print('China:'+str(d['China']))
print('Malaysia:'+str(d['Malaysia']))
print('New Zealand:'+str(d['New Zealand']))
print('Average temperature:{0:.2f}'.format((d['Australia']+d['China']+d['Malaysia']+d['New Zealand'])/4))
print('Maximum temperature:{0:.2f}'.format(max(d.values())))

s=0
for j in d.values():
    if j>=20 and j<=0:
        s=s+1
print('Number of temperatures between 20 and 30: '+str(s))
