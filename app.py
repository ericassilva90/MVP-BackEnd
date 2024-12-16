from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from models import Session, Livro
from flask_cors import CORS
from schemas import *

info = Info(title="Minha Estante", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo as tags que separam as categorias
home_tag = Tag(name="Documentação", description="Seleção de documentação")
livro_tag = Tag(name="Livros", description="Adição, visualização e remoção de livros à base de dados")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/adicionar_livro', tags=[livro_tag],
          responses={"200": LivroViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: LivroSchema):
    """Adiciona um novo Livro à base de dados.
    """
    livro = Livro(
        nome=form.nome,
        autor=form.autor,
        genero=form.genero,
        status=form.status)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(livro)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_livro(livro), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Livro de mesmo nome já salvo na base de dados!"
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo livro!"
        return {"message": error_msg}, 400


@app.get('/lista_livros', tags=[livro_tag],
         responses={"200": ListagemLivrosSchema, "404": ErrorSchema})
def get_livros():
    """Faz a busca por todos os Livros cadastrados.
    """
    
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    livros = session.query(Livro).all()

    if not livros:
        # se não há produtos cadastrados
        return {"produtos": []}, 200
    else:
        # retorna a representação de produto
        print(livros)
        return apresenta_livros(livros), 200


@app.get('/busca_livro', tags=[livro_tag],
         responses={"200": LivroViewSchema, "404": ErrorSchema})
def get_livro(query: LivroBuscaSchema):
    """Faz a busca a partir do nome do livro.
    """
    livro_nome = query.nome
    
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    livro = session.query(Livro).filter(Livro.nome == livro_nome).first()

    if not livro:
        # se o produto não foi encontrado
        error_msg = "Livro não encontrado na base de dados!"
        
        return {"message": error_msg}, 404
    else:
        
        # retorna a representação de produto
        return apresenta_livro(livro), 200
    



@app.get('/busca_autor', tags=[livro_tag],
          responses={"200": LivroViewSchema, "404": ErrorSchema})
def get_autor(query: AutorBuscaSchema):

    """Faz a busca por um Livro a partir do nome do autor"""

    livro_autor = query.autor

    # Criando conexão com a base
    session = Session()
    # Fazendo a busca pelo nome do autor
    livro = session.query(Livro).filter(Livro.autor == livro_autor).first()

    if not livro:
        # Se o livro não foi encontrado
        error_msg = "Livro do autor não encontrado na base de dados!"
        return {"message": error_msg}, 404
    else:
        # Retorna a representação do livro
        return apresenta_livro(livro), 200
    


@app.delete('/deletar_livro', tags=[livro_tag],
            responses={"200": LivroDeleteSchema, "404": ErrorSchema})
def del_livro(query: LivroBuscaSchema):
    """Deleta um Livro a partir do nome informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    livro_nome = unquote(unquote(query.nome))
    print(livro_nome)
    
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Livro).filter(Livro.nome == livro_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        
        return {"message": "Produto removido", "id": livro_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base de dados!"
        
        return {"message": error_msg}, 404


