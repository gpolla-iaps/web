from nicegui import app, ui
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from login import login_page
from main_page import main_page

from page_admin import admin_page
from page_forwarder import forwarder_page
from page_transporte import transporte_page




# Middleware de autenticación
class AuthMiddleware(BaseHTTPMiddleware):
    """Middleware para restringir el acceso a las páginas de NiceGUI."""

    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get('authenticated', False):
            if not request.url.path.startswith('/_nicegui') and request.url.path not in ['/login', '/registrar']:
                app.storage.user['referrer_path'] = request.url.path  # recordar a dónde quería ir el usuario
                return RedirectResponse('/login')
        return await call_next(request)

app.add_middleware(AuthMiddleware)

# Registrar las páginas usando decoradores
@ui.page('/')
def main():
    main_page()  # Llamar a la función que define la página principal

@ui.page('/login')
def login():
    login_page()  # Llamar a la función que define la página de inicio de sesión
 
#@ui.page('/registrar')  # Registrar la nueva página de registro
#def registrar():
#    registrar_page()

@ui.page('/admin')
def admin():
    admin_page()  # Llamar a la función que define la subpágina


@ui.page('/forwarder')
def forwarder():
    forwarder_page()  # Llamar a la función que define la subpágina


@ui.page('/transporte')
def transporte():
    transporte_page()  # Llamar a la función que define la subpágina


if __name__ in {'__main__', '__mp_main__'}:
    ui.run(storage_secret='ESTO_DEBE_CAMBIARSE')  # Cambiar a ui.run()
