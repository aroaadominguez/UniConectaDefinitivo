from src.controlador.ControladorBaseNavegableAdmin import ControladorBaseNavegableAdmin

class ControladorGestionAdmin(ControladorBaseNavegableAdmin):
    def __init__(self, vista, correo_usuario):
        super().__init__(vista, correo_usuario)
