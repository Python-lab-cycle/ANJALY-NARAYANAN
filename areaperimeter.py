from areaperimeterfunction import *
while[True]:
    print("\n*****Menu*****")
    print("\n1.Circle")
    print("\n2.Cuboid")
    print("\n3.sphere")
    print("******************")
    choice=int(input("enter choice:"))
    if(choice==1):
        r1=int(input("Enter radius:"))
        area=circlearea(r1)
        print("\nArea is:"+str(area))
        perimeter=circleperimeter(r1)
        print("\nperimeter is:"+str(perimeter))
    elif(choice==2):
        r2=int(input("Enter radius:"))
        area=spherearea(r2)
        print("\nArea is:"+str(area))
        perimeter=sphereperimeter(r2)
        print("\nperimeter is:"+str(perimeter))
    elif(choice==3):
        l1=int(input("Enter the length:"))
        w1=int(input("Enter the width:"))
        h1=int(input("Enter the height:"))
        area=cuboidarea(l1,w1,h1)
        print("\nArea is:"+str(area))
        perimeter=sphereperimeter(r2)
        print("\nperimeter is:"+str(perimeter))
    elif(choice==4):    
            quit(0)
    else:
                print("Give a valid choice")
            
