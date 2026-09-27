# Documentação do Agente — Tatame IA

## 1. O que é

**Tatame IA** é um assistente virtual com inteligência artificial voltado para **atletas e professores(as) de judô**. Ele responde dúvidas comuns sobre regras, técnicas, faixas, treino, etiqueta e cuidados básicos, usando como base uma coleção organizada de informações sobre o esporte.

## 2. Para quem serve

- **Atletas de judô** (de iniciantes a competidores) que querem entender melhor regras, técnicas e como se preparar.
- **Professores(as)/sensei** que precisam de apoio rápido para organizar aulas, explicar regras a alunos(as) ou relembrar informações técnicas.

Não é voltado para o público em geral sem contato com o judô, embora qualquer pessoa curiosa possa usá-lo.

## 3. Objetivo do assistente

Ajudar a pessoa usuária a:
1. Entender uma dúvida específica sobre judô (regra, técnica, faixa, treino, etc.);
2. Tomar uma decisão prática a partir disso — por exemplo, saber que precisa checar o regulamento oficial, procurar um profissional de saúde, ou como estruturar uma aula.

## 4. Como ele deve se comportar

O Tatame IA segue estas diretrizes de comportamento (detalhadas em `docs/prompts.md`):

- **Responde apenas com base na base de conhecimento** (`data/base_conhecimento.json`) ou em conhecimento geral e verificável sobre judô — nunca inventa regras, técnicas ou números.
- **Assume quando não sabe.** Se a pergunta foge do escopo do judô ou não há informação suficiente na base, o assistente diz isso claramente, em vez de arriscar uma resposta errada.
- **Não dá conselhos médicos, nutricionais ou de corte de peso específicos.** Para esses temas, sempre orienta a buscar um profissional (médico, nutricionista, fisioterapeuta, psicólogo do esporte).
- **Tom didático e respeitoso**, alinhado à cultura do judô (uso de termos japoneses com explicação em português).
- **Sempre que a informação puder variar entre federações** (ex.: tempo entre graduações, categorias de peso), o assistente avisa isso e recomenda checar a fonte oficial.

## 5. Limitações conhecidas

- A base de conhecimento é um protótipo pequeno (15 itens) e não cobre todas as técnicas ou situações do judô.
- Regras de competição (como pontuação da IJF) mudam com frequência; o assistente pode estar desatualizado e sempre recomenda checar o regulamento vigente.
- Não substitui orientação médica, nutricional, psicológica ou de primeiros socorros.

## 6. Estrutura do projeto

```
assistente-virtual-judo/
  README.md              -> visão geral do projeto
  data/
    base_conhecimento.json -> base de conhecimento estruturada
  docs/
    documentacao.md        -> este arquivo
    prompts.md              -> prompts e instruções do agente
    avaliacao.md            -> metodologia de avaliação e casos de teste
    pitch.md                 -> apresentação do projeto
  src/
    app.py                   -> aplicação funcional (CLI)
```
