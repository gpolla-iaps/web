from nicegui import app
from nicegui import ui
from pymongo import MongoClient

from bson import ObjectId  # Para manejar el ID de MongoDB
from data import *
import time


client = MongoClient(uri)
db = client[cliente]
collection = db[db_usuario] 

selected_rows = []


def main_page() -> None:
    ui.query('body').style('background-color: #1c1e33')

    with ui.dialog() as edit_dialog:

        with ui.row().classes('justify-center no-wrap'):  # Contenedor para alinear las tarjetas horizontalmente
            with ui.card() \
                .style('background-color: #25273e; padding: 15px; border-radius: 20px;') \
                .classes('w-64'):
                
                dialog_label = ui.label('Datos personales') \
                    .classes("w-full text-center text-2xl mb-4") \
                    .style("color: white;")
                
                datos_personales_nombre = ui.input(label = 'Nombre') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')

                datos_personales_apellido = ui.input(label='Apellido') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')
                
                datos_personales_mail = ui.input(label='Mail') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')
                
                datos_personales_cuit = ui.input(label='Cuit') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')
                
                datos_personales_direccion = ui.input(label='Dirección') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')
                
                datos_personales_telefono = ui.input(label='Teléfono') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')
                
                datos_personales_usuario = ui.input(label='Usuario') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')

            with ui.card() \
                .style('background-color: #25273e; padding: 15px; border-radius: 20px;') \
                .classes('w-64'):
            
                dialog_label = ui.label('Tipo de usuario') \
                    .classes("w-full text-center text-2xl mb-4") \
                    .style("color: white;")

                tipo_usuario_tipo = ui.input(label = 'Tipo') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')

                tipo_usuario_habilitado = ui.input(label='Habilitado') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')
                
                tipo_usuario_suscripción = ui.input(label='Suscripción') \
                    .props('input-style="color: rgb(255, 255, 255)"') \
                    .classes('w-full')


            #with ui.card() \
            #    .style('background-color: #25273e; padding: 15px; border-radius: 20px;') \
            #    .classes('w-64'):
                
            #    dialog_label = ui.label('tercer card')

        
        
        ui.button('salir', on_click=lambda: edit_dialog.close())  # Puedes agregar lógica para guardar aquí





    def def_logout() -> None:
        app.storage.user.clear()
        ui.navigate.to('/login')


    # Función para abrir el diálogo con los valores de la fila seleccionada
    def open_edit_dialog():
        selected_rows = table.selected
        if selected_rows:
            row_id = selected_rows[0]['id']  # Obtener el 'id' de la primera fila seleccionada
            # Consultar en MongoDB usando el ID de la fila seleccionada
            usuario = collection.find_one({"_id": ObjectId(row_id)})
            
            # Llenar los inputs con los datos del usuario consultado
            if usuario:
                datos_personales_nombre.value = usuario.get("datos_personales", {}).get("Nombre", "")
                datos_personales_apellido.value = usuario.get("datos_personales", {}).get("Apellido", "")
                datos_personales_mail.value = usuario.get("datos_personales", {}).get("Mail", "")
                datos_personales_cuit.value = usuario.get("datos_personales", {}).get("Cuit", "")
                datos_personales_direccion.value = usuario.get("datos_personales", {}).get("Dirección", "")
                datos_personales_telefono.value = usuario.get("datos_personales", {}).get("Teléfono", "")
                datos_personales_usuario.value = usuario.get("datos_personales", {}).get("Usuario", "")

                tipo_usuario_tipo.value = usuario.get("tipo_usuario", {}).get("Tipo", "")
                tipo_usuario_habilitado.value = usuario.get("tipo_usuario", {}).get("Habilitado", "")
                tipo_usuario_suscripción.value = usuario.get("tipo_usuario", {}).get("Suscripción", "")


                
                
                
                edit_dialog.open()  # Abrir el diálogo con los datos cargados











    with ui.splitter(value = 10).style('height: 95vh;').classes('w-full') as splitter:
        with splitter.before:
            with ui.tabs(on_change = lambda tab: def_logout() if tab.value == 'Salir' else None).props('vertical').classes('w-full h-full') as tabs:
                mail = ui.tab('Mails', icon = 'mail').classes('text-white')
                alarm = ui.tab('Alarms', icon = 'alarm').classes('text-white')
                movie = ui.tab('Movies', icon = 'movie').classes('text-white')
                users = ui.tab('Usuarios', icon='group').classes('text-white')
                logout = ui.tab('Salir', icon = 'logout').classes('text-white')
     



        with splitter.after:
            with ui.tab_panels(tabs, value = mail) \
                .props('vertical').classes('w-full h-full'):
        

                with ui.tab_panel(mail).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Mails').classes('text-h4')
                    ui.label('Content of mails')
        

                with ui.tab_panel(alarm).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Alarms').classes('text-h4')
                    ui.label('Content of alarms')
        

                with ui.tab_panel(movie).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Movies').classes('text-h4')
                    ui.label('Content of movies')


                with ui.tab_panel(users).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Movies').classes('text-h4')

                    with ui.row().classes('w-full justify-end'):
                        #ui.button(icon="edit") \
                        ui.button(on_click = open_edit_dialog, icon = 'edit') \
                            .props('outline round')


                        #ui.button(on_click = dialog_cambiar_password.close, icon = 'close') \
                        ui.button(icon="delete") \
                            .props('outline round')
                    
                    # Generación de filas para la tabla de usuarios
                    rows = [
                        {
                            "id": str(usuario.get("_id")),  # Agregar el ID de MongoDB
                            "Nombre": usuario.get("datos_personales", {}).get("Nombre", ""),
                            "Apellido": usuario.get("datos_personales", {}).get("Apellido", ""),
                            "Mail": usuario.get("datos_personales", {}).get("Mail", ""),
                            "Cuit": usuario.get("datos_personales", {}).get("Cuit", ""),
                            "Dirección": usuario.get("datos_personales", {}).get("Dirección", ""),
                            "Teléfono": usuario.get("datos_personales", {}).get("Teléfono", ""),
                            "Usuario": usuario.get("datos_personales", {}).get("Usuario", ""),
                        }
                        for usuario in collection.find()
                    ]


                    columns=[
                            {'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
                            {'name': 'Apellido', 'label': 'Apellido', 'field': 'Apellido'},
                            {'name': 'Mail', 'label': 'Mail', 'field': 'Mail'},
                            {'name': 'Cuit', 'label': 'Cuit', 'field': 'Cuit'},
                            {'name': 'Dirección', 'label': 'Dirección', 'field': 'Dirección'},
                            {'name': 'Teléfono', 'label': 'Teléfono', 'field': 'Teléfono'},
                            {'name': 'Usuario', 'label': 'Usuario', 'field': 'Usuario'},
                    ]

                    with ui.table(columns = columns, rows = rows, selection = 'multiple', pagination=10).classes('w-full') as table:
                        #table.on_select(update_selected_row)
                        
                        #with table.add_slot('top-right'):
                        pass
                        #    table.on_select(update_selected_rows)
                        #    pass
                            #ui.label().bind_text_from(table, 'selected', lambda val: f'Current selection: {val}')




                with ui.tab_panel(logout).style('background-color: #1c1e33'):
                    pass
