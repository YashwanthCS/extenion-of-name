filename = input("Input the Filename: ")
f_extns = filename.split(".")
if f_extns[-1]=='py':
    print ("The extension of the file is : python" )
elif f_extns[-1]=='cpp':
    print ("The extension of the file is : C++" )    
elif f_extns[-1]=='py':
    print ("The extension of the file is :Python " )
else :
    print("enter the extention")
