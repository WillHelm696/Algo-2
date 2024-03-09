def contiene_suma(A,n):
    #Creamos un conjunto para almacenar los elementos vistos
    vistos=set()

    #iteramos sobre la lista A, y visitamos cada elemento de la lista
    for num in A:
        #calculamos el complemento esesario para que la suma sea n
        complemento = n - num
        #Verificamos si el complemento ya esta en la lista de elementos visitados
        if complemento in vistos:
			#Si seencuentra un par que dado su suma da n
            return True
        vistos.add(num)
	#Si no se a ancontrado entonces retorna falso
    return False

A=[1,2,3,4,5]
n=9
print("Lista: ",A)
print("¿La lista A contiene un par de elementos que suman",n,"? ", contiene_suma(A,n) )
#la compejiad del algoritmo seria O(n) ya que solo recoremos la lista una vez y realiza las operaciones en tiempo constante en cada iteracion.

