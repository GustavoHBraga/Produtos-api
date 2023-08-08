from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool

produtos = [
    Produto(id=1, nome="Notebook", preco=1000.0, em_oferta=False),
    Produto(id=2, nome="Mouse", preco=50.25, em_oferta=True),
    Produto(id=3, nome="Teclado", preco=100.11, em_oferta=False),
    Produto(id=4, nome="Monitor", preco=500.0, em_oferta=True),
    Produto(id=5, nome="Impressora", preco=800.0, em_oferta=False),
]

def buscarProdutos(id):
    return next((produto for produto in produtos if produto.id == id), None)

# Create the FastAPI instance
app = FastAPI()

# Create a routes
@app.get("/")
async def index():
    return {"message": "Hello World!"}

@app.get("/produtos/{id}")
async def buscar_produto(id: int):
    return buscarProdutos(id)

@app.put("/produtos/{id}")
def atualizarProduto(id: int, produto: Produto ):
    prod = buscarProdutos(id)
    prod = produto
    return prod