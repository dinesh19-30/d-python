ocount=0
ecount=0
for num in range(1, 11):
    if num % 2 != 0:
        ecount = ecount+1
    else :
        ocount = ocount+1
print("odd = ",ocount)
print("even = ",ecount)
