from Triee import *

T=Trie()
insert(T,"cris")
print(search(T,"cris"))
insert(T,"cruz")
print(search(T,"cruz"))
insert(T,"javi")
print(search(T,"javi"))
insert(T,"juan")
print(search(T,"juan"))
insert(T,"rafa")
print(search(T,"rafa"))

print_words(T)
