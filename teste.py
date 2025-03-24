import flet as ft
'''
class Task(ft.Row):
    def __init__(self, text, remove_task_callback):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.Icons.SAVE, on_click=self.save
        )
        self.delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=self.delete)
        self.remove_task_callback = remove_task_callback
        
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()
    
    def delete(self, e):
        self.remove_task_callback(self)

def main(page: ft.Page):
    task_list = ft.Column()
    task_input = ft.TextField(hint_text="Adicionar nova tarefa")
    
    def add_task(e):
        if task_input.value.strip():
            task_list.controls.append(Task(text=task_input.value, remove_task_callback=remove_task))
            task_input.value = ""
            page.update()
    
    def remove_task(task):
        task_list.controls.remove(task)
        page.update()
    
    page.add(
        task_input,
        ft.ElevatedButton(text="Adicionar", on_click=add_task),
        task_list
    )

ft.app(target=main)
'''





'''
def main(page: ft.Page):
    page.title = "AlertDialog examples"

    def handle_close(e):
        page.close(dlg_modal)
        page.add(ft.Text(f"botao apertado: {e.control.text}"))

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("pup_up de confirmação"),
        content=ft.Text("deseja deletar a tarefa?"),
        actions=[
            ft.TextButton("Yes", on_click=handle_close),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.add(
        ft.ElevatedButton("abbrir pop up", on_click=lambda e: page.open(dlg_modal)),
    )


ft.app(main)
'''



'''
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.DataTable(
            width=700,
            bgcolor="black", # cor da tabela
            border=ft.border.all(2, "red"), # contorno da tabela
            border_radius=10, # aredondamento de canto
            vertical_lines=ft.BorderSide(3, "blue"), #linhas verticais da tabela
            horizontal_lines=ft.BorderSide(1, "green"), # linhas horisontais da tabela
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.Colors.BLACK12,
            heading_row_height=100,
            data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=[
                ft.DataColumn(
                    ft.Text("Column 1"),
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
                ft.DataColumn(
                    ft.Text("Column 2"),
                    tooltip="This is a second column",
                    numeric=True,
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
            ],
            rows=[
                ft.DataRow(
                    [ft.DataCell(ft.Text("A")), ft.DataCell(ft.Text("1"))],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                ),
                ft.DataRow([ft.DataCell(ft.Text("B")), ft.DataCell(ft.Text("tabela interativa"))]),
            ],
        ),
    )

ft.app(main)
'''
'''
import flet as ft

def main(page: ft.Page):

    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    page.add(ft.Text("Body!"))

ft.app(main)
'''


# codigos do karithon

'''
def deletar_tarefa(tarefa_id):
    session = Session()
    try:
        
        exc_tarefa = session.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
        if exc_tarefa:
            session.delete(exc_tarefa)
            session.commit()
            return f"tarefa excluida"
        else:
            return f"tarefa não encontrada"
    except Exception as e:
        # rollback
        session.rollback()
        return f"erro ao excluir tarefa {e}"
    finally:
        #fechar conexão
        ...
        
        
        
        
def on_excluir_tarefa_click(e, tarefa_id, tarefs_collum):
    excluir_tarefa(tarefa_id)
    atualizar_lista_tarefa(tarefas_colum)
'''

'''
def editar_tarefa(tarefa_id: int, novadescrição: str, nova situacao: bool):
    session = Session()
    try:
        tarafa = session.query(Tarefa).filter(Tarefa.id == tarefa_id).first
        
        if not tarefa:
            return "tarefa não encontrada"
        
        tarefa.descricao = nova_descricao
        tarefa.situacao = nova_situacao
        
        session.commit()
        
    except Exception as e:
        session.rollback()
        return f"erro ao editar tarefa {e}"
    
    finally:
        session.close()
'''

'''
def modal_editar(page, tarefa, tarefas_colum):
    descricao_input = ft.Textfild(label= "nova descricao", value=tarefa.descricao)
    situacao_input = ft.Checbox(label= "comcluida", value=tarefa.situacao)
    
    def salcar_edicao(e):
        editar_tarefa(tarefa_id, descricao_input.value, situacao_input.value)
        page.dialog.open = False
        page.update()
        atualizar_lista_tarefas(tarefas_colum)
        
    modal = ft.AlertDialog(
        title= ft.Text("editar tarefa")
        content= ft.Colum([
            descricao_input,
            situacao_input
        ]),
        actions=[
            ft.
        ]
    )
'''




import flet as ft
from services.service import (
    criar_tarefa,
    listar_tarefas,
    editar_tarefa,
    alternar_status_tarefa,
    deletar_tarefa
)

class TarefaUI(ft.Row):
    def __init__(self, tarefa_id, descricao, concluida, remover_callback, status_callback):
        super().__init__()
        self.tarefa_id = tarefa_id
        self.status = concluida
        self.texto_visivel = ft.Text(descricao)
        self.campo_edicao = ft.TextField(value=descricao, visible=False)
        self.checkbox = ft.Checkbox(value=concluida, on_change=self.alternar_status)
        self.botao_editar = ft.IconButton(icon=ft.icons.EDIT, on_click=self.editar)
        self.botao_salvar = ft.IconButton(icon=ft.icons.SAVE, on_click=self.salvar, visible=False)
        self.botao_deletar = ft.IconButton(icon=ft.icons.DELETE, on_click=self.deletar)
        self.remover_callback = remover_callback
        self.status_callback = status_callback

        self.controls = [
            self.checkbox,
            self.texto_visivel,
            self.campo_edicao,
            self.botao_editar,
            self.botao_salvar,
            self.botao_deletar,
        ]

    def editar(self, e):
        self.botao_editar.visible = False
        self.botao_salvar.visible = True
        self.texto_visivel.visible = False
        self.campo_edicao.visible = True
        self.update()

    def salvar(self, e):
        if self.campo_edicao.value.strip():
            editar_tarefa(self.tarefa_id, self.campo_edicao.value)
            self.texto_visivel.value = self.campo_edicao.value
        self.texto_visivel.visible = True
        self.campo_edicao.visible = False
        self.botao_editar.visible = True
        self.botao_salvar.visible = False
        self.update()

    def alternar_status(self, e):
        self.status = self.checkbox.value
        alternar_status_tarefa(self.tarefa_id, self.status)
        self.status_callback()
        self.update()

    def deletar(self, e):
        deletar_tarefa(self.tarefa_id)
        self.remover_callback(self)

class ListaTarefas(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.page.title = "Lista de Tarefas"

        self.entrada_tarefa = ft.TextField(hint_text="O que precisa ser feito?", expand=True)
        self.botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=self.adicionar_tarefa)
        self.lista_tarefas = ft.Column()
        self.tarefas_ativas = ft.Text("0 tarefas ativas")

        self.controls = [
            ft.Row([self.entrada_tarefa, self.botao_adicionar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            self.lista_tarefas,
            self.tarefas_ativas
        ]
        self.carregar_tarefas()

    def carregar_tarefas(self):
        self.lista_tarefas.controls.clear()
        for tarefa in listar_tarefas():
            tarefa_ui = TarefaUI(tarefa.id, tarefa.descricao, tarefa.status, self.remover_tarefa, self.atualizar_status)
            self.lista_tarefas.controls.append(tarefa_ui)
        self.atualizar_status()

    def adicionar_tarefa(self, e):
        if self.entrada_tarefa.value.strip():
            nova_tarefa = criar_tarefa(self.entrada_tarefa.value)
            tarefa_ui = TarefaUI(nova_tarefa.id, nova_tarefa.descricao, nova_tarefa.status, self.remover_tarefa, self.atualizar_status)
            self.lista_tarefas.controls.append(tarefa_ui)
            self.entrada_tarefa.value = ""
            self.atualizar_status()

    def remover_tarefa(self, tarefa):
        self.lista_tarefas.controls.remove(tarefa)
        deletar_tarefa(tarefa.tarefa_id)
        self.atualizar_status()

    def atualizar_status(self):
        count = sum(1 for t in self.lista_tarefas.controls if not t.status)
        self.tarefas_ativas.value = f"{count} tarefa(s) ativa(s)"
        self.page.update()

class PaginaPesquisa(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.entrada_pesquisa = ft.TextField(
            hint_text="Pesquisar por ID ou Descrição",
            expand=True,
            on_change=self.pesquisar_tarefa
        )
        self.botao_pesquisar = ft.IconButton(icon=ft.icons.SEARCH, on_click=self.pesquisar_tarefa)

        self.tabela_tarefas = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Descrição")),
                ft.DataColumn(ft.Text("Status"))
            ],
            rows=[]
        )

        self.controls = [
            ft.Row([self.entrada_pesquisa, self.botao_pesquisar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            self.tabela_tarefas,
        ]

        self.carregar_tarefas()

    def carregar_tarefas(self):
        """Carrega todas as tarefas na tabela ao abrir a página."""
        self.tabela_tarefas.rows.clear()
        for tarefa in listar_tarefas():
            self.tabela_tarefas.rows.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(tarefa.id))),
                    ft.DataCell(ft.Text(tarefa.descricao)),
                    ft.DataCell(ft.Text("Feito" if tarefa.status else "Pendente"))
                ]
            ))
        self.page.update()

    def pesquisar_tarefa(self, e=None):
        """Filtra as tarefas baseadas no termo de pesquisa (em tempo real)."""
        termo = self.entrada_pesquisa.value.lower().strip()
        self.tabela_tarefas.rows.clear()

        for tarefa in listar_tarefas():
            if termo in str(tarefa.id) or termo in tarefa.descricao.lower():
                self.tabela_tarefas.rows.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(tarefa.id))),
                        ft.DataCell(ft.Text(tarefa.descricao)),
                        ft.DataCell(ft.Text("Feito" if tarefa.status else "Pendente"))
                    ]
                ))
        self.page.update()

def carregar_interface(page: ft.Page):
    def mudar_pagina(e):
        """Navega entre as páginas usando `page.go()`."""
        if page.navigation_bar.selected_index == 0:
            page.go("/")
        else:
            page.go("/pesquisa")

    def on_route_change(e):
        """Atualiza a interface ao mudar de rota."""
        page.views.clear()
        page.views.append(ft.View("/", controls=[page.navigation_bar]))  # Mantém a barra de navegação

        if page.route == "/":
            page.views.append(ft.View("Lista de Tarefas", controls=[ListaTarefas(page)]))
        elif page.route == "/pesquisa":
            page.views.append(ft.View("Pesquisa", controls=[PaginaPesquisa(page)]))

        page.update()

    page.on_route_change = on_route_change
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.LIST, label="Tarefas"),
            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Pesquisa"),
        ],
        on_change=mudar_pagina
    )
    page.go(page.route)  # Navega para a rota inicial
