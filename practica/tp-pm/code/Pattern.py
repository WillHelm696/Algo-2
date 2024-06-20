#Ejercicio 7 aaabccddd
def reduceLen(String):
    stack = []
    for char in String:
        if stack and stack[-1] == char:
            stack.pop()  # Elimina el par de caracteres repetidos
        else:
            stack.append(char)
    return ''.join(stack)
#Ejercicio 8
def isContained(s, p):
    m, n = len(s), len(p)
    i, j = 0, 0    
    while i < m and j < n:
        if s[i] == p[j]:
            j += 1
        i += 1
    return j == n
#Ejercicio 9 Revision
def isPatternContained(text, pattern, wildcard):
    def compute_lps(pattern, wildcard):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length] or pattern[i] == wildcard or pattern[length] == wildcard:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern, wildcard)
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if text[i] == pattern[j] or pattern[j] == wildcard:
            i += 1
            j += 1
        
        if j == m:
            return True
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False
#Ejercicio 12 Revision
def build_automaton(pattern):
    m = len(pattern)
    alphabet = set(pattern)  # Todos los caracteres únicos en el patrón
    automaton = [{c: 0 for c in alphabet} for _ in range(m + 1)]
    
    for i in range(m + 1):
        for c in alphabet:
            k = min(m, i + 1)
            while k > 0 and pattern[:k] != (pattern[:i] + c)[-k:]:
                k -= 1
            automaton[i][c] = k
    return automaton

def search_pattern(text, pattern):
    automaton = build_automaton(pattern)
    m = len(pattern)
    n = len(text)
    state = 0
    
    for i in range(n):
        if text[i] in automaton[state]:
            state = automaton[state][text[i]]
        else:
            state = 0
        if state == m:
            print(f"Pattern found at index {i - m + 1}")
#Ejercicio 13
def hash(p,m):
    key=0
    for n in range (0,m):
        key += ord(p[m-n-1])*(10**n)
    return key

def Rabin_Karp(t,p):
    m=len(p)
    n=len(t)
    if m<n:
        ts=t[:m]
        hp=hash(p,m)
        ht=hash(t,m)
        for s in range(0,n-m+1):
            if ht==hp:
                if ts==p:
                    #print(p,"found at",s)
                    return True
            ht = 10*(ht - (10**(m-1))*ord(t[s]))+ord(t[s+m])
            ts = ts[1:]+t[m+s]
    return False

