import pandas as pds
requestDouban = pds.read_csv('douban_movie_comments.csv', usecols=[1, 3, 6], nrows=10)
print(requestDouban)
