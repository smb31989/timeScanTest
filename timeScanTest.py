import time

count5sec = 0
count30sec = 0
def getDiff1():
    print('diff1 5 second')

def changmining():
    print('Chang mining 30 second')

while True:
    
    if count5sec == 5 :
        getDiff1()
        #reset 
        count5sec = 0

    if count30sec == 30 :
        changmining()
        #reset 
        count30sec = 0
        
    #delay (1 second)
    time.sleep(1)
    
    count5sec = count5sec + 1
    count30sec = count30sec + 1 
