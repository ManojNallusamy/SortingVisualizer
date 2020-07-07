# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:31:41 2019

@author: admin
"""

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
        while i<=y1 and j<=y2:
                if array[i]<array[j]:
                        temp.append(array[i])
                        i+=1
                else:
                        temp.append(array[j])
                        j+=1
        while i<=y1:
                temp.append(array[i])
                i+=1
        while j<=y2:
                temp.append(array[j])
                j+=1
        array[x1:y2+1]=temp                

arr=[5,4,3,2,1]
mergesort(arr,0,len(arr)-1)
print(arr)