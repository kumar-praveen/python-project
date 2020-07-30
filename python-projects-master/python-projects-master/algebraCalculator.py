ex=input('Enter the expression\n')

def expression(ex):
    p=[]
    j=0
    for i in ex:
        p.insert(j,i)
        j+=1
    return(p)

def assigning(p):
    lst=[]
    i=0
    while i<len(p):
        j=i+1
        if (p[i].isalpha())==True:
            var=input('enter '+ex[i]+'\n')
            while j<len(p):
                if p[j]==p[i]:
                    p[j]=var
                j+=1
            lst.append(var)
        else:
            lst.append(p[i])
        i+=1
#    m=calculation(lst)
    return lst




def bodmas(lst):
    
    i=0
    while i<len(lst):
        if lst[i]=='^':
            lst[i-1]=str(pow(float(lst[i-1]),float(lst[i+1])))
            lst.pop(i)
            lst.pop(i)
            i-=1
        i+=1
    i=0
    while i<len(lst):
        if lst[i]=='/':
            lst[i-1]=str(float(lst[i-1])/float(lst[i+1]))
            lst.pop(i)
            lst.pop(i)
            i-=1
        i+=1
    i=0
    while i<len(lst):
        if lst[i]=='*':
            lst[i-1]=str(float(lst[i-1])*float(lst[i+1]))
            lst.pop(i)
            lst.pop(i)
            i-=1
        i+=1
    i=0
    while i<len(lst):
        if lst[i]=='+':
            lst[i-1]=str(float(lst[i-1])+float(lst[i+1]))
            lst.pop(i)
            lst.pop(i)
            i-=1
        i+=1
    i=0
    while i<len(lst):
        if lst[i]=='-':
            lst[i-1]=str(float(lst[i-1])-float(lst[i+1]))
            lst.pop(i)
            lst.pop(i)
            i-=1
        i+=1
        
        
        
    return(lst)
    
    

        
#                                                  praveen make changes in bracket defination   
def brackets(stack):
    stack1=[]
    while len(stack):
        stack1.append(stack[len(stack)-1])
        print(stack.pop())
        if stack1[len(stack1)-1]=='(':
           stack2=[] 
           print(stack1)
           i=len(stack1)
           for j in range(len(stack1)):
                stack2.append(stack1[i-2])
                stack1.pop()
                if stack1[i-3]==')':
                    break
                i-=1
           for j in range(2):
               stack1.pop()
           
#           stack2=list(reversed(stack2))
           print(stack2)
           calci=bodmas(stack2)
           stack1.append(calci[0])
           print(stack1)
           
        if stack1[len(stack1)-2]=='^':
            if stack1[0]==None:
                pass
            else:
                m=pow(float(stack1[len(stack1)-1]),float(stack1[len(stack1)-3]))
                for i in range(3):
                    stack1.pop()
                stack1.append(m)
            
    print(stack1)
    return bodmas(stack1)
    
                
    
    



m=int(input('How many values you want\n'))
i=1
while i<=m:
    lst=expression(ex)
    k=assigning(lst)
    print(k)
    print("And your answer is :  ",brackets(k))
    i+=1


    
    
    
    
    
    
    
    