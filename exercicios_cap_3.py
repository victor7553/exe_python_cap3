#capítulo 3

print('\n------------- exercicio 3.1 --------------------')
# Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado.

#     Número      Tipo numérico
#     5      ○ inteiro ○ ponto flutuante
#     5.0    ○ inteiro ○ ponto flutuante
#     4.3    ○ inteiro ○ ponto flutuante
#     -2     ○ inteiro ○ ponto flutuante
#     100    ○ inteiro ○ ponto flutuante
#     1.333  ○ inteiro ○ ponto flutuante

num_1 = print(type (5))
num_2 = print(type(5.0))
num_3 = print(type(4.3))
num_4 = print(type(-2))
num_5 = print(type(100))
num_6 = print(type(1.333))


print('\n------------- exercicio 3.2 --------------------')
# Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

# Expressão Resultado        Expressão Resultado
# a == c    ○ True ○ False   b > a     ○ True ○ False
# a < b     ○ True ○ False   c >= f    ○ True ○ False
# d > b     ○ True ○ False   f >= c    ○ True ○ False
# c != f    ○ True ○ False   c <= c    ○ True ○ False
# a == b    ○ True ○ False   c <= f    ○ True ○ False
# c < d     ○ True ○ False

a = 4 
b = 10
c = 5.0
d = 1
f = 5

print(a==c)
print(a < b)
print(d > b)
print(c !=f)
print(a==b)
print(c < d)
print(b > a)
print(c >= f)
print(f >= c)
print(c <= c)
print(c <= f)


print('\n------------- exercicio 3.3 --------------------')
# Complete a tabela a seguir utilizando a = True, b = False e c = True.

# Expressão Resultado         Expressão Resultado
# a and a   ○ True ○ False    a or c    ○ True ○ False
# b and b   ○ True ○ False    b or c    ○ True ○ False
# not c     ○ True ○ False    c or a    ○ True ○ False
# not b     ○ True ○ False    c or b    ○ True ○ False
# not a     ○ True ○ False    c or c    ○ True ○ False
# a and b   ○ True ○ False    b or b    ○ True ○ False
# b and c   ○ True ○ False

a = True
b = False
c = True

print(a and a)
print(b and b)
print(not c)
print(not b)
print(not a)
print(a and b)
print(b and c)
print(a or c)
print(b or c)
print(c or a)
print(c or b)
print(c or c)
print(b or b)



