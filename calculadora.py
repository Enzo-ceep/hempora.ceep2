#Definiçao das funçoes matematicas basicas
def adicionar (a, b):
    """soma dois numeros"""
    return a+b
def Subtrair(a, b):
    """Subtrai o segundo numero do primeiro"""
    return a-b
def multiplicar(a, b):
    """multiplica dois numeros"""
    return a*b
def dividir(a, b):
    """divide dois numeros, evitando divisão por zero."""
    if b==0:
        return "Erro: Divisão por zero"
    return a/b

#Testes básicos das funções
if __name__ == "__main__":
    print("soma:", adicionar(10, 5))
    print("subtração:", Subtrair(10, 5))
    print("multiplicação:", multiplicar(10, 5))
    print("divisão:", dividir(10, 5))

