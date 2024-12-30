from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(**produto.dict())
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        return self.db.query(models.Produto).all()

    def editar(self, produto_id: int, produto: schemas.Produto):
        db_produto = self.db.query(models.Produto).filter(models.Produto.id == produto_id).first()
        if db_produto:
            for key, value in produto.dict(exclude_unset=True).items():
                setattr(db_produto, key, value)
            self.db.commit()
            self.db.refresh(db_produto)
            return db_produto
        return None

    def obter(self, produto_id: int):
        return self.db.query(models.Produto).filter(models.Produto.id == produto_id).first()

    def remover(self, produto_id: int):
        db_produto = self.db.query(models.Produto).filter(models.Produto.id == produto_id).first()
        if db_produto:
            self.db.delete(db_produto)
            self.db.commit()
