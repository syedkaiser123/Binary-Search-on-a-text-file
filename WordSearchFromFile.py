#lineList = [line. rstrip('\n') for line in open("abc.txt")]

f = open("abc.txt")
x = f.read()

wordList = []
FinalList = []
for word in x:
    if word != " " and word != '\n': 
        
        wordList.append(word)
        

    elif word == " " or word == '\n':
        result = ''.join(map(str,wordList))
        
        FinalList.append(result)
        wordList.clear()

FinalList = sorted(FinalList)        
print(FinalList) 

def search(FinalList,key):
    
    n = len(FinalList)
    
    start = 0
    end = n-1
    value = int(FinalList.index(key))
    
    
    
    while(start<=end):
        
        mid = (start+end)//2
        
        if key == FinalList[mid]:
            print("key found at {}".format(mid))
            break
        elif value > mid:
            start = mid+1
            
        else:
            end = mid-1

key = input("enter the word to be searched in the given text file :")            
search(FinalList,key)
