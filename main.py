def LongestConsecutive(nums):
    if nums=="":
        return 0
    if len(nums)==1:
        return 1
    d=set(nums)
    largest=0
    for i in d:
        if i-1 not in nums:
            start=i
            count=1
            while start+1 in d:
                start=start+1
                count+=1
            largest=max(largest,count) 

              
    return largest
list1=[1,2,2,3,4,4,5,6]              
print(LongestConsecutive(list1))
list2=[10,5,12,3,55,11]              
print(LongestConsecutive(list2))
list3=[100,4,200,1,3,2,5,6,7]              
print(LongestConsecutive(list3))