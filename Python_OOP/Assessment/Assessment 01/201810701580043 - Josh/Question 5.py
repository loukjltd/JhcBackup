#Question 5
#Josh net182 201810701580043

tcount = int(input('How many sensors are currently collecting data?: '))
tlist = []
maxt = -273
medtc = 0
for i in range(1,tcount+1):
    t = float(input('Enter temperature '+str(i)+': '))
    tlist.append(t)
    if t > maxt:
        maxt = t
    if t >= 10 and t <=20:
        medtc +=1
print('Average temperature: '+str('%.2f' %(sum(tlist) / tcount)))
print('Maximum temperature: '+str('%.2f' %maxt))
print('Number of temperatures between 20 and 30: '+str(medtc))