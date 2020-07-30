#lets make a picture gussing game
print("Lets begin the game :)  ")
import random as ra
from matplotlib import pyplot as plt
from matplotlib import image as img
import PIL.Image as imgp
from PIL import ImageDraw,ImageFont
import numpy as np
lst1={1:"yuvraj",2:"mercedes",3:"deepika",4:"shahrukh",5:"taj",6:"jeff"}
lst2={1:img.imread(r"C:\Users\Praveen\Desktop\Raju\yuvraj.png"),2:img.imread(r"C:\Users\Praveen\Desktop\Raju\mercedes.png"),
    3:img.imread(r"C:\Users\Praveen\Desktop\Raju\deepika.png"),4:img.imread(r"C:\Users\Praveen\Desktop\Raju\shahrukh.png"),
    5:img.imread(r"C:\Users\Praveen\Desktop\Raju\tajmahal.png"),6:img.imread(r"C:\Users\Praveen\Desktop\Raju\jeff.png")}
i=imgp.open(r"C:\Users\Praveen\Desktop\Raju\tajmahal.png")

while(1):
    img1=ra.randint(1,6)
    print("Identify the picture:")
    plt.imshow(lst2[img1])
    plt.show()
    length=len(lst1[img1])
    chance=length+2
    output=[" "]*len(lst1[img1])
    print(output)
    
    
    
    
    #image output declaration
    
    ans=lst1[img1]
    
    img1=imgp.new("RGB",(1000,100))
    n=1
    for l in range(length):
        img2=imgp.new("RGB",(100,200),color="white")
        posi=(l*100+20*n,20)
        img1.paste(img2,posi)

#        img1.show()
        n+=1
        
    plt.imshow(img1)
    plt.show()
    
    for i in range(20):
            ans1=input()
            pre=1
            m=1
            for j in range(len(ans)):
                if ans1==ans[j]:
                    output.pop(j)
                    output.insert(j,ans1)
                    pre+=1
                    
                    im=imgp.new("RGB",(100,200),color="red")
                    draw=ImageDraw.Draw(im)
                    f=ImageFont.truetype(r'C:\Users\Praveen\Downloads\lemon-jelly-personal-use-font\LemonJellyPersonalUse-dEqR.ttf',90)
                    draw.text((30,1),ans[j],font=f,fill=(225,225,100))
                    
                    
                    posi=(j*100+20*m,20)
                    img1.paste(im,posi)
#                    img1.show()
                    plt.imshow(img1)
                    
                m+=1
            plt.show()
#y
            print(output)
            if pre==1:
                print("alphabet is not present")
            
            if output==list(ans):
                print("correct answer : ",output)
                break    
            if chance==1:
                print("sorry,chance over")
                break
            chance-=1
    plt.show()
    cont=int(input("Press 1 to retry:  "))
    if cont==1:
        pass 
    else:
        print("Game end   :)  ")
        break