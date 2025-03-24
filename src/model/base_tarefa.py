import flet as ft

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
