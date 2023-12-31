'''
##Linear search 
#searches numsList for the key and iterates 
#Big O - O(N)
def Linear_search(numsList, key):
    for i in numsList: 
        if(i == key):
            print("Found key! - Here it is: " + str(key))


'''

'''
##Binary Search
def Binary_search(numsList, key):
    low = 0
    high = len(numsList) - 1


    while(low <= high):

        mid = (low + high) // 2
        print("this is mid: " + str(mid)) 

        #if key is greater than mid, ignore left half 
        if (numsList[mid] < key):
            low = mid + 1  

        #if key is less than mid, ignore right half
        elif (numsList[mid] > key):
            high = mid - 1
        
        else:
            return mid
    

    return -1 
    
    

'''
'''
##Selection Sort
#Selection Sort
# 2 parts unsorted and sorted. the outer loop iterates through i which is the sorted and j checks the rest of the elements ->
#-> which is the unsorted elements. j finds the smallest element and swaps it with i. 
#for the outer loop len(numbers)-1 is -1 because after i iterates through all elements, the last unsorted element will be in the correct position->
#-> which means we do not need to check the performance. 
def Selection_Sort(numbers): 
    for i in range(len(numbers)-1):

        #Find index of smallest remaining element
        index_smallest = i 
        
        #range - start at i+1 and stop len(numbers)
        for j in range(i+1,len(numbers)):       
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
        
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp

'''
'''
#Insertion Sort takes an input and breaks it into 2 parts. The sorted and unsorted. i is the sorted and j is the unsorted. 
# j is checked against i and if the unsorted part is less than that of i, they are swapped. 

def Insertion_Sort(numbers) :

    for i in range(1, len(numbers)):

        j = i

        while (j > 0 and numbers[j] < numbers[j-1]):
            temp = numbers[j]
            numbers[j] = numbers[j-1]
            numbers[j-1] = temp
            j -= 1
    return numbers

if __name__ == "__main__":
# Call the function to demonstrate their usage
    numbers = [1,2,5,10,8 ]
    print(Insertion_Sort (numbers))
'''
'''
#Shell Sort - using gap values and interleaved lists to sort the array 
def Shell_Sort(numbers, start_index, gap):
    
    for i in range(start_index+gap, len(numbers),gap):

        j = i

        while (j-gap >= start_index and numbers[j] < numbers[j-gap]):
            temp = numbers[j]
            numbers[j] = numbers[j-gap]
            numbers[j-gap] = temp
            j = j-gap
    return numbers
'''
'''
#Quick Sort requires 2 functions (Parition and Quick Sort) unlike the previous Sorting algorithms
# Partition function takes all values lower than the pivot on the left side and ->
# -> all values greater than the pivot
def Partition(numbers, low, high):

    mid = low + (high - low) // 2
    pivot = numbers[mid]

    done = False

    while not done: 

        while numbers[low] < pivot:
            low += 1 
            
        while numbers[high] > pivot:
            high -= 1 
        
        if high <= low:
            done = True
        
        temp = numbers[low]
        numbers[low] = numbers[high]
        numbers[high] = temp
        low += 1
        high -= 1 

    return high
    
def Quick_Sort(numbers, low, high):

    if high <= low:
        return
    
    lowEndIndex = Partition(numbers, low, high) 
    Quick_Sort (numbers,low,lowEndIndex)
    Quick_Sort(numbers,lowEndIndex+1,high)    
'''
#Merge Sort takes 2 functions 
# Merge - merges the 2 halves into the list.
# Merge_Sort - splits the list into 2 halves and recursively sorts the list.

def merge(numbers, low, mid, high):

    #new list 
    merged_size = (high - low) + 1

    merged_list = [0] * merged_size

    #3 pointers, i to point to the left sublist, j to point to the right sublist and k to point to the new list
    i = low
    j = mid + 1
    k = 0

    #this keeps i within the Left sublist and j within the right sublist
    while i <= mid and j <= high:

        if numbers[i] <= numbers[j]: 
            merged_list[k] = numbers[i]
            i += 1

        else:
            merged_list[k] = numbers[j]
            j += 1

        k += 1    

        #if i list is completed and j list has leftover elements, insert the remaining elements into the new list
        if(i > mid):
            while(j <= high):
                merged_list[k] = numbers[j]
                j += 1
                k += 1
        else: 
            while(i <= mid):
                merged_list[k] = numbers[i]
                i += 1
                k += 1 

    for k in range(low, high):
        numbers[k] = merged_list[k]

    for m in range(len(merged_list)):
        numbers[m] = merged_list[m]
    

def merge_sort(numbers, start_index, end_index):
    
    if(start_index < end_index):
        mid = (start_index + end_index) // 2

        #recursively sorts the left half  
        merge_sort(numbers,start_index, mid) 

        #recursively sorts the right half 
        merge_sort(numbers,mid+1, end_index)

        merge(numbers,start_index,mid,end_index)

if __name__ == "__main__":
# Call the function to demonstrate their usage
    numbers = [15,5,24,8,1,3,16,10,20]
    merge_sort(numbers,0,len(numbers)-1)
    print(numbers)
    
    



