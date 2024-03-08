def contiene_suma(A,n):
	#Creamos un conjunto para almacenar los elementos vistos
	vistos=set()
	
	#Iteramos sobre la lista A, con el for visitamos cada elemento de la lista
	for num in A:

        #Calculamos el complemeento nesesrio para que la suma sea n
	    complemento = n - num
        #Verifficamos si el complemento ya esta en el conjunto de elementos vistos  
	    if complemento  in visitos:
	    
	        return True
		#Si no no encntramos ningun para que sume n, retornamos FALSO
		visitos.add(num)
    return False

A = [1,2,3,4,5]
n = 9
print("Lista: ",A)
print("¿La lista A contiene un par de elementos que suman",n,"? ", contiene_suma(A,n) )
#la compejiad del algoritmo seria O(n) ya que solo recoremos la lista una vez y realiza las operaciones en tiempo constante en cada iteracion.

