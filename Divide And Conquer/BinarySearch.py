# Binary Search on a list of integers

def binarySearch(mylist,start,end,var):
    '''
    Divide sorted list to get mid element as element to find
    '''
    if(start<=end):
        mid=(start+end)//2
        if(var==mylist[mid]):
            return mid
        elif(var>mylist[mid]):
            return binarySearch(mylist,mid+1,end,var)
        elif(var<mylist[mid]):
            return binarySearch(mylist,start,mid-1,var)
    else:
        return -1

def main():
    my_list=[1,2,3,4,5,6,7,8,9,10]
    my_list.sort()
    n=len(my_list)
    to_find=4
    #print(my_list)
    search=binarySearch(my_list,0,n-1,to_find)
    if(search!=-1):
        print(f"{to_find} found at index location {search}")
    else:
        print(f"{to_find} not found in list")

if __name__=="__main__":
    main()
