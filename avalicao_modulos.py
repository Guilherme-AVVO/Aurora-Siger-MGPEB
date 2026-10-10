import random  # biblioteca padrão do Python, usada para sortear o clima de cada descida

# A semente fixa faz o sorteio sair igual toda vez que o programa roda,
# então a apresentação mostra o mesmo resultado que eu testei.
# Ela fica aqui em cima porque precisa rodar uma vez só. Dentro da função,
# todo módulo receberia o mesmo número.
random.seed(42)

# Cada função abaixo é um "portão" da autorização de pouso (S, C, T e A).
# Todas seguem o mesmo padrão: devolvem True quando o módulo passa, ou False
# junto com o motivo quando ele é barrado. Quem imprime e decide para qual
# lista o módulo vai é o main.py.

# Portão S, parte 1: o módulo precisa dos sensores para medir altura e
# velocidade durante a descida. Sem eles, desce às cegas.
def av_sensores(modulo):
    if modulo["sensores"] == False:
        return False,"falha de sensor"
    else:
        return True,None

# Portão S, parte 2: a energia alimenta os sensores e o computador de bordo.
# Abaixo de 40% considerei arriscado demais começar a descida.
def av_energia(modulo):
    if modulo["energia"] < 40:
        return False,"energia abaixo do mínimo"
    else:
        return True,None

# Portão C: confere se o combustível dá para frear até o chão.
# Quanto mais pesado o módulo, mais combustível ele gasta. A conta que usei é
# 100 kg por tonelada mais 10% de reserva de segurança, o que dá massa × 110.
def av_combustivel(modulo):
    comb = modulo["comb"]
    massa = modulo["massa"]
    if massa * 110 > comb:
        return False,"combustível insuficiente"
    else:
        return True,None

# Portão T: sorteia um número de 1 a 100 e compara com a chance de tempestade
# do local. No LOC-B, por exemplo, a chance é 10%, então os números de 1 a 10
# viram tempestade. O sorteio fica dentro da função para cada módulo ter o
# próprio clima. Devolvo também o número sorteado e a chance para mostrar no terminal.
def av_condicoes_atmosfericas(locais,opcao):
    sorteio = random.randint(1, 100)
    chance = locais[opcao - 1]["tempestade"]
    tempestade = sorteio <= chance
    if tempestade == True:
        return False,"tempestade de poeira",sorteio,chance
    else:
        return True,None,sorteio,chance

# Portão A: procura uma vaga para o módulo descer.
# Primeiro tenta a área primária e, se ela estiver cheia, a alternativa.
# No LOC-C a alternativa tem 0 vagas, então esse segundo caminho nunca acontece.
# Cada pouso ocupa uma vaga, por isso diminuo o contador direto no dicionário do local.
# Devolve o resultado, a frase para o terminal, a área usada e quantas vagas sobraram.
def av_area_de_pouso(locais,opcao):
    if locais[opcao-1]["vagas_prim"] >= 1:
        locais[opcao-1]["vagas_prim"] = locais[opcao-1]["vagas_prim"] - 1
        return True,"área primária","primária",locais[opcao-1]["vagas_prim"]

    if locais[opcao-1]["vagas_prim"] == 0 and locais[opcao-1]["vagas_alt"] >= 1:
        locais[opcao-1]["vagas_alt"] = locais[opcao-1]["vagas_alt"] - 1
        return True,"primária lotada, desviando para alternativa","alternativa",locais[opcao-1]["vagas_alt"]

    return False,"sem vaga nas áreas de pouso",None,None

