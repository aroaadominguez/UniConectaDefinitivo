from PyQt5.QtWidgets import QMessageBox
from src.modelo.dao.UsuarioDAO import UsuarioDAO
from src.modelo.LoginLogica import LoginLogica
from src.vista.Tablon import Tablon
from src.controlador.ControladorTablon import ControladorTablon
from src.vista.TablonAdmin import TablonAdmin
from src.controlador.ControladorTablonAdmin import ControladorTablonAdmin

class ControladorLogin:
    def __init__(self, vista):
        self._vista = vista
        self.vista_principal = None
        self.ventana_tablon = None
        self.usuario_dao = UsuarioDAO()
        self.logica = LoginLogica(self.usuario_dao)

        # Conectar las señales de la vista
        self._vista.aceptar_clicked.connect(self.on_login_clicked)
        self._vista.volver_clicked.connect(self.on_volver_clicked)
        self._vista.recuperar_clicked.connect(self.on_recuperar_clicked)

    def set_pagina_principal(self, vista_principal):
        self.vista_principal = vista_principal

    def on_login_clicked(self):
        correo = self._vista.iniciarSesion_correo.text()
        contraseña = self._vista.iniciarSesion_contrasena.text()

        exito, tipo_usuario = self.logica.autenticar_usuario(correo, contraseña)
        if exito:
            if tipo_usuario == "estudiante":
                self.ventana_tablon = Tablon()
                self.controlador_tablon = ControladorTablon(self.ventana_tablon, correo)
                self.ventana_tablon.show()
            elif tipo_usuario == "administrador":
                self.ventana_admin = TablonAdmin()
                self.controlador_admin = ControladorTablonAdmin(self.ventana_admin, correo)
                self.ventana_admin.show()
            else:
                self.mostrar_mensaje_error("Error", "Tipo de usuario desconocido.")
                return
            self._vista.close()
        else:
            self.mostrar_mensaje_error("Error de autenticación", tipo_usuario)

    def on_volver_clicked(self):
        if self.vista_principal is not None:
            self.vista_principal.show()
        self._vista.close()

    def on_recuperar_clicked(self):
        correo = self._vista.iniciarSesion_correo.text()
        print(f"Recuperar contraseña para: {correo}")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Recuperación de contraseña")
        msg.setText(f"Para recuperar su contraseña asociada a {correo}, por favor pase por secretaría.")
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QLabel {
                color: black;
                font-size: 13px;
            }
            QPushButton {
                background-color: #d32f2f;
                color: white;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #b71c1c;
            }
        """)
        msg.exec_()

    def mostrar_mensaje_error(self, titulo, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QLabel {
                color: black;
                font-size: 13px;
            }
            QPushButton {
                background-color: #d32f2f;
                color: white;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #b71c1c;
            }
        """)
        msg.exec_()
