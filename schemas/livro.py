from pydantic import BaseModel
from typing import Optional, List
from models.livro import Livro



class LivroSchema(BaseModel):
    """ Define como um novo livro a ser inserido deve ser representado.
    """
    nome: str = "Orgulho e Preconceito"
    autor: str = 'Jane Austen'
    genero: str = 'Romance'
    status: str = 'Lido'


class LivroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura da busca com base no nome do livro.
    """
    nome: str = "Orgulho e Preconceito"
   

class AutorBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura da busca com base no autor do livro.
    """
    autor: str = "Jane Austen"


class ListagemLivrosSchema(BaseModel):
    """ Define como uma listagem de livros será retornada.
    """
    livros:List[LivroSchema]


def apresenta_livros(livros: List[Livro]):
    """ Retorna uma representação do livro seguindo o schema definido em LivroViewSchema.
    """
    result = []
    for livro in livros:
        result.append({
            "nome": livro.nome,
            "autor": livro.autor,
            "genero": livro.genero,
            "status": livro.status        
            })

    return {"livros": result}


class LivroViewSchema(BaseModel):
    """ Define como um livro será retornado.
    """
    id: int = 1
    nome: str = "Orgulho e Preconceito"
    autor: str = "Jane Austen"
    genero: str = "Romance"
    status: str = "Lido"



class LivroDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    message: str
    nome: str

def apresenta_livro(livro: Livro):
    """ Retorna uma representação do livro seguindo o schema definido em LivroViewSchema.
    """
    return {
        "id": livro.id,
        "nome": livro.nome,
        "autor": livro.autor,
        "genero": livro.genero,
        "status": livro.status
    }
