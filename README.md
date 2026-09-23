# Cracking the Coding Interview em Python

Este repositório reúne exercícios, desafios e implementações de algoritmos em Python, com foco em estudo, prática e revisão de conceitos importantes de lógica, estruturas de dados e resolução de problemas.

## Objetivo

O principal objetivo deste projeto é:

- praticar algoritmos clássicos e soluções de entrevista;
- fortalecer conceitos de lógica de programação;
- desenvolver a habilidade de escrever código limpo e eficiente;
- documentar soluções e raciocínios usados para cada problema.

## Estrutura do projeto

```text
.
├── chapter_1/
│   ├── problem_1.py
│   └── problem_2.py
├── Pipfile
└── README.md
```

## Capítulo 1: Arrays e Strings

Os exercícios atuais estão na pasta `chapter_1` e são organizados em arquivos individuais:

- `problem_1.py`: verifica se uma string possui apenas caracteres únicos usando uma bitmask;
- `problem_2.py`: verifica se duas strings são permutações usando contagem de frequência.

Os arquivos também registram as premissas e a análise de complexidade de cada solução.

## Como executar

Certifique-se de ter o Python 3.10 instalado.

### 1. Instalar as dependências

```bash
pipenv install --dev
```

### 2. Ativar o ambiente

```bash
pipenv shell
```

### 3. Executar um arquivo

```bash
python chapter_1/problem_1.py
```

ou

```bash
python chapter_1/problem_2.py
```

Também é possível executar diretamente pelo Pipenv:

```bash
pipenv run python chapter_1/problem_1.py
```

## Depuração no VS Code

Você pode rodar os arquivos diretamente no editor com a configuração de depuração do VS Code:

1. Abra a pasta do projeto no VS Code.
2. Selecione o arquivo Python que deseja testar.
3. Pressione `F5` ou use a opção "Run and Debug".
4. Coloque breakpoints para acompanhar a execução passo a passo.

## Tecnologias utilizadas

- Python 3
- VS Code
- Pipenv

## Observações

Este é um projeto pessoal de estudo. Novos problemas podem ser adicionados em capítulos e arquivos separados, acompanhados de suas premissas, solução e análise de complexidade.