from pydantic import BaseModel
from typing import Optional, List

    
class Produto(BaseModel):
    id: Optional[str] = ''
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    
    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id:Optional[str] = None  
    usuario: 'User' 
 
    quantidade: int
    entrega: bool = True
    endereco: str
    obs: Optional[str]  = 'Sem observações'
    
    
class User (BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
  
    
    
      