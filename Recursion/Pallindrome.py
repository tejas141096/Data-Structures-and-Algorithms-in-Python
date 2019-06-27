# Check if a word is a Pallindrome or not using recursion

def pall(word,st,e):
    '''
    Check if the nth letter from start and end are same or not
    '''
    if(st==e):
        return True
    if(word[st]!=word[e]):
        return False

    if(st<e+1):
        return pall(word,st+1,e-1)
    return True

def isPall(word):
    n=len(word)
    return pall(word,0,n-1)

def main():
    word="hello"
    if(isPall(word)):
        print(f"{word} is a pallindrome")
    else:
        print(f"{word} is not a pallindrome")
    word="nitin"
    if(isPall(word)):
        print(f"{word} is a pallindrome")
    else:
        print(f"{word} is not a pallindrome")

if __name__=="__main__":
    main()
