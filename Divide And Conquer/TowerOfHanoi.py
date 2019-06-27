#Tower of Hanoi Problem

def TOH(disk,from_rod,to_rod,aux_rod):
    '''
    Base Condition (Start and Stop condition):
    Move smallest disk to its place. For start to_rod if odd or aux_rod if even. For stop to_rod.
    Iterative Condition:
    Move until largest plate is not on to_rod.
    '''
    if(disk==1):
        print(f"Move disk {disk} from {from_rod} to {to_rod}")
        return
    TOH(disk-1,from_rod,aux_rod,to_rod)
    print(f"Move disk {disk} from {from_rod} to {to_rod}")
    TOH(disk-1,aux_rod,to_rod,from_rod)

def main():
    '''
    Rods defined as A, B, C
    '''
    disk=3
    TOH(disk,'A','C','B')

if __name__=="__main__":
    main()
