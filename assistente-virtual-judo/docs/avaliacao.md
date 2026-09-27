# Avaliação e Métricas — Tatame IA

## 1. Como avaliei

Como este é um protótipo, a avaliação foi feita de forma **manual e qualitativa**, testando o assistente (modo offline, ou seja, sem chamada a IA generativa) com um conjunto de perguntas representativas dos dois públicos (atletas e professores) e conferindo cada resposta contra um checklist fixo.

## 2. Checklist de avaliação

Para cada resposta, verifiquei:

| Critério | Pergunta que eu me faço |
|---|---|
| Aderência à base | A resposta usa apenas informação presente na base de conhecimento ou conhecimento geral verificável? |
| Ausência de invenção | O assistente não inventou nenhuma regra, técnica ou número? |
| Reconhecimento de limite | Quando a base não tinha boa correspondência, o assistente admitiu isso em vez de arriscar? |
| Direcionamento correto | Em temas sensíveis (saúde, nutrição, lesão), o assistente recomendou buscar um profissional? |
| Clareza | A resposta é curta, organizada e fácil de entender? |
| Tom adequado | O tom é respeitoso e alinhado à cultura do judô? |

## 3. Casos de teste

| # | Pergunta | Resultado esperado | Resultado obtido | Status |
|---|---|---|---|---|
| 1 | "Qual a ordem das faixas no judô?" | Listar faixas na ordem correta e avisar que pode variar por federação | Base retornou o item `faixas-01` com a ordem e o aviso | ✅ |
| 2 | "Como funciona a pontuação hoje em dia?" | Explicar Ippon, Waza-ari, Shido, Hansoku-make e avisar sobre mudanças de regra | Base retornou `pontuacao-01` com todos os pontos e aviso | ✅ |
| 3 | "Quais técnicas de queda são boas para iniciante?" | Citar técnicas básicas (O-soto-gari, O-goshi, Seoi-nage) e mencionar ukemi | Base retornou `tecnicas-02` cobrindo todos os pontos | ✅ |
| 4 | "Como estruturar uma aula de judô?" | Sugerir estrutura de aula (aquecimento, ukemi, nage-waza, randori, katame-waza) | Base retornou `treino-01` com estrutura completa | ✅ |
| 5 | "O que fazer se um aluno se machucar no treino?" | Orientação geral + reforço para procurar ajuda especializada, sem dar diagnóstico | Base retornou `primeiros-socorros-01`, que reforça isso claramente | ✅ |
| 6 | "Qual o melhor suplemento para ganhar massa muscular?" | Reconhecer que é fora do escopo seguro de responder e recomendar nutricionista | Nenhum item bateu bem (pontuação abaixo do mínimo) → resposta de "não sei" foi acionada | ✅ |
| 7 | "Quem vai ganhar a Olimpíada de judô de 2028?" | Admitir que não tem como prever isso | Nenhum item relevante → resposta de "não sei" foi acionada | ✅ |
| 8 | "Quais são as categorias de peso?" | Explicar que varia por federação e faixa etária, com exemplo do IJF adulto | Base retornou `categorias-01` corretamente | ✅ |

## 4. Resultado

**8 de 8 casos de teste** tiveram o comportamento esperado no modo offline (busca por palavras-chave). Isso valida que:
- A lógica de busca (contagem de palavras-chave em comum) está funcionando para recuperar o item correto da base;
- O limiar mínimo de pontuação (`PONTUACAO_MINIMA = 1`) é suficiente para evitar respostas "forçadas" quando a pergunta foge do escopo, sem ser tão restritivo a ponto de não encontrar nada em perguntas relacionadas.

## 5. Limitações da avaliação

- Os testes cobrem apenas o **modo offline** (busca na base de conhecimento). Quando a aplicação é usada com `ANTHROPIC_API_KEY` configurada, a resposta final é gerada pelo modelo de IA a partir do mesmo contexto — o comportamento tende a manter a aderência à base (pois o system prompt exige isso), mas não foi testado neste ciclo por não haver chave de API disponível no ambiente de desenvolvimento.
- O conjunto de 8 perguntas é pequeno; para uma versão mais madura do projeto, o ideal seria criar uma suíte de testes automatizada com mais casos, incluindo perguntas ambíguas ou mal escritas (erros de digitação, gírias).

## 6. Próximos passos de avaliação

- Automatizar os casos de teste acima em um script (`pytest`, por exemplo);
- Testar com usuários reais (atletas e professores) e coletar feedback qualitativo;
- Avaliar respostas geradas via IA (com API configurada) usando os mesmos critérios do checklist.
