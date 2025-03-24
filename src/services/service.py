from sqlalchemy.orm import Session
from connection import SessaoLocal 
from model.tarefa import Tarefa  


# Criar uma nova tarefa no banco de dados
def criar_tarefa(descricao: str):
    sessao = SessaoLocal()
    nova_tarefa = Tarefa(descricao=descricao, status=False)
    sessao.add(nova_tarefa)
    sessao.commit()
    sessao.refresh(nova_tarefa)  # Atualiza com o ID gerado
    sessao.close()
    return nova_tarefa

# Obter todas as tarefas do banco de dados
def listar_tarefas():
    sessao = SessaoLocal()
    tarefas = sessao.query(Tarefa).all()
    sessao.close()
    return tarefas

# Atualizar uma tarefa existente
def editar_tarefa(tarefa_id: int, nova_descricao: str):
    sessao = SessaoLocal()
    tarefa = sessao.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if tarefa:
        tarefa.descricao = nova_descricao
        sessao.commit()
    sessao.close()

# Marcar tarefa como concluída/não concluída
def alternar_status_tarefa(tarefa_id: int, concluida: bool):
    sessao = SessaoLocal()
    tarefa = sessao.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if tarefa:
        tarefa.status = concluida
        sessao.commit()
    sessao.close()

# Remover uma tarefa do banco de dados
def deletar_tarefa(tarefa_id: int):
    sessao = SessaoLocal()
    tarefa = sessao.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if tarefa:
        sessao.delete(tarefa)
        sessao.commit()
    sessao.close()