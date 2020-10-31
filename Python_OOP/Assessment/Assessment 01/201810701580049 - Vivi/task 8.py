#Task8
"""
id : 201810701580049
class : Net182
name : vivi
"""

dic = {'Australia':22.5, 'China':36.4, 'Malaysia':38.4, 'New Zealand':18.2}
tsum = 0
tcount = len(dic)
maxt = 0
medtc = 0
for key in dic:
    t = dic[key]
    print(key+': '+str(t))
    tsum += t
    if t > maxt:
        maxt = t
    if t >= 20 and t <=30:
        medtc +=1
print()
print('Average temperature: '+str('%.2f' %(tsum / tcount)))
print('Maximum temperature: '+str('%.2f' %maxt))
print('Number of temperatures between 20 and 30: '+str(medtc))
