# As funções dos portões (S, C, T e A) ficam em avalicao_modulos.py,
# assim este arquivo cuida só do fluxo do programa.
from avalicao_modulos import *

# Cadastro dos módulos. Cada módulo é um dicionário com os mesmos campos:
#   crit = criticidade, de 1 a 5 (o quanto perder esse módulo seria grave)
#   prio = prioridade de pouso, de 1 a 5 (quem tem 5 desce primeiro)
#   massa em toneladas, comb = combustível em kg, energia em %
#   sensores = True quando estão funcionando
# Deixei a lista fora de ordem de propósito, para o bubble sort ter trabalho.
# Quando dois módulos têm a mesma prioridade, quem está antes aqui pousa antes,
# como se fosse a ordem de chegada na órbita.
modulos = [
    {"nome": "Comunicação",      "carga": "Comunicacao",     "crit": 3, "prio": 3, "massa": 10, "comb": 1500, "energia": 35, "sensores": True},
    {"nome": "Extração de Gelo", "carga": "Recursos",        "crit": 2, "prio": 1, "massa": 20, "comb": 2600, "energia": 80, "sensores": True},
    {"nome": "Logística Alfa",   "carga": "Logistica",       "crit": 1, "prio": 5, "massa": 12, "comb": 1800, "energia": 85, "sensores": True},
    {"nome": "Laboratório",      "carga": "Laboratorio",     "crit": 2, "prio": 2, "massa": 18, "comb": 2400, "energia": 80, "sensores": False},
    {"nome": "Suporte de Vida",  "carga": "Suporte de Vida", "crit": 5, "prio": 4, "massa": 22, "comb": 2900, "energia": 80, "sensores": True},
    {"nome": "Médico",           "carga": "Medico",          "crit": 4, "prio": 3, "massa": 15, "comb": 1600, "energia": 70, "sensores": True},
    {"nome": "Energia",          "carga": "Energia",         "crit": 5, "prio": 5, "massa": 25, "comb": 3300, "energia": 90, "sensores": True},
    {"nome": "Logística Beta",   "carga": "Logistica",       "crit": 2, "prio": 2, "massa": 14, "comb": 2000, "energia": 85, "sensores": True},
    {"nome": "Habitação",        "carga": "Habitacao",       "crit": 4, "prio": 4, "massa": 30, "comb": 3800, "energia": 75, "sensores": True},
]

# Os três locais de pouso possíveis. Os números são fictícios, escolhidos para
# cada local se comportar de um jeito diferente na simulação.
#   vagas_prim e vagas_alt = quantos módulos cabem em cada área
#   tempestade = chance de tempestade de poeira, em %
# O LOC-C não tem área alternativa (0 vagas), então lá não existe desvio.
locais = [
    {"id": "LOC-A", "nome": "Planície Aurora", "lat": "8°N",  "dist_alt": 12, "vagas_prim": 8, "vagas_alt": 2, "tempestade": 5},
    {"id": "LOC-B", "nome": "Cratera Siger",   "lat": "22°S", "dist_alt": 20, "vagas_prim": 7, "vagas_alt": 2, "tempestade": 10},
    {"id": "LOC-C", "nome": "Vale Boreal",     "lat": "28°N", "dist_alt": 0,  "vagas_prim": 9, "vagas_alt": 0, "tempestade": 15},
]

print("==============================================================")
print("  MGPEB - Módulo de Gerenciamento de Pouso e Estabilização de Base")
print("  Missão Aurora Siger | Colônia Marte")
print("==============================================================")
print("Inicializando sistema de controle de pouso...")
print(f"Sistema pronto. {len(modulos)} módulos aguardando em órbita de Marte.")

print("\n--- SELEÇÃO DO LOCAL DE POUSO ---")
print("[1] LOC-A Planície Aurora | 8°N  | área alternativa: sim (12 km)")
print("[2] LOC-B Cratera Siger   | 22°S | área alternativa: sim (20 km)")
print("[3] LOC-C Vale Boreal     | 28°N | área alternativa: NÃO")

# O while só termina quando o usuário escolhe uma opção válida.
while True:
    opcao = int(input("\nEscolha o local de pouso (1, 2 ou 3): "))
    match opcao:
        case 1:
            print(f"Local selecionado: {locais[0]["nome"]}")
            print(f"Área primária: {locais[0]["vagas_prim"]} vagas | Área alternativa: {locais[0]["vagas_alt"]} vagas")
            print(f"Chance de tempestade de poeira: {locais[0]["tempestade"]}%")
            break
        case 2:
            print(f"Local selecionado: {locais[1]["nome"]}")
            print(f"Área primária: {locais[1]["vagas_prim"]} vagas | Área alternativa: {locais[1]["vagas_alt"]} vagas")
            print(f"Chance de tempestade de poeira: {locais[1]["tempestade"]}%")
            break
        case 3:
            print(f"Local selecionado: {locais[2]["nome"]}")
            print(f"Área primária: {locais[2]["vagas_prim"]} vagas | Área alternativa: {locais[2]["vagas_alt"]} vagas")
            print(f"Chance de tempestade de poeira: {locais[2]["tempestade"]}%")
            break
        case _:
            print("opção invalida, tente novamente!")

# Mostra o cadastro como está, ainda fora de ordem, para comparar com a fila depois.
print("\n--- MÓDULOS CADASTRADOS ---\n")
for modulo in modulos:
    print(f"{modulo["nome"]} | carga: {modulo["carga"]} | prioridade: {modulo["prio"]} | criticidade: {modulo["crit"]}")
    print(f"massa: {modulo["massa"]} t | combustível: {modulo["comb"]} kg | energia: {modulo["energia"]}% | sensores: {modulo["sensores"]}")
    print("==========================================================")

print("\nOrdenando módulos por prioridade (desempate: ordem de cadastro)...\n")
# Ordenação com bubble sort: compara cada módulo com o vizinho da direita e
# troca os dois se o da esquerda tiver prioridade menor. Repetindo isso, os de
# prioridade maior vão subindo para o começo da lista.
# Escolhi o bubble sort porque ele é estável. Com o "<" ele nunca troca dois
# módulos de mesma prioridade, então o empate respeita a ordem do cadastro.
n = len(modulos)
for j in range(n-1):
    for i in range(n-1):
        if modulos[i]["prio"] < modulos[i+1]["prio"]:
            modulos[i], modulos[i+1] = modulos[i+1], modulos[i]

print("Fila de pouso montada:")

for index,modulo in enumerate(modulos):
    print(f"{index+ 1}° {modulo["nome"]} (prioridade {modulo["prio"]}) ")

# Listas para onde cada módulo vai depois de avaliado.
# historico funciona como pilha: cada decisão entra no fim, e no final eu tiro
# pelo fim também, mostrando da decisão mais recente para a mais antiga.
# av_modulos é a fila de pouso. Fiz uma cópia com [:] para ir tirando os
# módulos dela sem esvaziar a lista original, que as buscas ainda usam.
pousados = []
alerta = []
em_espera = []
historico = []
av_modulos = modulos[:]

# Laço principal: enquanto houver módulo na fila, pego o primeiro e passo ele
# pelos portões na ordem S, C, T e A.
# Se falhar em algum, ele vai para a lista certa, sai da fila com pop(0) e o
# continue pula para o próximo módulo sem olhar os portões seguintes.
# Falha em S ou C vai para alerta, porque é problema do próprio módulo e esperar
# não resolve. Falha em T ou A vai para espera, porque a tempestade passa e
# uma vaga pode abrir depois.
while 0 < len(av_modulos):
    print(f"\nAvaliando: {av_modulos[0]["nome"]} ({av_modulos[0]["carga"]}) | restam {len(av_modulos)} na fila\n")
    # Portão S: primeiro os sensores, depois a energia
    s1, motivo_sensor = av_sensores(av_modulos[0])
    s2, motivo_energia = av_energia(av_modulos[0])
    if s1 == False:
        print(f"[S] Sensores e energia ...... FALHA ({motivo_sensor})")
        print(f">> MÓDULO EM ALERTA: {motivo_sensor}")
        alerta.append({"nome": av_modulos[0]["nome"], "motivo": motivo_sensor })
        historico.append({"nome": av_modulos[0]["nome"], "resultado": "ALERTA", "detalhe": motivo_sensor})
        av_modulos.pop(0)
        continue
    elif s2 == False:
        print(f"[S] Sensores e energia ...... FALHA (energia {av_modulos[0]["energia"]}% abaixo do mínimo de 40%)")
        print(f">> MÓDULO EM ALERTA: {motivo_energia}")
        alerta.append({"nome": av_modulos[0]["nome"], "motivo": motivo_energia })
        historico.append({"nome": av_modulos[0]["nome"], "resultado": "ALERTA", "detalhe": motivo_energia})
        av_modulos.pop(0)
        continue
    else:
        print(f"[S] Sensores e energia ...... OK (sensores operacionais, energia {av_modulos[0]["energia"]}%)")
    # Portão C: a margem é o combustível que o módulo tem menos o mínimo que ele precisa
    c,motivo_comb = av_combustivel(av_modulos[0])
    if c == False:
        print(f"[C] Combustível ............. FALHA ({av_modulos[0]["comb"]} kg < mínimo {av_modulos[0]["massa"] * 110} kg, margem {av_modulos[0]["comb"] - (av_modulos[0]["massa"]  * 110)} kg)")
        print(f">> MÓDULO EM ALERTA: {motivo_comb}")
        alerta.append({"nome": av_modulos[0]["nome"], "motivo": motivo_comb })
        historico.append({"nome": av_modulos[0]["nome"], "resultado": "ALERTA", "detalhe": motivo_comb})
        av_modulos.pop(0)
        continue
    else:
       print(f"[C] Combustível ............. OK ({av_modulos[0]["comb"]} kg ≥ mínimo {av_modulos[0]["massa"] * 110} kg, margem +{av_modulos[0]["comb"] - (av_modulos[0]["massa"]  * 110)} kg)")

    # Portão T: um sorteio novo de clima para este módulo
    t,motivo_tempestade,sorteio,chance = av_condicoes_atmosfericas(locais,opcao)
    if t == False:
        print(f"[T] Condições atmosféricas .. FALHA (sorteio {sorteio} ≤ {chance}%: tempestade de poeira)")
        print(f">> MÓDULO EM ESPERA: {motivo_tempestade}")
        em_espera.append({"nome": av_modulos[0]["nome"], "motivo": motivo_tempestade})
        historico.append({"nome": av_modulos[0]["nome"], "resultado": "ESPERA", "detalhe": motivo_tempestade})
        av_modulos.pop(0)
        continue
    else:
        print(f"[T] Condições atmosféricas .. OK (sorteio {sorteio} > {chance}%: sem tempestade)")

    # Portão A: se achar vaga aqui, o pouso está autorizado
    a,motivo_local,area,vagas = av_area_de_pouso(locais,opcao)
    if a == False:
        print(f"[A] Área de pouso ........... FALHA ({motivo_local})")
        print(f">> MÓDULO EM ESPERA: sem vaga nas áreas de pouso")
        em_espera.append({"nome": av_modulos[0]["nome"], "motivo": motivo_local})
        historico.append({"nome": av_modulos[0]["nome"], "resultado": "ESPERA", "detalhe": motivo_local})
        av_modulos.pop(0)
        continue
    else:
        print(f"[A] Área de pouso ........... OK ({motivo_local}, restam {vagas} vagas)")
        print(f">> POUSO AUTORIZADO na área {area}")
        pousados.append({"nome": av_modulos[0]["nome"], "motivo_local": motivo_local, "area": area})
        historico.append({"nome": av_modulos[0]["nome"], "resultado": "AUTORIZADO", "detalhe": area})
    # Passou pelos quatro portões e pousou, então sai da fila
    av_modulos.pop(0)

# Relatório final: quem pousou, quem ficou esperando e quem está em alerta.
# O if vem antes do for para mostrar "(nenhum módulo)" quando a lista está vazia.
print("\n==============================================================")
print(f"RELATÓRIO FINAL DA OPERAÇÃO DE POUSO - {locais[opcao-1]["nome"]}")
print("==============================================================\n")
print(f"POUSADOS ({len(pousados)}):")
if len(pousados) == 0:
    print("(nenhum módulo)")
else:
    for p in pousados:
        print(f"- {p["nome"]} | área {p["area"]}")
print("\n================================================================\n")
print(f"EM ESPERA ({len(em_espera)}):")
if len(em_espera) == 0:
    print("(nenhum módulo)")
else:
    for e in em_espera:
        print(f"- {e["nome"]} | motivo: {e["motivo"]}")
print("\n================================================================\n")
print(f"EM ALERTA ({len(alerta)}):")
if len(alerta) == 0:
    print("(nenhum módulo)")
else:
    for item in alerta:
        print(f"- {item["nome"]} | motivo: {item["motivo"]}")

# Histórico: aqui a lista é usada como pilha. O pop() sem número tira sempre o
# último registro, que é a decisão mais recente. O n é o tamanho da pilha antes
# de tirar, por isso a numeração vai de 9 até 1. No fim a pilha fica vazia.
print("\n--- HISTÓRICO DE DECISÕES (mais recente primeiro) ---\n")
while len(historico) > 0:
    n = len(historico)
    registro = historico.pop()
    print(f"{n}. {registro["nome"]} -> {registro["resultado"]} | {registro["detalhe"]}")

# Buscas: as três são lineares, olham módulo por módulo do começo ao fim.
# Usam a lista "modulos", que continua com os 9 porque a fila era uma cópia.

# Menor combustível: começo achando que o primeiro é o menor e troco sempre
# que aparece um com menos combustível.
def buscar_menor_combustivel(lista):
    menor = lista[0]
    for modulo in lista:
        if modulo["comb"] < menor["comb"]:
            menor = modulo
    return menor

# Maior prioridade: mesma ideia. Com o ">" estrito, no empate fica o primeiro
# encontrado. Como a lista já foi ordenada, dá Logística Alfa e não Energia.
def buscar_maior_prioridade(lista):
    maior = lista[0]
    for modulo in lista:
        if modulo["prio"] > maior["prio"]:
            maior = modulo
    return maior

# Por tipo de carga: junta numa lista todos os módulos com a carga digitada.
# Comparo em minúsculas para "energia" e "Energia" darem o mesmo resultado.
def buscar_por_carga(lista, carga):
    encontrados = []
    for modulo in lista:
        if modulo["carga"].lower() == carga.lower():
            encontrados.append(modulo)
    return encontrados

# Menu das consultas. Comparo a opção como texto ("1", "2"...) para que uma
# letra digitada caia em "opção inválida" em vez de travar o programa.
while True:
    print("\n--- CONSULTAS ---")
    print("[1] Módulo com menor combustível")
    print("[2] Módulo com maior prioridade")
    print("[3] Módulos por tipo de carga")
    print("[0] Encerrar")
    escolha = input("\nEscolha uma consulta: ")

    if escolha == "1":
        menor = buscar_menor_combustivel(modulos)
        print(f"Menor combustível: {menor["nome"]} com {menor["comb"]} kg")
    elif escolha == "2":
        maior = buscar_maior_prioridade(modulos)
        print(f"Maior prioridade: {maior["nome"]} (prioridade {maior["prio"]})")
    elif escolha == "3":
        carga = input("Digite o tipo de carga (ex.: Logistica, Energia, Medico): ")
        encontrados = buscar_por_carga(modulos, carga)
        if len(encontrados) == 0:
            print(f"Nenhum módulo encontrado com carga \"{carga}\".")
        else:
            nomes = []
            for modulo in encontrados:
                nomes.append(modulo["nome"])
            print(f"Módulos com carga \"{carga}\": {", ".join(nomes)}")
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Digite um número de 0 a 3.")

# Encerramento. Uso len(modulos) para o total porque a fila termina vazia.
print("\n==============================================================")
print(f"Encerrando MGPEB. Base Aurora Siger: {len(pousados)} de {len(modulos)} módulos em solo.")
print("Bons pousos, colônia.")
print("==============================================================")

