# GCD of 2 numbers

def GCD(a,b):
    '''
    Using Euclidean method to find GCD
    a,b=b,a%b until b is 0 and return a
    '''
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

# Main function
def main():
    a=98
    b=56
    ans=GCD(a,b)
    print(f"The GCD of {a} and {b} is {ans}")

if __name__=="__main__":
    main()
