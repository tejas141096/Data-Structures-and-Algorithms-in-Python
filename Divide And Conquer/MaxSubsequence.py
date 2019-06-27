# Max Subarray Sum

def main():
    mylist=[-2, -3, 4, -1, -2, 1, 5, -3]
    max_sum=0
    max_sum_till_now=0
    for i in range(len(mylist)):
        max_sum_till_now+=mylist[i]
        if(max_sum_till_now>max_sum):
            max_sum=max_sum_till_now
        if(max_sum_till_now<0):
            max_sum_till_now=0

    if(max_sum<=0):
        max_sum=max(mylist)
    print(f"Max sum of subarray is {max_sum}")

if __name__=="__main__":
    main()
