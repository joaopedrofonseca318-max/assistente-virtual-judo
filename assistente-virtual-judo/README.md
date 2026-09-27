# 🥋 Tatame IA — Assistente Virtual para Atletas e Professores de Judô

Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"** (Digital Innovation One).

## Sobre o Projeto

**Tatame IA** é um assistente virtual que responde dúvidas sobre judô — faixas, regras de pontuação, técnicas, estrutura de aula, etiqueta, prevenção de lesões e mais — direcionado a **atletas** e **professores(as)/sensei**.

O assistente usa uma base de conhecimento estruturada e um padrão de **RAG (Retrieval-Augmented Generation)**: primeiro busca a informação relevante, depois formula a resposta com base nela — evitando "inventar" regras ou técnicas, e assumindo claramente quando não tem informação suficiente.

## Estrutura do Repositório

```
assistente-virtual-judo/
├── README.md                    # este arquivo
├── data/
│   └── base_conhecimento.json   # base de conhecimento estruturada (15 itens)
├── docs/
│   ├── documentacao.md          # o que o assistente faz, para quem, como se comporta
│   ├── prompts.md                # system prompt e instruções do agente
│   ├── avaliacao.md              # metodologia de avaliação e casos de teste
│   └── pitch.md                   # apresentação do problema, solução e valor
└── src/
    └── app.py                     # aplicação funcional (CLI)
```

## Como Rodar

Pré-requisito: Python 3.8+ (não precisa de nenhuma biblioteca externa).

```bash
cd assistente-virtual-judo
python src/app.py
```

Por padrão, a aplicação roda em **modo offline**: busca a pergunta na base de conhecimento e mostra diretamente os itens mais relevantes, sem gerar texto novo.

### Modo com IA generativa (opcional)

Para que o assistente formule respostas mais naturais com Claude a partir do contexto recuperado, configure sua chave de API da Anthropic:

```bash
export ANTHROPIC_API_KEY="sua-chave-aqui"     # Linux/Mac
setx ANTHROPIC_API_KEY "sua-chave-aqui"        # Windows (novo terminal depois)

python src/app.py
```

## Exemplo de Uso

```
Você: Qual a ordem das faixas no judô?

Tatame IA: 📌 Sistema de Faixas (Kyu/Dan)
No sistema brasileiro mais comum, a ordem geral das faixas é: Branca, Cinza, Azul,
Amarela, Laranja, Verde, Roxa, Marrom e Preta...
```

## Os 6 Passos do Desafio

| Passo | Onde está |
|---|---|
| 1. Documentação | [`docs/documentacao.md`](docs/documentacao.md) |
| 2. Base de Conhecimento | [`data/base_conhecimento.json`](data/base_conhecimento.json) |
| 3. Prompts | [`docs/prompts.md`](docs/prompts.md) |
| 4. Aplicação Funcional | [`src/app.py`](src/app.py) |
| 5. Avaliação e Métricas | [`docs/avaliacao.md`](docs/avaliacao.md) |
| 6. Pitch | [`docs/pitch.md`](docs/pitch.md) |

## Projeto Original / Referência

Este projeto foi desenvolvido a partir do desafio [Construa Seu Assistente Virtual Com Inteligência Artificial](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro), da Digital Innovation One.

## Autor(a)

João Pedro Fonseca Preigschadt
Linkedin: linkedin.com/in/joão-pedro-fonseca-6460481a5
