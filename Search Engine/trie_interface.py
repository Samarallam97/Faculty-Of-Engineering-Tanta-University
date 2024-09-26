
import timeit
from trie import Trie
trie =Trie()



##########################################################################
def invalidInput():
    print("                  ---------------------------                 ")
    print("                         ivalid input ")
    print("                  ---------------------------                 ")
    print("                     program is terminated                 ")
    print("                  ---------------------------\n\n\n                 ")

########################################################################
def autoComplete():
    print("do you want autocomplete for a specific prefix if yes press y, if no press n")
    complete = input()

    if complete == "y":
        print("enter the prefix")
        prefix = input()
        suggestions=trie.suggest(prefix)
        if suggestions:
            print("sugesstions" , suggestions) 
        
        else:
            print("No sugesstions")

        

    elif complete == "n":
        print("              ---------------------------                     ")
        print("              Thanks for using our program                ")
        print("              ---------------------------                     ")

    else:
        invalidInput()
  

############################################################################################
def formMyTrie(words):
    i=0
    for line in words:     
       trie.insert(line.rstrip('\n'),i)
       i+=1
    #    print (line.rstrip('\n') + "  =>  is inserted")
    
    print("                  ---------------------------                     ")
    print("                   Forming The Trie Is Done                        ")
    print("                  ---------------------------                     ")

########################################################################################
def userForming(list):
    
    elapsed_time = timeit.timeit(lambda: formMyTrie(list), number=1)
    print("                  inserion time is :" ,round(elapsed_time, 5),"s")
    print("                  ---------------------------                 ")

###########################################################################################

def isExist(val):
    # print(trie.search(val))
    if trie.search(val) is not None:
        print("              ---------------------------                     ")
        print("             ", val, "is exist at index", trie.search(val))
    else:
        print("              ---------------------------                     ")
        print("                    ", val, "not exist            ")


######################################################################################### 

def userSearch():
    print("do yo want to search for any item? if yes print y, if no print n:")
    wantToSearch=input()
    if wantToSearch =="y":
        print("enter the element you want to search about:")

        searchWord=input()       
        elapsed_time = timeit.timeit(lambda: isExist(searchWord) , number=1)

        print("              ---------------------------                     ")
        print("               search time is :",round(elapsed_time , 5) ,"s")
        print("              ---------------------------                     ")
    

    elif wantToSearch not in ["n","y"]: 
        invalidInput()
 


######################################################################################## console screen
print("------------------------------------------------------")
print("                       Trie")
print("------------------------------------------------------")

print("if you want to form your trie by entering words one by one  press 1 \nif you want to form it using a file press 2")
inputMethod= input()
if inputMethod == "1":
        print("please enter elements separated with space:")
        myList = input() 
        userForming(myList.split()) 
        userSearch()
        autoComplete()
    
    
elif inputMethod=="2":
        print("please enter the file path")
        filePath=input()
        # str=open(filePath,"r")

        try:
           with open(filePath, "r") as file:

            userForming(file)
            userSearch()
            autoComplete()

        except FileNotFoundError:
            print("File not found. Please check the file path.")

else:
        invalidInput()



