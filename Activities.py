def activity(list):
    list.sort(key=lambda x:x[-1]) # the 0th key is the activity ID, 1st is the start time and 2nd is the end time
    finallist=[]
    finallist.append(list[0]) #so initially the final list has the activity that ends first
    print(list)
    for i in list:
       #consider the end time i.e. i[2]
       if i[1]>=finallist[-1][2]: #only consider those that START AFTER the most recent one in the finallist has ENDED
           finallist.append(i)
    return(len(finallist))

activities=[int(x) for x in input().split()]
starttimes=[int(x) for x in input().split()]
endtimes=[int(x) for x in input().split()]
input=[]
if len(activities)==len(starttimes)==len(endtimes):
    for i in range(len(activities)):
        input.append([activities[i],starttimes[i],endtimes[i]])
#print(input)
print(activity(input))
#print([activities,starttimes,endtimes])
''' PLEASE INPUT IN 24-HOUR FORMAT'''
