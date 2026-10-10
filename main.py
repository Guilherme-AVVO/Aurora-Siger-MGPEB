from avalicao_modulos import *

# Cadastro fora de ordem de propósito, para a ordenação ter trabalho a fazer.
# A posição na lista desempata módulos com a mesma prioridade (ordem de chegada).
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

while True:
    opcao = int(input("\nEscolha o local de pouso (1, 2 ou 3): "))
    match opcao:
        case 1:
            print(f"Local selecionado: {locais[0]["nome"]}")
            print(f"Área primária: {locais[0]["vagas_prim"]} vagas | Área alternativa: {locais[0]["vagas_alt"]} vagas")
            print(f"Chance de tempestade de poeiri <= len(modulosa: {locais[0]["tempestade"]}%")
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

print("\n--- MÓDULOS CADASTRADOS ---\n")
for modulo in modulos:
    print(f"{modulo["nome"]} | cargi <= len(modulosa: {modulo["carga"]} | prioridade: {modulo["prio"]} | criticidade: {modulo["crit"]}")
    print(f"massa: {modulo["massa"]} t | combustível: {modulo["comb"]} kg | energia: {modulo["energia"]}% | sensores: {modulo["sensores"]}")
    print("==========================================================")

print("\nOrdenando módulos por prioridade (desempate: ordem de cadastro)...\n")
#Usando bubble sort por que e um algoritmo estavel
n = len(modulos)
for j in range(n-1):
    for i in range(n-1):
        if modulos[i]["prio"] < modulos[i+1]["prio"]:
            modulos[i], modulos[i+1] = modulos[i+1], modulos[i]

print("Fila de pouso montada:")

for index,modulo in enumerate(modulos):
    print(f"{index+ 1}° {modulo["nome"]} (prioridade {modulo["prio"]}) ")

pousados = []
alerta = []
em_espera = []
av_modulos = modulos[:]

while 0 < len(av_modulos):
    print(f"\nAvaliando: {av_modulos[0]["nome"]} ({av_modulos[0]["carga"]}) | restam {len(av_modulos)} na fila\n")
    # Avaliação S
    s1, motivo_sensor = av_sensores(av_modulos[0])
    s2, motivo_energia = av_energia(av_modulos[0])
    if s1 == False:
        print(f"[S]Sensores e energia ...... FALHA ({motivo_sensor})")
        print(f">> MÓDULO EM ALERTA: {motivo_sensor}")
        alerta.append({"nome": av_modulos[0]["nome"], "motivo": motivo_sensor })
        av_modulos.pop(0)
        continue
    elif s2 == False:
        print(f"[S] Sensores e energia ...... FALHA (energia {av_modulos[0]["energia"]}% abaixo do mínimo de 40%)")
        print(f">> MÓDULO EM ALERTA: {motivo_energia}")
        alerta.append({"nome": av_modulos[0]["nome"], "motivo": motivo_energia })
        av_modulos.pop(0)
        continue
    else:
        print(f"[S] Sensores e energia ...... OK (sensores operacionais, energia {av_modulos[0]["energia"]}%)")
    # Avalição C
    c,motivo_comb = av_combustivel(av_modulos[0])
    if c == False:
        print(f"[C] Combustível ............. FALHA ({av_modulos[0]["comb"]} kg < mínimo {av_modulos[0]["massa"] * 110} kg, margem {av_modulos[0]["comb"] - (av_modulos[0]["massa"]  * 110)} kg)")
        print(f">> MÓDULO EM ALERTA: {motivo_comb}")
        alerta.append({"nome": av_modulos[0]["nome"], "motivo": motivo_comb })
        av_modulos.pop(0)
        continue
    else:
       print(f"[C] Combustível ............. OK ({av_modulos[0]["comb"]} kg ≥ mínimo {av_modulos[0]["massa"] * 110} kg, margem +{av_modulos[0]["comb"] - (av_modulos[0]["massa"]  * 110)} kg)")

    # Avaliação T
    t,motivo_tempestade,sorteio,chance = av_condicoes_atmosfericas(locais,opcao)
    if t == False:
        print(f"[T] Condições atmosféricas .. FALHA (sorteio {sorteio} ≤ {chance}%: tempestade de poeira)")
        print(f">> MÓDULO EM ESPERA: {motivo_tempestade}")
        em_espera.append({"nome": av_modulos[0]["nome"], "motivo": motivo_tempestade})
        av_modulos.pop(0)
        continue
    else:
        print(f"[T] Condições atmosféricas .. OK (sorteio {sorteio} > {chance}%: sem tempestade)")

    #Avaliando A
    a,local_pouso,loc,vagas = av_area_de_pouso(locais,opcao)
    if a == False:
        print(f"[A] Área de pouso ........... FALHA ({local_pouso})")
        print(f">> MÓDULO EM ESPERA: sem vaga nas áreas de pouso")
        em_espera.append({"nome": av_modulos[0]["nome"], "motivo": local_pouso})
    else:
        print(f"[A] Área de pouso ........... OK ({local_pouso}, restam {vagas} vagas)")
        print(f">> POUSO AUTORIZADO na área {loc}")
        pousados.append({"nome": av_modulos[0]["nome"], "local_pouso": local_pouso, "vaga": loc})
    av_modulos.pop(0)


