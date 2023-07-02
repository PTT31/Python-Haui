from decimal import*  #everywhere = "*"

# getcontext(),prec = ??? so chu so sau dau cham
getcontext().prec = 100

f=10/3
print(f)

d = Decimal(10)/Decimal(3)

print(d)
