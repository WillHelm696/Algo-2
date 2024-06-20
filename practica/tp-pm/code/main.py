from Pattern import *
# Ejercicio 1
def existChar(String,c):
    for char in String:
        if char == c:
            return True 
    return False
# Ejercicio 2
def isPalindrome(string):
    long = len(string)
    for i in range(long // 2):
        if string[i] != string[long - i - 1]:
            return False
    return True
# Ejercicio 3
def mostRepeatedChar(string):
    char_count = {}    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Encontrar el carácter con el mayor número de ocurrencias
    max_count = 0
    most_repeated_char = None
    for char in string:
        if char_count[char] > max_count:
            max_count = char_count[char]
            most_repeated_char = char
    return most_repeated_char
# Ejercicio 4
def getBiggestIslandLen(string):
    if not string:
        return 0
    max_len = 1
    current_len = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1
    if current_len > max_len:
        max_len = current_len
    return max_len
# Ejercicio 5
def isAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    count1 = {}
    count2 = {}
    for char in string1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    for char in string2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    return count1 == count2
# Ejercicio 6
def verifyBalancedParentheses(String):
    count = 0
    for char in String:
        if char == '(':
            count +=1
        elif char == ')':
            count -=1
        if count  < 0:
            return False
    return count == 0

print("Ejercicio 1")# Ejercicio 1
String="Esto es un string"
print(f"el caracter 'a' esta en '{String}': {existChar(String,'a')}")
print("Ejercicio 2")# Ejercicio 2 
String="ojo"
print(f"la palabra '{String}' es palindrome: {isPalindrome(String)}")
print("Ejercicio 3")# Ejercicio 3
string = "aabcccccaaa"
print(f"la cantidad de palabras que se repite en '{string}' :{mostRepeatedChar(string)}")
print("Ejercicio 4")# Ejercicio 4
string = "cdaaaaaasssbbb"
print(f"la longitud de la isla mayor de '{string}' es:{getBiggestIslandLen(string)}")
print("Ejercicio 5")# Ejercicio 5
string1 = "cuaderno"
string2 = "educaron"
print(f"es '{string1}' anagrama de '{string2}' : {isAnagram(string1,string2)}")
print("Ejercicio 6")# Ejercicio 6
string1 = "(ccc(ccc)cc((ccc(c))))"
string2 = ")ccc(ccc)cc((ccc(c)))("
print(f"es corecta '{string1}' : {verifyBalancedParentheses(string1)}")
print(f"es corecta '{string2}' : {verifyBalancedParentheses(string2)}")
print("Ejercicio 7")# Ejercicio 7
string="aaabccddd"
print(f"'aaabccddd' reducido {reduceLen(string)}")  # Salida esperada: "abd"
string="aab"
print(f"'aab' reducido {reduceLen(string)}")        # Salida esperada: "b"
string="abba"
print(f"'abba' reducido {reduceLen(string)}")       # Salida esperada: "" (todos los caracteres se eliminan)
print("Ejercicio 8")# Ejercicio 8
string1="aaafffmmmarillzzzllhooo"
string2= "amarillo"
print(f"es {string2} de {string1}: {isContained(string1,string2)}")  # Salida esperada: True
string1="aaafffmmmarrrilzzzhooo"
string2= "amarillo"
print(f"es {string2} de {string1}: {isContained(string1,string2)}")  # Salida esperada: False
print("Ejercicio 9")# Ejercicio 9
text = "cabccbacbacab"
pattern = "ab♢ba♢c"
wildcard = "♢"
print(f"es {pattern} un patron de {text}: {isPatternContained(text, pattern, wildcard)}")  # Salida esperada: True
print("Ejercicio 12")#Ejercicio 12
text = "aaababaabaababaab"
pattern = "aabab"
print(f"{pattern} en  {text} :{search_pattern(text, pattern)}")
print("Ejercicio 13")# Ejercicio 13
t="abcdf"
p="cdf"
print(f"es '{p}' un patron de '{t}': {Rabin_Karp(t,p)}")
