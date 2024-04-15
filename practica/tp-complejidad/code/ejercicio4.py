"""
Estrategia
Para implementar un algoritmo que ordene una lista de elementos segun el criterio especifico, podemos segir los sigirntes pasos
1-Encontrar el elemento del medio para eso vamos a usar el QuickSelect que dado una posicion k nos dara el elemento de esa pocicion
si fuese estar ordenada. 
2-Una vez encontrada el elemento del medio por QuickSelect tendemos a la derecha de la pocicion k los elementos menores al valor
y a la derecha los elementos mayores al valor
3-Dividiremos la sub lista izquierda y derecha del valor central a la mitad y colocaremos a la derecha la mitad mayor y la mitad menor y
hacemos lo mismo a la derecha del valor
"""

def QuickSelect(lst,k):
    """
    Encuentra el k-esimo elemento mas pequeño en la lista 'lst' usando el 
metodo QuickSelect
    """
    if len(lst) == 1:
        return lst[0]
    lst[len(lst)-1],lst[k]=lst[k],lst[len(lst)-1]
    pos = partition(lst, 0, len(lst)-1)
    if k == pos:
        return lst[pos]
    elif k < pos:
        return QuickSelect(lst[:pos], k)
    else:
        return QuickSelect(lst[pos + 1:], k - pos - 1)

def partition(lst,left,right):
    """
    Esta funcion toma el ultimo elemento como pivote, coloca el elemento 
pivote en su posicion correcta en la lista ordenada,
    y coloca todos los elementos menores (menores que el pivote) a la 
izquierda del pivote y todos los elementos mayores a la derecha del 
pivote
    """
    pivot = lst[right]
    i = left
    for j in range(left,right):
        if lst[j] < pivot:
            lst[i],lst[j]=lst[j],lst[i]
            i=i+1
    lst[i],lst[right]=lst[right],lst[i]
    return i

def order_short(lst):
    """"
    Para sa satida del resultado utilizamos un metodo funcional
    """

    if len(lst) > 1:
        n=len(lst)
        mid = n//2 # Funcion piso
        if n%2==0:
            med = QuickSelect(lst,mid-1) 
        else:
            med = QuickSelect(lst,mid)
        if n > 4:
            k=mid//2
            lst= lst[mid+1:n-k] + lst[0:k] + lst[mid:mid+1] + lst[k:mid] +lst[n-k:]            
    return lst

lst_1=[1,2,3,4,5]
print("lista",lst_1)
lst_1=order_short(lst_1)
print(lst_1)
lst_2=[1,2,3,4,5,6]
print("lista",lst_2)
lst_2=order_short(lst_2)
print(lst_2)

