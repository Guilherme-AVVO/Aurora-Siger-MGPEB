
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

print("==============================================================")
print("  MGPEB - Módulo de Gerenciamento de Pouso e Estabilização de Base")
print("  Missão Aurora Siger | Colônia Marte")
print("==============================================================")
print("Inicializando sistema de controle de pouso...")
print(f"Sistema pronto. {len(modulos)} módulos aguardando em órbita de Marte.")
