# MGPEB: Módulo de Gerenciamento de Pouso e Estabilização de Base

Protótipo em Python feito para a atividade integradora da Fase 2 de Ciência da Computação da FIAP (missão Aurora Siger). O programa decide quais módulos da colônia podem pousar em Marte, em que ordem e em qual área, e registra cada decisão.

**Grupo 9**

- Felipe de Barros Franco (felipedebarrosfranco@gmail.com)
- Guilherme Santos (guilhermesantos3828@gmail.com)

O relatório técnico está em [`relatorio/Relatorio_Tecnico_MGPEB_Grupo9.pdf`](relatorio/Relatorio_Tecnico_MGPEB_Grupo9.pdf). O anexo de estruturas de dados é a última seção dele.

## Como rodar

Precisa de Python 3.12 ou mais recente. O código usa só a biblioteca padrão.

```bash
python3 main.py
```

O programa pede o local de pouso (1, 2 ou 3) e depois mostra:

1. os nove módulos cadastrados, fora de ordem;
2. a fila de pouso ordenada por prioridade;
3. a avaliação de cada módulo, portão por portão;
4. o relatório final com pousados, em espera e em alerta;
5. o histórico de decisões, do mais recente para o mais antigo;
6. um menu de consultas (digite `0` para sair).

O sorteio do clima usa `random.seed(42)`, então duas execuções com o mesmo local dão o mesmo resultado.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `main.py` | cadastro de módulos e locais, ordenação, fila de pouso, relatório, histórico e consultas |
| `avalicao_modulos.py` | as quatro verificações de pouso (S, C, T e A) |
| `relatorio/` | relatório técnico em PDF |

## Como a decisão funciona

Cada módulo que sai da fila passa por quatro verificações, nesta ordem:

| Portão | Verifica | Se falhar |
|---|---|---|
| S | sensores funcionando e bateria em pelo menos 40% | alerta |
| C | combustível maior ou igual a massa × 110 kg (100 kg/t mais 10% de reserva) | alerta |
| T | sorteio de 1 a 100 maior que a chance de tempestade do local | espera |
| A | vaga na área primária ou, se ela estiver cheia, na alternativa | espera |

Só pousa quem passa nas quatro: `AUTORIZA = S · C · T · A`. Problema do próprio módulo (S ou C) vai para alerta, porque esperar não resolve. Problema do ambiente (T ou A) vai para espera.

Resultado com a semente atual:

| Local | Pousados | Em espera | Em alerta |
|---|---|---|---|
| LOC-A Planície Aurora | 5 de 9 | Suporte de Vida | Comunicação, Médico, Laboratório |
| LOC-B Cratera Siger | 5 de 9 | Suporte de Vida | Comunicação, Médico, Laboratório |
| LOC-C Vale Boreal | 4 de 9 | Energia, Suporte de Vida | Comunicação, Médico, Laboratório |

## Estruturas de dados e algoritmos

- Lista `modulos`: cadastro dos módulos, um dicionário por módulo. As listas `pousados`, `em_espera` e `alerta` guardam o destino de cada um.
- Fila `av_modulos`: cópia da lista ordenada (`modulos[:]`). O módulo da frente sai com `pop(0)`.
- Pilha `historico`: cada decisão entra com `append` e, no fim, sai com `pop()`, da mais recente para a mais antiga.
- Ordenação com bubble sort por prioridade decrescente. A comparação usa `<` estrito, então módulos com a mesma prioridade mantêm a ordem do cadastro.
- Três buscas lineares, por menor combustível, maior prioridade e tipo de carga.

## Premissas

Os módulos, os locais e os números do projeto são fictícios. Foram escolhidos dentro de limites inspirados em documentos da NASA para que a demonstração passe por todos os caminhos de decisão. Os valores definidos pela equipe são: 100 kg de combustível por tonelada, 10% de reserva, energia mínima de 40%, chances de tempestade de 5, 10 e 15% e o número de vagas por área.

## Referências

Material da disciplina (FIAP, Ciência da Computação, Fase 2, 2025):

- Cap. 1: *Ignition Zero: o início da Aurora*
- Cap. 2: *A programação procedural governando cada ajuste de descida* (portas lógicas e funções)
- Cap. 3: *As estruturas lógicas que refinam a correção de trajetória*
- Cap. 4: *As estruturas lineares organizando o fluxo de dados da aproximação*
- Cap. 5: *Os algoritmos que selecionam caminhos e ordenam prioridades de voo*
- Cap. 6: *As funções aplicadas interpretando as variáveis da atmosfera marciana*
- Cap. 7: *A evolução computacional que sustenta os sistemas da nave*
- *Governança ambiental, social e corporativa (ESG)*

Fontes externas:

- NASA. *Systems Engineering Handbook*, [Appendix C: How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/). Formato dos requisitos.
- NASA. *Systems Engineering Handbook*, [5.3 Product Verification](https://www.nasa.gov/reference/5-3-product-verification/). Métodos de verificação e dispensas de requisito.
- Jet Propulsion Laboratory. [*MSL Landing Site Selection: User's Guide to Engineering Constraints*, v4.5](https://marsoweb.nas.nasa.gov/landingsites/msl/memoranda/MSL_Eng_User_Guide_v4.5.1.pdf), 2007. Limites de terreno, vento e áreas alternativas.
- NASA Kennedy Space Center. [*Landing the Space Shuttle Orbiter*](https://www3.nasa.gov/centers/kennedy/pdf/167415main_LandingatKSC06.pdf), 2006. Decisão de pouso e local alternativo.
- NASA. [*Mars Entry, Descent, and Landing: Challenges for Human Missions*](https://www.nasa.gov/wp-content/uploads/2024/12/acr24-mars-edl-challenges.pdf), 2024. Massa dos módulos, poeira e detritos dos motores.
- Bussey, B.; Hoffman, S. J. [*Human Mars Landing Site and Impacts on Mars Surface Operations*](https://ntrs.nasa.gov/citations/20160001040). IEEE Aerospace Conference, 2016. Critérios de local e distância entre módulos pousados.
- NASA Science. [*Perseverance Rover Components*](https://science.nasa.gov/mission/mars-2020-perseverance/rover-components/). Hardware embarcado usado em Marte.
