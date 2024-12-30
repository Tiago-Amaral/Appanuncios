from sqlalchemy import Column, Integer,String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)  # Nome com 100 caracteres e não pode ser nulo
    detalhes = Column(String(255), nullable=True)  # Detalhes podem ser nulos
    preco = Column(Float, nullable=False)  # Preço não pode ser nulo
    disponivel = Column(Boolean, default=True)  # Valor padrão é True (disponível)
    