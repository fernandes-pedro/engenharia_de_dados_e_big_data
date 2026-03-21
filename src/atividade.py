# =========================
# README.md
# =========================
"""
# Nome do Projeto

## 👥 Integrantes
- Pedro Fernandes Cavalcanti Ferreira
- Integrante 2
- Integrante 3

## 📌 Descrição
Projeto em Python que manipula dados JSON e SQLite.

## ▶️ Como executar
python src/aula.py

## ✅ Boas práticas
- Uso de docstrings
- Código formatado com Black
"""


# =========================
# src/aula.py
# =========================
import json
import sqlite3


def carregar_dados(caminho):
    """
    Carrega dados de um arquivo JSON.

    Args:
        caminho (str): Caminho do arquivo JSON.

    Returns:
        dict: Dados carregados.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(caminho, dados):
    """
    Salva dados em um arquivo JSON.

    Args:
        caminho (str): Caminho do arquivo.
        dados (dict): Dados a serem salvos.
    """
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)


def conectar_banco(caminho_db):
    """
    Cria conexão com banco SQLite.

    Args:
        caminho_db (str): Caminho do banco.

    Returns:
        Connection: Conexão com banco.
    """
    return sqlite3.connect(caminho_db)


def criar_tabela(conn):
    """
    Cria tabela de exemplo no banco.

    Args:
        conn: Conexão com banco
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
        """
    )
    conn.commit()


def inserir_usuario(conn, nome):
    """
    Insere um usuário no banco.

    Args:
        conn: Conexão com banco
        nome (str): Nome do usuário
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()


def main():
    """Função principal do programa."""

    dados = carregar_dados("data/data.json")

    conn = conectar_banco("data/database.db")
    criar_tabela(conn)

    for nome in dados.get("usuarios", []):
        inserir_usuario(conn, nome)

    print("Dados inseridos com sucesso!")


if __name__ == "__main__":
    main()


# =========================
# data/data.json
# =========================
"""
{
    "usuarios": [
        "Pedro",
        "Maria",
        "João"
    ]
}
"""


# =========================
# requirements.txt
# =========================
"""
black
"""


# =========================
# .gitignore
# =========================
"""
venv/
__pycache__/
*.pyc
"""
