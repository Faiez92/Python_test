chaine = input("Please give me a string ",)

def my_function(ch):
    
    print (chaine)
    FinalList = ''
    minlist, majlist= ([] for i in range(2))
    
    for car in chaine:
        minlist.append(ord(car))
   
    for j in minlist:
        if 64 < j < 91 or j==32 or 47<j<58:
            majlist.append(j)
        else:
            majlist.append(j-32)
    
    for l in majlist:
        FinalList += chr(l)
    print (FinalList)
  
my_function(chaine)

