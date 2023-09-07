
def sub(list,sum,num):
 for i in range(0,num):
     CurrentSum= list[i]
     if (CurrentSum == sum):
       print("Sum found at indexes ",i)
       return
     else:
      for j in range(i+1,num):
        CurrentSum += list[j]
        if (CurrentSum ==sum):
                print("Sum Found between indexes",i, "and", j)
                return
 print("We dont have any Subarray")



num = int(input(" enter your list number here"))
list = []
for i in range (num):
  take = int(input())
  list.append(take)

sum = int(input("Enter your sum :"))
sub(list,sum,num)





# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}

# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}







# for i in range(0,n):
 #        currentSum = arr[i]
 #        if(currentSum == sum):
 #            print("Sum found at indexes",i)
 #            return
 #        else:
 #            # Try all subarrays starting with 'i'
 #            for j in range(i+1,n):
 #                currentSum += arr[j]
 #                if(currentSum == sum):
 #                    print("Sum found between indexes",i,"and",j)
 #                    return
 #    print("No Subarray Found")
