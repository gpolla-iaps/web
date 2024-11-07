from nicegui import app
from nicegui import ui
from pymongo import MongoClient

from bson import ObjectId  # Para manejar el ID de MongoDB
from data import *
import time


client = MongoClient(uri)
db = client[cliente]


ui.add_head_html('''
<style>
    .left-align-cell .q-table__row .q-td {
        text-align: left !important;
    }
</style>
''')



selected_rows = []


def admin_page() -> None:
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

        
        
        ui.button('salir', on_click = lambda: edit_dialog.close())  # Puedes agregar lógica para guardar aquí





    def def_logout() -> None:
        app.storage.user.clear()
        ui.navigate.to('/login')


    # Función para abrir el diálogo con los valores de la fila seleccionada
    def open_edit_dialog():
        selected_rows = table.selected
        if selected_rows:
            row_id = selected_rows[0]['id']  # Obtener el 'id' de la primera fila seleccionada
            # Consultar en MongoDB usando el ID de la fila seleccionada
            #usuario = collection.find_one({"_id": ObjectId(row_id)})
            
            usuario = True
            # Llenar los inputs con los datos del usuario consultado
            if usuario:
                datos_personales_nombre.value = usuario.get("Tipo_usuario", "")
                datos_personales_nombre.value = usuario.get("Nombre", "")
                datos_personales_apellido.value = usuario.get("Apellido", "")
                datos_personales_mail.value = usuario.get("Mail", "")
                datos_personales_cuit.value = usuario.get("Cuit_rut", "")
                datos_personales_direccion.value = usuario.get("Dirección", "")
                datos_personales_telefono.value = usuario.get("Teléfono", "")
                datos_personales_usuario.value = usuario.get("Usuario", "")

                tipo_usuario_habilitado.value = usuario.get("Permiso", "")
                tipo_usuario_suscripción.value = usuario.get("Vencimineto_permiso", "")

                edit_dialog.open()  # Abrir el diálogo con los datos cargados











    with ui.splitter(value = 12).style('height: 95vh;').classes('w-full') as splitter:
        with splitter.before:
            with ui.tabs(on_change = lambda tab: def_logout() if tab.value == 'Salir' else None).props('vertical').classes('w-full h-full') as tabs:
                operaciones = ui.tab('Operaciones', icon = 'settings').classes('text-white')
                usuarios = ui.tab('Usuarios', icon = 'group').classes('text-white')
                clientes = ui.tab('Clientes', icon = 'person').classes('text-white')
                despachante = ui.tab('Despachantes', icon = 'local_shipping').classes('text-white')
                exportador = ui.tab('Exportadores', icon = 'public').classes('text-white')
                logout = ui.tab('Salir', icon = 'logout').classes('text-white')
     



        with splitter.after:
            with ui.tab_panels(tabs, value = operaciones) \
                .props('vertical').classes('w-full h-full'):
        
                # Operaciones
                with ui.tab_panel(operaciones).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Operaciones').classes('text-h4 text-white')



                # Usuarios
                with ui.tab_panel(usuarios).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Usuarios').classes('text-h4 text-white')

                    collection = db[db_usuario]

                    with ui.row().classes('w-full justify-end'):
                        #ui.button(icon="edit") \
                        ui.button(on_click = open_edit_dialog, icon = 'edit') \
                            .props('outline round')


                        #ui.button(on_click = dialog_cambiar_password.close, icon = 'close') \
                        ui.button(icon = "delete") \
                            .props('outline round')
                    
                    # Generación de filas para la tabla de usuarios
                    rows = [
                        {
                            "id": str(usuario.get("_id")),  # Agregar el ID de MongoDB
                            "Tipo usuario": usuario.get("Tipo_usuario", ""),
                            "Nombre": usuario.get("Nombre", ""),
                            "Apellido": usuario.get("Apellido", ""),
                            "Mail": usuario.get("ail", ""),
                            "Cuit": usuario.get("Cuit_rut", ""),
                            "Dirección": usuario.get("Dirección", ""),
                            "Teléfono": usuario.get("Teléfono", ""),
                            "Usuario": usuario.get("Usuario", ""),

                            "Permiso": usuario.get("Permiso", ""),
                            "Vencimiento permiso": usuario.get("Vencimiento_permiso", ""),
                        }
                        for usuario in collection.find()
                    ]

                    columns = [
                            {'name': 'Tipo usuario', 'label': 'Tipo usuario', 'field': 'Tipo usuario'},
                            {'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
                            {'name': 'Apellido', 'label': 'Apellido', 'field': 'Apellido'},
                            {'name': 'Mail', 'label': 'Mail', 'field': 'Mail'},
                            {'name': 'Cuit', 'label': 'Cuit', 'field': 'Cuit'},
                            {'name': 'Dirección', 'label': 'Dirección', 'field': 'Dirección'},
                            {'name': 'Teléfono', 'label': 'Teléfono', 'field': 'Teléfono'},
                            {'name': 'Usuario', 'label': 'Usuario', 'field': 'Usuario'},
                    ]

                    with ui.table(columns = columns, rows = rows, selection = 'multiple', pagination = 10) \
                        .classes('w-full') as table:

                        pass



                # Clientes
                with ui.tab_panel(clientes).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Clientes').classes('text-h4 text-white')



                # Despachantes
                with ui.tab_panel(despachante).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Despachante').classes('text-h4 text-white')

                    collection = db[db_despachantes]

                    with ui.row().classes('w-full justify-end'):
                        ui.button(icon = "edit") \
                            .props('outline round')


                        #ui.button(on_click = dialog_cambiar_password.close, icon = 'close') \
                        ui.button(icon = "delete") \
                            .props('outline round')

                    rows = [
                        {
                            "id": str(usuario.get("_id")),  # Agregar el ID de MongoDB
                            "Nombre": usuario.get("Nombre", ""),
                        }
                        for usuario in collection.find()
                    ]

                    columns = [
                            {'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
                    ]

                    with ui.row().classes('w-full justify-center'):
                        with ui.table(columns = columns, rows = rows, selection = 'multiple', pagination = 6) \
                            .classes('w-[60%]') as table:
                            pass



                # Exportadores
                with ui.tab_panel(exportador).style('background-color: #383c5c').classes('w-full h-full'):
                    ui.label('Exportadores').classes('text-h4 text-white')

                    collection = db[db_exportadores]

                    with ui.row().classes('w-full justify-end'):
                        ui.button(icon = "edit") \
                            .props('outline round')


                        #ui.button(on_click = dialog_cambiar_password.close, icon = 'close') \
                        ui.button(icon = "delete") \
                            .props('outline round')

                    rows = [
                        {
                            "id": str(usuario.get("_id")),  # Agregar el ID de MongoDB
                            "Nombre": usuario.get("Nombre", ""),
                        }
                        for usuario in collection.find()
                    ]

                    columns = [
                            {'name': 'Nombre', 'label': 'Nombre', 'field': 'Nombre'},
                    ]

                    with ui.row().classes('w-full justify-center'):
                        with ui.table(columns = columns, rows = rows, selection = 'multiple', pagination = 6) \
                            .classes('w-[60%]') as table:
                            pass



                with ui.tab_panel(logout).style('background-color: #1c1e33'):
                    pass
