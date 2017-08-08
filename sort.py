print list
listLen=len(list)-1
for i in range(len(list)):
    for j in range(listLen-i):
        if(list[j]>list[j+1]):
            tmp  = list[j]
            list[j]=list[j+1]
            list[j+1]=tmp
print list
