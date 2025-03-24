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
        self.update()

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
        self.update()

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