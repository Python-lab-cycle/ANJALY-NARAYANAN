print("Print leap year betweeen two given years ")
print("Enter start year")
startYear=int(input())
print("Enter last year")
endYear=int(input())
print("List of years")
for year in range(startYear,endYear):
    if year%4==0:
        print(year)

