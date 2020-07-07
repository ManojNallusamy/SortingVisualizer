import pygame
import random
import time
pygame.font.init()
startTime = time.time()
# Total window
screen=pygame.display.set_mode((900,650))

# Title and Icon 
pygame.display.set_caption("SORTING VISUALISER")
#Place any png file you wanted in same folder as the source code
#and mention it below or comment below two lines to avoid error
img = pygame.image.load('sorticon.png')
pygame.display.set_icon(img)

# a Boolean variable to run the program in while loop
run = True

# Window size
width=900
length=600
array =[0]*151
arr_clr=[(0,204,102)]*151
clr_ind=0
clr=[(0,204,102),(255,0,0),(0, 0, 153),(255, 102, 0)]
fnt =pygame.font.SysFont("comicsans", 30)
fnt1=pygame.font.SysFont("comicsans", 20)
#Generate new Array
def generate_arr():
    for i in range(1,151):
        arr_clr[i]=clr[0]
        array[i]=random.randrange(1,100)
generate_arr() 
def refill(algo_selected):
    screen.fill((255,255,255))
    draw(algo_selected)
    pygame.display.update()
    pygame.time.delay(60)


#Sorting Algo:Merge sort
def mergesort(array,l,r):
    mid=(l+r)//2
    if l<r:
        mergesort(array,l,mid)
        mergesort(array,mid+1,r)
        merge(array,l,mid,mid+1,r)
def merge(array,x1,y1,x2,y2):
    i=x1
    j=x2
    temp=[]
    pygame.event.pump() 
    while i<=y1 and j<=y2:
        arr_clr[i]=clr[1]
        arr_clr[j]=clr[1]
        refill(1)
        arr_clr[i]=clr[0]
        arr_clr[j]=clr[0]
        if array[i]<array[j]:
                temp.append(array[i])
                i+=1
        else:
                temp.append(array[j])
                j+=1
    while i<=y1:
        arr_clr[i]=clr[1]
        refill(1)
        arr_clr[i]=clr[0]
        temp.append(array[i])
        i+=1
    while j<=y2:
        arr_clr[j]=clr[1]
        refill(1)
        arr_clr[j]=clr[0]
        temp.append(array[j])
        j+=1
    j=0       
    for i in range(x1,y2+1):  
        pygame.event.pump()  
        array[i]=temp[j]
        j+=1
        arr_clr[i]=clr[2]
        refill(1)
        if y2-x1==len(array)-2:
            arr_clr[i]=clr[3]
        else:    
            arr_clr[i]=clr[0]


#Sorting Algo:Quick sort
def quicksort(array,l,r):
    if l<r:
        pi = partition(array,l,r)
        quicksort(array,l,pi-1)
        refill(2)
        for i in range(0,pi+1):
            arr_clr[i]=clr[3]
        quicksort(array,pi+1,r)
def partition(array,low,high):
    pygame.event.pump() 
    pivot=array[high]
    arr_clr[high]=clr[2]
    i=low-1
    for j in range(low,high):
        arr_clr[j]=clr[1]
        refill(2)
        arr_clr[high]=clr[2]
        arr_clr[j]=clr[0]
        arr_clr[i]=clr[0]
        if array[j]<pivot:
            i=i+1
            arr_clr[i]=clr[1]
            array[i],array[j]=array[j],array[i]
    refill(2)
    arr_clr[i]=clr[0]
    arr_clr[high]=clr[0]
    array[i+1],array[high] = array[high],array[i+1] 
    
    return ( i+1 )


# Sorting Algorithm: Insertion sort
def insertionSort(array):

    for i in range(1,len(array)):

        pygame.event.pump() 

        # Refill window
        refill(3)
        key = array[i]
        arr_clr[i]=clr[2]
        j=i-1
        while j>=0 and key<array[j]:
            arr_clr[j]=clr[2]
            array[j+1]=array[j]
            refill(3)
            arr_clr[j]=clr[3]
            j=j-1
        array[j+1]=key   
        refill(3)
        arr_clr[i]=clr[0]


# Sorting Algo: HeapSort
def heapsort(array):
    n=len(array)
    for i in range(n//2-1,-1,-1):
        pygame.event.pump()
        heapify(array,i,n)
    for i in range(n-1,0,-1):
        array[i],array[0]=array[0],array[i]
        arr_clr[i]=clr[1]
        refill(4)
        heapify(array,0,i)

def heapify(array,root,size):
    left=root*2+1
    right=root*2+2
    largest=root
    if left<size and array[left]>array[largest]:
        largest=left
    if right<size and array[right]>array[largest]:
        largest=right
    if largest!=root:
        arr_clr[largest]=clr[2]
        arr_clr[root]=clr[2]
        array[largest],array[root]=array[root],array[largest]
        refill(4)
        arr_clr[largest]=clr[0]
        arr_clr[root]=clr[0]
        heapify(array,largest,size)        

#Draw the array values
def draw(algo_selected):
    #Text should be rendered
    txt=fnt.render("SORT : PRESS 'ENTER'",1,(0,0,0))
    #Position where text is placed
    screen.blit(txt,(20,20))
    txt1=fnt.render("NEW ARRAY : PRESS 'R'",1,(0,0,0))
    screen.blit(txt1,(20,40))
    algorithms=["MERGE SORT","QUICK SORT","INSERTION SORT","HEAP SORT"]
    txt2=fnt1.render("ALGORITHM SELECTED: "+algorithms[algo_selected-1],1,(0,0,0))
    screen.blit(txt2,(600,60))
    text3=fnt1.render("Running Time(sec): "+str(int(time.time() - startTime)),1,(0,0,0))
    screen.blit(text3,(600,20))
    text4=fnt1.render("SELECT ALGORITHM:",1,(0,0,0))
    screen.blit(text4,(300,10))
    text4=fnt1.render("MergeSort    press 1 (Selected default)",1,(0,0,0))
    screen.blit(text4,(300,30))
    text4=fnt1.render("QuickSort     press 2",1,(0,0,0))
    screen.blit(text4,(300,45))
    text4=fnt1.render("InsertionSort press 3",1,(0,0,0))
    screen.blit(text4,(300,60))
    text4=fnt1.render("HeapSort      press 4",1,(0,0,0))
    screen.blit(text4,(300,75))
    element_width=(width-150)//150
    boundry_arr=900/150
    boundry_grp=550/100
    pygame.draw.line(screen,(0,0,0),(0,95),(900,95),6)
    #for i in range(1,100):
    #    pygame.draw.line(screen,(224,224,224),(0,boundry_grp*i+100),(900,boundry_grp*i+100),1)
    
    #Drawing the array values as lines
    for  i in range(1,151):
        pygame.draw.line(screen,arr_clr[i],(boundry_arr*i-3,100),(boundry_arr*i-3,array[i]*boundry_grp+100),element_width)
#Program should be run continuously to keep the window open
algo_selected=1
while run:
    #background
    screen.fill((255,255,255))
    
    #Event handler stores all event 
    for event in pygame.event.get():
        #If we click Close button in window
        if event.type == pygame.QUIT:
            run =False
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_r:
                generate_arr() 
            if event.key== pygame.K_1:
                algo_selected=1
            if event.key==pygame.K_2:
                algo_selected=2
            if event.key==pygame.K_3:
                algo_selected=3
            if event.key==pygame.K_4:
                algo_selected=4
            if event.key==pygame.K_RETURN:
                if algo_selected == 1:
                    mergesort(array,0,len(array)-1)
                elif algo_selected ==2:
                    quicksort(array,0,len(array)-1)
                elif algo_selected == 3:
                    insertionSort(array)
                else:
                    heapsort(array)       
    draw(algo_selected)
    pygame.display.update()
   
pygame.quit()