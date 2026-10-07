
fila = []
modulos = [
    {"nome": "Logística Alfa",   "carga": "Logistica",       "crit": 1, "prio": 5, "massa": 12, "comb": 1800, "energia": 85, "sensores": True},
    {"nome": "Energia",          "carga": "Energia",         "crit": 5, "prio": 5, "massa": 25, "comb": 3300, "energia": 90, "sensores": True},
    {"nome": "Suporte de Vida",  "carga": "Suporte de Vida", "crit": 5, "prio": 4, "massa": 22, "comb": 2900, "energia": 80, "sensores": True},
    {"nome": "Habitação",        "carga": "Habitacao",       "crit": 4, "prio": 4, "massa": 30, "comb": 3800, "energia": 75, "sensores": True},
    {"nome": "Comunicação",      "carga": "Comunicacao",     "crit": 3, "prio": 3, "massa": 10, "comb": 1500, "energia": 35, "sensores": True},
    {"nome": "Médico",           "carga": "Medico",          "crit": 4, "prio": 3, "massa": 15, "comb": 1600, "energia": 70, "sensores": True},
    {"nome": "Laboratório",      "carga": "Laboratorio",     "crit": 2, "prio": 2, "massa": 18, "comb": 2400, "energia": 80, "sensores": False},
    {"nome": "Logística Beta",   "carga": "Logistica",       "crit": 2, "prio": 2, "massa": 14, "comb": 2000, "energia": 85, "sensores": True},
    {"nome": "Extração de Gelo", "carga": "Recursos",        "crit": 2, "prio": 1, "massa": 20, "comb": 2600, "energia": 80, "sensores": True},
]

locais = [
    {"id": "LOC-A", "nome": "Planície Aurora", "lat": "8°N",  "dist_alt": 12, "vagas_prim": 3, "vagas_alt": 2, "tempestade": 5},
    {"id": "LOC-B", "nome": "Cratera Siger",   "lat": "22°S", "dist_alt": 20, "vagas_prim": 2, "vagas_alt": 2, "tempestade": 10},
    {"id": "LOC-C", "nome": "Vale Boreal",     "lat": "28°N", "dist_alt": 0,  "vagas_prim": 3, "vagas_alt": 0, "tempestade": 15},
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
