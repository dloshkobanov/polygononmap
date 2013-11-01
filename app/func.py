#-------------------------------------------------------------------------------
# Name:        func.py
# Purpose:
#
# Author:      dloshkobanov
#
# Created:     31.10.2013
# Copyright:   (c) dloshkobanov 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Алгоритм Грэхэма
def grahamscan(A):
    n = len(A) # число точек
    P = list(range(n)) # список номеров точек
    for i in range(1,n):
      if A[P[i]][0]<A[P[0]][0]: # если P[i]-ая точка лежит левее P[0]-ой точки
        P[i], P[0] = P[0], P[i] # меняем местами номера этих точек
    for i in range(2,n): # сортировка вставкой
      j = i
      while j>1 and (rotate(A[P[0]],A[P[j-1]],A[P[j]])<0):
        P[j], P[j-1] = P[j-1], P[j]
        j -= 1
    S = [P[0],P[1]] # создаем стек
    for i in range(2,n):
      while rotate(A[S[-2]],A[S[-1]],A[P[i]])<0:
        del S[-1] # pop(S)
      S.append(P[i]) # push(S,P[i])
    return S

#Определение центра тяжести многоугольника
def centeroffravity(A):
    x = 0
    y = 0
    for i in range(len(A)):
      x = x + A[i][0]
      y = y + A[i][1]
    return [(x/len(A), y/len(A))]

def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

"""
lstPoint = [(1,1),(1,-1),(0,0),(-1,1),(-1,-1)]# исходный список
numPolygon = grahamscan(lstPoint)# номера точек многоугольника
numInternal = set(range(len(lstPoint))) - set(numPolygon)# номера внутренних точек
lstPolygon = [lstPoint[i] for i in numPolygon]# список точек многоугольника
lstInternal = [lstPoint[i] for i in numInternal]# список внутренних точек
centerPoint= centeroffravity(lstPolygon)# центер тяжести многоугольника


print(lstPoint)
print(numPolygon)
print(lstPolygon)
print(numInternal)
print(lstInternal)
print(centerPoint)
"""