from pydantic import BaseModel

# Define uma nova classe chamada ErrorSchema que herda de BaseModel. 
# Essa classe será usada para representar uma mensagem de erro.


class ErrorSchema(BaseModel):

    """ Criado o atributo message
    """
    message: str
