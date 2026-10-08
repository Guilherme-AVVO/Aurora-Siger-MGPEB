from main import *
import random  # módulo padrão do Python: simula a incerteza do clima marciano

random.seed(42)
soteio = random.randint(1, 100)
tempestade = soteio <= locais[opcao-1]["tempestade"]

# Avalição de sensores e Avalidação de energia, as duas sãs avaliçoes S
def av_sensores(modulo):
    if modulo["sensores"] == False:
        return False
    else:
        return True

def av_energia(modulo):
    if modulo["energia"] <= 40:
        return False
    else:
        return True

# Avalição de combustivel, essa e a avaliação C
# quanto mais pesado o módulo, mais combustível ele precisa para frear.
# A conta é: massa × 100 kg por tonelada, mais 10 % de reserva. Na prática, massa × 110.
def av_combustivel(modulo):
    comb = modulo["combustivel"]
    massa = modulo["massa"]
    if massa * 110 > comb:
        return False
    else:
        return True

# Avalição de condições atmosféricas, essa e a avaliação T
def av_condicoes_atmosfericas():
    if tempestade == True:
        return False
    else:
        return True
#Avalição area de pouso, verifica se o local primario esta disponivel, senão estiver verifica se o alternativo esta disponovel
#Caso nenhum esteja disponivel retorna False
def av_area_de_pouso(locais):
    if locais[opcao-1]["vagas_prim"] >= 1:
        locais[opcao-1]["vagas_prim"] = locais[opcao-1]["vagas_prim"] - 1
        return True, locais[opcao-1]["vagas_prim"]

    if locais[opcao-1]["vagas_prim"] == 0 and locais[opcao-1]["vagas_alt"] >= 1:
        locais[opcao-1]["vagas_alt"] = locais[opcao-1]["vagas_alt"] - 1
        print("Essa modulo esta pousando em uma vaga alternativa!")
        return True, locais[opcao-1]["vagas_alt"]

    return False,

