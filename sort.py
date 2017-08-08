list = [2,5,20,3,5,16,63,55]
print list
listLen=len(list)-1
for i in range(10):
    for j in range(listLen-i):
        if(list[j]>list[j+1]):
            tmp  = list[j]
            list[j]=list[j+1]
            list[j+1]=tmp
print list
