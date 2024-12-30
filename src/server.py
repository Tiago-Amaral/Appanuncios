from fastapi import FastAPI, Depends, HTTPException
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto


criar_bd()
app= FastAPI()


@app.post('/produtos')
def criar_produtos(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.put('/produtos/{produto_id}')
def editar_produto(produto_id: int, produto: schemas.Produto, db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    produto_atualizado = repositorio.editar(produto_id, produto)
    
    if not produto_atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto_atualizado

# Rota para deletar produtos
@app.delete('/produtos/{produto_id}')
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    repositorio = RepositorioProduto(db)
    produto_existente = repositorio.obter(produto_id)
    if not produto_existente:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    repositorio.remover(produto_id)
    return {"detail": "Produto removido com sucesso"}                   