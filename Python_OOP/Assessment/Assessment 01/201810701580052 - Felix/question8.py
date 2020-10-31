d ={'Malaysia':38.4 ,'China':36.4,'Australia':22.5,'New Zealand':18.2}
l = []
l2 = []
for i in d:
    print(i + ';' + str(d[i]))
    l.append(d[i])

for j in l:
    if 20<=j<=30:
        l2 .append(j)


print('Average temperature: ',('%.2f'%(sum(l)/len(l))))
print('Maximum temperature: ',('%.2f'%(max(l))))
print('Number of temperatures between 20 and 30: ',len(l2))

