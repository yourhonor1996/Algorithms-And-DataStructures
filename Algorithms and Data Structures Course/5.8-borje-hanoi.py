#A variable for count the step of transmission of rings
step=1
def hanoi(n,src,dst,help):
    global step
    #Base condition !!there is only one ring!!
    if n==1:
        print(step,src,dst)
        step+=1
    else:
        #Move n-1 rings from A to B
        hanoi(n-1,src,help,dst)
        #Move the remain ring from A to C 
        print(step,src,dst)
        step+=1
        #Move n-1 rings from B to C
        hanoi(n-1,help,dst,src)

n=int(input())
hanoi(n,'A','B','C')