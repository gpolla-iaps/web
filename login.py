from nicegui import app, ui
from typing import Optional
from fastapi import Request
from fastapi.responses import RedirectResponse

from data import *

from pymongo import MongoClient
from datetime import datetime
import random
import string
from bson import ObjectId

client = MongoClient(uri)
db = client[cliente]
collection = db[db_usuario]


def login_user(user_id):
    app.storage.user.update({
        "user_id": user_id,
        "authenticated": True
    })


def login_page() -> Optional[RedirectResponse]:
    ui.query('body').style('background-color: #1c1e33')
    

    dialog_olvidar_password = ui.dialog() # Definir el diálogo
    dialog_cambiar_password = ui.dialog()
    dialog_registrar_usuario = ui.dialog()





#############################################################################################################
# Función, ¿No tienes cuenta? Regístrate aquí'
#############################################################################################################
    def def_registrar_usuario():
        def set_selected(item_text):
            #Cambiamos el texto del botón al valor seleccionado
            usuario_tipo.text = item_text
            usuario_tipo.update()  # Actualizamos el botón para que muestre el nuevo texto
        
        
        def def_registrar_nuevo_usuario():
            if usuario_contraseña.value == usuario_contraseña_confir.value:
                
                usuario = {
                    "Tipo_usuario": usuario_tipo.text,
                    "Nombre": usuario_nombre.value,
                    "Apellido": usuario_apellido.value,
                    "Mail": usuario_mail.value,
                    "Cuit_rut": usuario_cuit_rut.value,
                    "Dirección": usuario_direccion.value,
                    "Teléfono": usuario_telefono.value,
                    "Usuario": usuario_usuario.value,
                    "Contraseña": usuario_contraseña.value,
                    "Permiso": "0",
                    "Vencimiento_permiso": ""
                }
                collection.insert_one(usuario)  # Insertar el documento en la colección

                dialog_registrar_usuario.close()
                #fecha_hora_actual = datetime.now()

                # Separar la fecha y la hora en diferentes variables
                #fecha_actual = fecha_hora_actual.strftime("%d/%m/%Y")  # Formato DD/MM/AAAA
                #hora_actual = fecha_hora_actual.strftime("%H:%M")      # Formato HH:MM
                
                #def_enviar_correo_nuevo_usuario(usuario_mail.value, usuario_nombre.value, usuario_apellido.value, fecha_actual, hora_actual, dialog_registrar_usuario)
            else:
                ui.notify("Las contraseñas no coinciden. Por favor, verifica que ambas coincidan e inténtalo de nuevo.", color = "negative")


        with dialog_registrar_usuario:  # Construir el contenido del diálogo
            with ui.card() \
                .style('background-color: #25273e; padding: 15px; border-radius: 20px;') \
                .classes("absolute-center"):


                ui.add_head_html('''
                    <style>
                        /* Estilo específico para el ícono de mostrar/ocultar contraseña en color verde */
                        .q-field__append .q-icon {
                            color: rgb(255, 255, 255) !important;  /* Cambia a verde el ícono */
                        }
                    </style>
                ''')

                ui.label("Registro de usuario") \
                    .classes("w-full text-center text-2xl mb-4") \
                    .style("color: white")


                with ui.dropdown_button("Forwarder", auto_close = True) \
                    .props("class=w-full text-left") as usuario_tipo:
                    
                    ui.item("Forwarder", on_click = lambda: set_selected("Forwarder"))
                    ui.item("Transporte", on_click = lambda: set_selected("Transporte"))


                with ui.row():
                    usuario_nombre = ui.input(placeholder = "Nombre") \
                        .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense')
                    
                    usuario_apellido = ui.input(placeholder = "Apellido") \
                        .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense')
        
                usuario_mail = ui.input(placeholder = "Mail") \
                    .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                    .classes('w-full')
        
                usuario_cuit_rut = ui.input(placeholder = "Cuit") \
                    .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                    .classes('w-full')
                
                usuario_direccion = ui.input(placeholder = "Dirección") \
                    .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                    .classes('w-full')
                
                usuario_telefono = ui.input(placeholder = "Teléfono") \
                    .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                    .classes('w-full')
                
                usuario_usuario = ui.input(placeholder = "Usuario", validation = lambda value: 'Demasiado corto' if len(value) < 10 else None) \
                    .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                    .classes('w-full')
                
                usuario_contraseña = ui.input(placeholder = "Contraseña", validation = lambda value: 'Demasiado corto' if len(value) < 8 else None, password = True, password_toggle_button = True) \
                    .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                    .classes('w-full')

                usuario_contraseña_confir = ui.input(placeholder = "confirmar contraseña", validation = lambda value: 'Demasiado corto' if len(value) < 8 else None, password = True, password_toggle_button = True) \
                    .props('rounded outlined dense') \
                    .props('input-style="color: white"') \
                    .style('--q-password-toggle-icon-color: rgb(255, 255, 255);') \
                    .classes('w-full')
                

                ui.button('Registrar', on_click = def_registrar_nuevo_usuario) \
                    .props('color=red text-white') \
                    .style('border-radius: 10px') \
                    .classes('mt-4 w-full')
                

                with ui.row().classes('w-full justify-end'):
                    ui.button(on_click = dialog_registrar_usuario.close, icon = 'close') \
                        .props('outline round') \


        dialog_registrar_usuario.open()






#############################################################################################################
# Función, ¿Olvidaste tu contraseña?
#############################################################################################################
    def def_olvidar_password():

        def def_ui_button_search():
            def_buscar_usuario(usuario_mail.value)
        

        def def_buscar_usuario(mail_usuario_cambiar_password):
            def def_guardar_nuevo_pass():
                if  password_nuevo.value == password_nuevo_conf.value and codigo_verificacion.value == cadena_aleatoria:
                    usuarios_collection = db[db_usuario]  # Nombre de la colección
                    user_id = usuario['_id']

                    criterio = {"_id": ObjectId(user_id)}

                    nuevos_valores = {"$set": {"Contraseña": password_nuevo.value}}
                    
                    resultado = usuarios_collection.update_one(criterio, nuevos_valores)

                    if resultado.matched_count > 0:
                        ui.notify("Documento actualizado correctamente.", color = "negative")

                    dialog_cambiar_password.close
                else:
                    ui.notify("Las contraseñas o el codigo de verificación no coinciden. Por favor, verifica que ambas coincidan e inténtalo de nuevo.", color = "negative")


            def def_verificar_y_guardar():
                if password_nuevo.value != "":
                    def_guardar_nuevo_pass()


            usuario = collection.find_one({"Mail": mail_usuario_cambiar_password})

            if usuario:
                cadena_aleatoria = ''.join(random.choice(string.digits) for _ in range(6))

                #def_enviar_correo_codigo(usuario_mail.value, cadena_aleatoria)

                with dialog_cambiar_password:  # Construir el contenido del diálogo
                    with ui.card() \
                        .style('background-color: #25273e; padding: 15px; border-radius: 20px;') \
                        .classes('absolute-center'):
                        
                        ui.label("Tu cuenta se encuentra registrada") \
                            .classes("w-full text-center text-2xl mb-4") \
                            .style("color: white")
                        

                        ui.label("Se ha mandado un correo a la siguiente ceunta") \
                            .classes("w-full text-center") \
                            .style("color: white;")


                        ui.label(mail_usuario_cambiar_password) \
                            .classes("w-full text-center") \
                            .style("color: white;")


                        codigo_verificacion = ui.input(placeholder = "Código de verificación", validation = lambda value: 'Demasiado corto' if len(value) < 6 else None) \
                            .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                            .classes('w-full')


                        password_nuevo = ui.input(placeholder = "Contraseña", validation = lambda value: 'Demasiado corto' if len(value) < 8 else None, password = True, password_toggle_button = True) \
                            .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                            .classes('w-full')


                        password_nuevo_conf = ui.input(placeholder = "Confirmar contraseña", validation = lambda value: 'Demasiado corto' if len(value) < 8 else None, password = True, password_toggle_button = True) \
                            .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                            .classes('w-full')


                        with ui.row().classes('w-full justify-end'):
                            ui.button(on_click = def_verificar_y_guardar, icon = 'save') \
                                .props('outline round')


                            ui.button(on_click = dialog_cambiar_password.close, icon = 'close') \
                                .props('outline round')

                dialog_cambiar_password.open()

            elif usuario == None:
                ui.notify("Usuario no encontrado", color = "negative")


        # pantalla del dialog Vamos a buscar tu cuenta
        with dialog_olvidar_password:  # Construir el contenido del diálogo
            with ui.card() \
                .style('background-color: #25273e; padding: 15px; border-radius: 20px;') \
                .classes('absolute-center'):
                
                ui.label("Vamos a buscar tu cuenta") \
                    .classes("w-full text-center text-2xl mb-4") \
                    .style("color: white")


                ui.label("¿Cuál es tu correo?") \
                    .style("color: white;")


                with ui.row().classes('w-full'):
                    usuario_mail = ui.input(placeholder = "Mail") \
                        .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
                        .classes('flex-grow')  # Ocupa 70% de ancho

                    ui.button(on_click = def_ui_button_search, icon = 'search') \
                        .props('outline round') \
                        .classes('ml-2')


                with ui.row().classes('w-full justify-end'):
                    ui.button(on_click = dialog_olvidar_password.close, icon = 'close') \
                        .props('outline round')


        dialog_olvidar_password.open()  # Abrir el diálogo cuando se llama a la función





#############################################################################################################
# Función, loguearse a la web - Llama a la pantalla /main_page
#############################################################################################################
    def def_login() -> None:
        
        usuario = collection.find_one({
            "Usuario": username.value, 
            "Contraseña": password.value
        })
        
    
        if usuario:
            id = str(usuario.get("_id"))
            permiso = usuario.get("Permiso", "")
            tipo_usuario = usuario.get("Tipo_usuario", "")

            if permiso == "1":
                if tipo_usuario == "Administrador":
                    app.storage.user.update({
                        "username": username.value,
                        "authenticated": True
                    })
                    ui.navigate.to(f'/admin?username={username.value}')  # Redirigir a la subpágina después de iniciar sesión
            

                if tipo_usuario == "Forwarder":
                    login_user(id)
                    
                    ui.navigate.to(f'/forwarder?username={username.value}')  # Redirigir a la subpágina después de iniciar sesión


                if tipo_usuario == "Transporte":
                    login_user(id)

                    ui.navigate.to(f'/transporte?username={username.value}')  # Redirigir a la subpágina después de iniciar sesión
            
            elif permiso == "0":
                ui.notify("Usuario no habilitado", color = "negative")
        
        
        
        else:
           ui.notify("Usuario o contraseña incorrectos", color = "negative")


    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')  # Redirigir a la subpágina si ya está autenticado






#############################################################################################################
# Pantalla Principal
#############################################################################################################
    with ui.card() \
        .style('background-color: #25273e; padding: 15px; border-radius: 20px;') \
        .classes('absolute-center'):

        ui.add_head_html('''
            <style>
                /* Estilo específico para el ícono de mostrar/ocultar contraseña en color verde */
                .q-field__append .q-icon {
                    color: rgb(255, 255, 255) !important;  /* Cambia a verde el ícono */
                }
            </style>
        ''')

        ui.label("Inicio de sesión") \
            .classes("w-full text-center text-2xl mb-4") \
            .style("color: white;")


        username = ui.input(placeholder = "Usuario", validation = lambda value: 'Demasiado corto' if len(value) < 10 else None) \
            .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
            .classes('w-full')


        password = ui.input(placeholder = "Contraseña", validation = lambda value: 'Demasiado corto' if len(value) < 8 else None, password = True, password_toggle_button = True) \
            .on('keydown.enter', def_login) \
            .props('input-style="color: rgb(255, 255, 255)" rounded outlined dense') \
            .classes('w-full')


        ui.button('Iniciar sesión', on_click = def_login) \
            .props('color=red text-white') \
            .style('border-radius: 10px') \
            .classes('mt-4 w-full')


        ui.label("¿No tienes cuenta? Regístrate aquí") \
            .classes('w-full text-center cursor-pointer text-blue-500 underline') \
            .on('click', def_registrar_usuario) \


        ui.label("¿Olvidaste tu contraseña?") \
            .classes('w-full text-center cursor-pointer text-blue-500 underline') \
            .on('click', def_olvidar_password) \

    return None