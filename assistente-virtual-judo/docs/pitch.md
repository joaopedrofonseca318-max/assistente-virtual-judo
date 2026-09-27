# Pitch — Tatame IA

## O Problema

Atletas e professores(as) de judô lidam constantemente com dúvidas pontuais: qual a ordem das faixas, como a pontuação funciona hoje, como montar uma aula, quais técnicas ensinar para iniciantes. Essa informação existe, mas está espalhada entre livros, regulamentos oficiais, vídeos e a experiência de cada professor(a) — nem sempre acessível na hora em que a dúvida surge (no meio do treino, preparando uma aula, ou estudando para uma graduação).

## A Solução

O **Tatame IA** é um assistente virtual que concentra informações essenciais do judô em uma base de conhecimento organizada e responde dúvidas de forma rápida, clara e confiável — **sem inventar informação** e **reconhecendo quando não sabe** algo, especialmente em temas sensíveis como saúde e nutrição, onde sempre direciona a pessoa a um profissional.

## Para Quem

- **Atletas**: dúvidas sobre técnicas, regras de competição, preparação mental e cuidados básicos.
- **Professores(as)/sensei**: apoio para estruturar aulas, relembrar regras atualizadas e orientar alunos(as) sobre graduação.

## Como Funciona (visão técnica simples)

1. A pessoa faz uma pergunta em linguagem natural.
2. O sistema busca na base de conhecimento os itens mais relevantes (por palavras-chave).
3. Se houver uma chave de API configurada, o contexto encontrado é enviado a um modelo de IA (Claude), que formula uma resposta natural **baseada apenas nesse contexto**.
4. Se não houver informação suficiente, o assistente admite isso e orienta a pessoa a buscar uma fonte oficial ou um profissional.

Esse é um padrão conhecido como **RAG (Retrieval-Augmented Generation)**: buscar informação confiável antes de gerar a resposta, reduzindo o risco de "alucinação" da IA.

## Valor do Projeto

- **Confiabilidade**: respostas ancoradas em uma base de conhecimento controlada, não em "achismo" do modelo.
- **Transparência**: o assistente sempre admite limites, especialmente em saúde e nutrição.
- **Simplicidade**: funciona até sem uma API de IA paga (modo offline), o que facilita testes e evolução gradual.
- **Extensibilidade**: novas informações podem ser adicionadas facilmente no arquivo `base_conhecimento.json`, sem precisar mexer no código.

## Próximos Passos (Roadmap)

- Ampliar a base de conhecimento (mais técnicas, mais regras por federação/faixa etária);
- Criar uma interface web simples (chat) além da versão de linha de comando;
- Permitir upload de regulamentos oficiais em PDF para enriquecer a base automaticamente;
- Adicionar suporte a múltiplos idiomas para federações internacionais;
- Testes automatizados e feedback estruturado de usuários reais (atletas e professores).

## Uma Frase de Resumo

**"Tatame IA é o assistente que tira dúvidas de judô com a confiabilidade de uma base de conhecimento organizada — e a honestidade de dizer 'não sei' quando necessário."**
