# main.py

from utilsPackage.utils import *
# Call the function and store what it returns 
#  in a variable called data
if __name__ =="__main__":
    data = read_CSV_file()
    print("# of rows in dataset:", len (data))
    # print the first and last row of data
    print(data[0])
    print(data[-1])
    # I want a list comprehesion expression
    # to ull out all the Collison type into a set
    #Modidy this expression to exclude the blank collision type 
    collisionTypes = {myData[6] for myData in data}
    print("# of collision type:", len(collisionTypes))
    print(collisionTypes)
    
    
    

   

    



