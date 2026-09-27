"""
Tatame IA — Assistente Virtual para Atletas e Professores de Judô
====================================================================

Aplicação de linha de comando (CLI) para conversar com o assistente.

Funcionamento:
1. Busca na base de conhecimento (data/base_conhecimento.json) os itens mais
   relevantes para a pergunta feita (busca simples por palavras-chave, sem
   dependências externas).
2. Se a variável de ambiente ANTHROPIC_API_KEY estiver configurada, envia a
   pergunta + o contexto recuperado para o modelo Claude, seguindo o
   system prompt definido em docs/prompts.md.
3. Se não houver chave de API configurada, funciona em "modo offline": mostra
   diretamente os itens mais relevantes da base de conhecimento, sem gerar
   texto novo. Isso permite testar a aplicação sem depender de uma API paga.

Como rodar:
    python src/app.py

Como configurar a API (opcional, para respostas mais elaboradas):
    export ANTHROPIC_API_KEY="sua-chave-aqui"      # Linux/Mac
    setx ANTHROPIC_API_KEY "sua-chave-aqui"         # Windows
"""

import json
import os
import re
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_PATH = os.path.join(BASE_DIR, "..", "data", "base_conhecimento.json")
PROMPT_PATH = os.path.join(BASE_DIR, "..", "docs", "prompts.md")

MODELO = "claude-sonnet-4-6"
MAX_TOKENS = 500
TOP_N_CONTEXTO = 3
PONTUACAO_MINIMA = 1


def carregar_base():
    """Carrega a base de conhecimento a partir do arquivo JSON."""
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def normalizar(texto):
    """Deixa o texto em minúsculas e remove pontuação para facilitar a busca."""
    texto = texto.lower()
    texto = re.sub(r"[^a-zà-úãõâêîôûáéíóúç0-9\s]", " ", texto)
    return texto


def pontuar_item(palavras_pergunta, item):
    """Conta quantas palavras da pergunta aparecem no item da base."""
    texto_item = normalizar(
        item["pergunta_exemplo"]
        + " "
        + item["categoria"]
        + " "
        + " ".join(item.get("palavras_chave", []))
    )
    palavras_item = set(texto_item.split())
    return len(palavras_pergunta & palavras_item)


def buscar_contexto(pergunta, base, top_n=TOP_N_CONTEXTO, minimo=PONTUACAO_MINIMA):
    """Retorna os itens da base mais relevantes para a pergunta."""
    palavras_pergunta = set(normalizar(pergunta).split())
    pontuados = [(pontuar_item(palavras_pergunta, item), item) for item in base]
    pontuados.sort(key=lambda par: par[0], reverse=True)
    return [item for pontuacao, item in pontuados if pontuacao >= minimo][:top_n]


def extrair_system_prompt():
    """Extrai o bloco de system prompt de dentro de docs/prompts.md."""
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        conteudo = f.read()
    inicio = conteudo.find("## System Prompt")
    bloco = conteudo[inicio:]
    partes = bloco.split("```")
    if len(partes) >= 2:
        return partes[1].strip()
    return "Você é o Tatame IA, um assistente sobre judô. Responda com base no contexto fornecido."


def montar_texto_contexto(contexto):
    if not contexto:
        return "Nenhum item da base de conhecimento teve boa correspondência com a pergunta."
    return "\n".join(f"- {item['categoria']}: {item['resposta']}" for item in contexto)


def chamar_claude(pergunta, contexto):
    """Chama a API da Anthropic, se houver chave configurada. Retorna None se falhar/não configurada."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    system_prompt = extrair_system_prompt()
    contexto_texto = montar_texto_contexto(contexto)

    corpo = {
        "model": MODELO,
        "max_tokens": MAX_TOKENS,
        "system": system_prompt,
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Contexto da base de conhecimento:\n{contexto_texto}\n\n"
                    f"Pergunta da pessoa usuária: {pergunta}"
                ),
            }
        ],
    }

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(corpo).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            dados = json.loads(resp.read().decode("utf-8"))
            textos = [b["text"] for b in dados.get("content", []) if b.get("type") == "text"]
            return "\n".join(textos).strip() or None
    except Exception as erro:
        print(f"[Aviso] Não foi possível chamar a API da Anthropic: {erro}")
        return None


def responder_modo_offline(contexto):
    """Resposta baseada diretamente na base de conhecimento, sem chamar nenhum modelo."""
    if not contexto:
        return (
            "Não encontrei informação suficiente na minha base de conhecimento para "
            "responder com segurança. Recomendo consultar um(a) professor(a)/sensei ou "
            "uma fonte oficial (ex.: CBJ, IJF)."
        )
    linhas = [
        "[Modo offline — sem chamada a modelo de IA. Configure ANTHROPIC_API_KEY para "
        "respostas mais elaboradas.]\n",
        "Aqui está o que encontrei na base de conhecimento sobre isso:\n",
    ]
    for item in contexto:
        linhas.append(f"📌 {item['categoria']}\n{item['resposta']}\n")
    return "\n".join(linhas)


def responder(pergunta, base):
    contexto = buscar_contexto(pergunta, base)
    resposta_ia = chamar_claude(pergunta, contexto)
    if resposta_ia:
        return resposta_ia
    return responder_modo_offline(contexto)


def main():
    print("=" * 64)
    print("🥋 Tatame IA — Assistente Virtual para Atletas e Professores de Judô")
    print("=" * 64)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("(Rodando em modo offline — configure ANTHROPIC_API_KEY para respostas com IA)")
    print("Digite sua pergunta sobre judô (ou 'sair' para encerrar).\n")

    base = carregar_base()

    while True:
        try:
            pergunta = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nTatame IA: Até o próximo treino! 🥋")
            break

        if pergunta.lower() in ("sair", "exit", "quit"):
            print("Tatame IA: Até o próximo treino! 🥋")
            break
        if not pergunta:
            continue

        resposta = responder(pergunta, base)
        print(f"\nTatame IA: {resposta}\n")


if __name__ == "__main__":
    main()
