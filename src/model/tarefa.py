from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from connection import engine  # Importar a conexão

# Criar a base declarativa
Base = declarative_base()

# Definir o modelo da tabela
class Tarefa(Base):
    __tablename__ = "tb_enzo_netto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(255), nullable=False)
    status = Column(Boolean, default=False)

# Criar a tabela no banco de dados (caso ainda não exista)
Base.metadata.create_all(engine)