# 🛰️ Global Solution 2026 - Economia Espacial: Otimização de Rotas Agroclimáticas

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Concluído-success.svg)
![FIAP](https://img.shields.io/badge/FIAP-Engenharia_de_Software-ed145b.svg)

Este repositório contém a solução arquitetada para a **Global Solution (1º Semestre de 2026)** da disciplina de Dynamic Programming. 

O projeto desenvolve um ecossistema de roteamento algorítmico focado em **mitigação de riscos agroclimáticos**, utilizando dados orbitais (NASA, ESA, INPE) para otimizar o deslocamento de equipes de resgate, fornecimento de insumos e infraestrutura no território brasileiro.

---

## 🎯 Visão Geral do Problema e Solução

O Brasil enfrenta perdas bilionárias anuais devido a eventos climáticos extremos. Apesar da vasta disponibilidade de dados satelitais (NDVI, umidade, altimetria), falta uma ponte computacional rápida para transformar esses dados em decisões logísticas eficientes.

Nosso sistema modela o território como uma grade geoespacial bidimensional, onde cruzamos o **Custo Logístico** de acesso com o **Índice de Risco Agroclimático**. Para resolver isso, implementamos três abordagens algorítmicas combinadas:

1. **Programação Dinâmica (Bottom-Up):** O motor principal. Resolve a matriz em tempo polinomial `O(N * M)`, entregando o caminho de custo mínimo absoluto e lidando com obstáculos topológicos.
2. **Simulação de Monte Carlo:** Injeta estocasticidade no modelo. Roda dezenas de milhares de cenários para prever a distribuição de custos logísticos frente à incerteza climática.
3. **Força Bruta:** Algoritmo baseline de enumeração exaustiva `O(2^(N+M))`, utilizado em testes unitários automatizados (CI) para garantir a corretude absoluta da Programação Dinâmica.

---

## 🇧🇷 Cenários Brasileiros Analisados

O algoritmo foi instanciado e validado em duas frentes críticas nacionais:

* **Cenário A (Seca no MATOPIBA):** Otimização de rotas de suprimento agrícola em zonas de estiagem severa (dados derivados do MODIS e pluviometria do INMET).
* **Cenário B (Inundações no Rio Grande do Sul):** Alocação de equipes de resgate em cenários de malha viária fragmentada e rotas fluviais bloqueadas, exigindo do algoritmo respostas sub-milissegundo para contingências reais.

---

## 🌍 Impacto e Sustentabilidade (ODS ONU)

Nossa arquitetura de software se alinha diretamente a cinco Objetivos de Desenvolvimento Sustentável da Agenda 2030:
* **ODS 2:** Fome Zero e Agricultura Sustentável (proteção de safras via previsibilidade).
* **ODS 9:** Indústria, Inovação e Infraestrutura (aplicação de dados orbitais à malha terrestre).
* **ODS 11:** Cidades e Comunidades Sustentáveis (resiliência contra desastres naturais).
* **ODS 13:** Ação Contra a Mudança Global do Clima.
* **ODS 8:** Trabalho Decente e Crescimento Econômico (mitigação de perdas do PIB agrícola).

---

## 👥 Composição do Grupo
* **Davi Correa Paião** - RM: 560438
* **Marcos Vinicius Gonçalves Santos** - RM: 560062
* **Matheus Ricardo Parreira da Silva** - RM: 560099

## 🚀 Instruções de Execução

### Pré-requisitos
* Python 3.10 ou superior.
* Git para clonagem do repositório.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/math-r1card0/global-solution-2026-dynProg.git](https://github.com/math-r1card0/global-solution-2026-dynProg.git)
   cd global-solution-2026-dynProg
