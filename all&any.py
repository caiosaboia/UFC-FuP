#Funções all e any

L = [7,2,5,4]
M = [7,5,6,2,1]

C = [x in M for x in L] #list comprehension
#print(C)

todos = all(C)
alguem = any(C)

#print(todos)
#print(alguem)
