from sqlalchemy import Column, String, Integer
from typing import Union

from models import Base

# Criando a tabela "livro"

class Livro(Base):
    __tablename__ = 'livro'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    autor = Column(String(100))
    genero = Column(String(100))
    status = Column(String(5))


    def __init__(self, nome:str, autor:str, genero:str, status: str):
        """
        Cadastra um livro no banco de dados.

        Argumentos:
            nome: Nome do livro
            autor: Autor do livro
            genero: Gênero do livro
            status: Status de Leitura do livro
        """
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.status = status



