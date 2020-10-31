print("M   T   W   T   F   S   Su",end="\t")
print( )
for m in range(1,32):
    print( m , end="\t" )
    if m % 7 == 0:
        print( )