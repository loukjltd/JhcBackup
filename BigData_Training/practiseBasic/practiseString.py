str = "2017-05-08 09:12:48 status half-configured passwd:amd64 1:4.2-3.1ubuntu5.2"
year = str[0:4]
month = str[5:7]
day = str[8:10]
hour = str[11:13]
minutes = str[14:16]
seconds = str[17:19]
print(year + '/' + month + '/' + day + '/' + hour + '/' + minutes + '/' + seconds)
