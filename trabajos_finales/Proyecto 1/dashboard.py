from ui_viajes_final_ui import Ui_MainWindow
from login_ui import Ui_MainWindow_login
from PyQt6 import QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os
import re
dic_usuarios = {}
class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow_login):
    def __init__(self):
        self.basedir = os.path.dirname(__file__)
        super().__init__()
        self.setupUi(self)
        #botones login
        self.button_registrate_stacked.clicked.connect(self.cambiar_a_registro)
        self.button_ver_password.pressed.connect(lambda: self.mirar_password(self.line_password_login, self.button_ver_password))
        self.button_ver_password.released.connect(lambda: self.ocultar_password(self.line_password_login, self.button_ver_password))
        self.button_inicia_sesion.clicked.connect(self.validar_login)

        #botones registro
        self.button_inicia_sesion_stacked.clicked.connect(self.cambiar_a_login)
        self.button_ver_password_registro.pressed.connect(lambda: self.mirar_password(self.line_password_registro, self.button_ver_password))
        self.button_ver_password_registro.released.connect(lambda: self.ocultar_password(self.line_password_registro, self.button_ver_password))
        self.pushButton_7.pressed.connect(lambda: self.mirar_password(self.line_password_validacion_registro, self.pushButton_7))
        self.pushButton_7.released.connect(lambda: self.ocultar_password(self.line_password_validacion_registro, self.pushButton_7))
        self.button_registrarse.clicked.connect(self.validar_registro)

        


    def cambiar_a_login(self):
        self.stackedWidget.setCurrentWidget(self.login_widget)  # Cambia a la página de inicio
        self.line_usuario_login.clear()
        self.line_password_login.clear()
        self.line_usuario_login.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_password_login.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        

    def cambiar_a_registro(self):
        self.stackedWidget.setCurrentWidget(self.singup_widget)
        self.line_nombre_registro.clear()
        self.line_apellido_registro.clear()
        self.line_email.clear()
        self.line_password_registro.clear()
        self.line_password_validacion_registro.clear()
        self.line_nombre_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_apellido_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_email.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_password_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")
        self.line_password_validacion_registro.setStyleSheet("background-color: rgba(255, 255, 255, 50%); border-bottom: 1px solid black; border-radius: 5px; color: black; height: 30px; font-size: 13px;")

    
    def mirar_password(self, line_edit, button):
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.basedir, "img_trabajos", "ojo-abierto-morado.png")))
        button.setIcon(icon)
    
    def ocultar_password(self, line_edit, button):
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.basedir, "img_trabajos", "ojo-cerrado-morado.png")))
        button.setIcon(icon)
    
    def validar_login(self):
        usuario = self.line_usuario_login.text().strip()
        contraseña = self.line_password_login.text().strip()

        if usuario and contraseña:
            if usuario in dic_usuarios:
                password = dic_usuarios[usuario][2]  # Obtener la contraseña almacenada
                if contraseña == password:
                    QtWidgets.QMessageBox.information(self,"Login Exitoso", "Has iniciado sesión correctamente.")
                    self.line_usuario_login.clear()
                    self.line_password_login.clear()
                    # self.line_usuario_login.setStyleSheet("border-color: black;")
                    # self.line_password_login.setStyleSheet("border-color: black;")
                    # implementacion para la pagina principal
                    self.main_window = MainApp()
                    self.main_window.name_edit_profile_2.setText(f"{dic_usuarios[usuario][0]}")
                    self.main_window.lastname_edit_profile_2.setText(f"{dic_usuarios[usuario][1]}")
                    self.main_window.email_edit_profile_2.setText(usuario)
                    self.main_window.pass_edit_profile_2.setText(contraseña)
                    self.main_window.show()
                    self.close()
                else:
                    self.mostrar_warning("Contraseña incorrecta.")
                    # self.line_password_login.setStyleSheet("border-color: red;")
                    return
            else:
                self.mostrar_warning("El usuario no existe.")
                # self.line_usuario_login.setStyleSheet("border-color: red;")
                return

        else:
            if not usuario:
                # self.line_usuario_login.setStyleSheet("border-color: red;")
                self.mostrar_warning("El campo de usuario no puede estar vacío.")
                return
            if not contraseña:
                # self.line_password_login.setStyleSheet("border-color: red;")
                self.mostrar_warning("El campo de contraseña no puede estar vacío.")
                return

    def validar_registro(self):
        nombre = self.line_nombre_registro.text().strip()
        apellido = self.line_apellido_registro.text().strip()
        email = self.line_email.text().strip()
        password = self.line_password_registro.text().strip()
        validacion_password = self.line_password_validacion_registro.text().strip()

        mensajes_alerta = []  # Lista para almacenar mensajes de alerta

        if not nombre:
            mensajes_alerta.append("El nombre no puede estar vacío.")

        if not apellido:
            mensajes_alerta.append("El apellido no puede estar vacío.")

        if not email:
            mensajes_alerta.append("El email no puede estar vacío.")

        if not password:
            mensajes_alerta.append("La contraseña no puede estar vacía.")

        if not validacion_password:
            mensajes_alerta.append("La verificación de contraseña no puede estar vacía.")

        if mensajes_alerta:
            self.mostrar_warning("\n".join(mensajes_alerta))
            return

        if password != validacion_password:
            self.mostrar_warning("Verifica que tus contraseñas sean iguales")
            return
        else:
            
            if self.validar_nombre_registro(self.line_nombre_registro): 
                if self.validar_apellido_registro(self.line_apellido_registro):
                    if self.validar_email_registro(self.line_email): 
                        if self.validar_password_registro(self.line_password_registro):
                            nombre = self.line_nombre_registro.text()
                            apellido = self.line_apellido_registro.text()
                            email = self.line_email.text()
                            contraseña = self.line_password_registro.text()
                            msg_box = QMessageBox()
                            msg_box.setIcon(QMessageBox.Information)
                            msg_box.setText("Cuenta creada con éxito.")
                            msg_box.setWindowTitle("Cuenta Creada")

                            # Cambiar el tamaño del QMessageBox
                            msg_box.resize(300, 200)

                            # Cambiar el estilo del botón
                            msg_box.setStyleSheet("""
                                QPushButton {
                                    min-width: 30px;
                                    min-height: 15px;
                                }
                            """)
                            dic_usuarios[email] = [nombre, apellido, contraseña]
                        

                            print(dic_usuarios)
                            ok = msg_box.exec()
                            if ok:
                                self.stackedWidget.setCurrentWidget(self.login_widget)
                            self.line_nombre_registro.clear()
                            self.line_apellido_registro.clear()
                            self.line_email.clear()
                            self.line_password_registro.clear()
                            self.line_password_validacion_registro.clear()
                            # self.line_nombre_registro.setStyleSheet("border-color: black;")
                            # self.line_apellido_registro.setStyleSheet("border-color: black;")
                            # self.line_email.setStyleSheet("border-color: black;")
                            # self.line_password_registro.setStyleSheet("border-color: black;")
                            # self.line_password_validacion_registro.setStyleSheet("border-color: black;")


    def validar_nombre_registro(self, nombre_line_edit):
        nombre = nombre_line_edit.text().strip()
        if not re.match(r'^[a-zA-Z\s]+$', nombre):
            self.mostrar_warning("El nombre no puede contener caracteres especiales ni dígitos.")
            # nombre_line_edit.setStyleSheet("border-color: red;")
            return False
        elif len(nombre.split()) > 3:
            self.mostrar_warning("No puede haber más de tres nombres.")
            # nombre_line_edit.setStyleSheet("border-color: red;")
            return False
        else:
            nombre = ' '.join(nombre.split()).title()
            nombre_line_edit.setText(nombre)
            # nombre_line_edit.setStyleSheet("border-color: green;")

            return nombre

    def validar_apellido_registro(self, apellido_line_edit):
        apellido = apellido_line_edit.text().strip()
        if not re.match(r'^[a-zA-Z\s]+$', apellido):
            self.mostrar_warning("El apellido no puede contener caracteres especiales ni dígitos.")
            # apellido_line_edit.setStyleSheet("border-color: red;")
            return False
        elif len(apellido.split()) > 3:
            self.mostrar_warning("No puede haber más de tres apellidos.")
            # apellido_line_edit.setStyleSheet("border-color: red;")
            return False
        else:
            apellido = ' '.join(apellido.split()).title()
            apellido_line_edit.setText(apellido)
            # apellido_line_edit.setStyleSheet("border-color: green;")
            return apellido

    def validar_email_registro(self, email_line_edit):
        email = email_line_edit.text()
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email.strip()):
            self.mostrar_warning("Debe colocar un email válido.")
            # email_line_edit.setStyleSheet("border-color: red;")
            return False
        # email_line_edit.setStyleSheet("border-color: green;")
        email_line_edit.setText(email)
        return email

    def validar_password_registro(self, password_line_edit):
        password = password_line_edit.text()
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_regex, password.strip()):
            self.mostrar_warning("La contraseña debe contener al menos 8 caracteres, incluyendo una letra mayúscula, una letra minúscula y un número. No se permiten caracteres especiales.")
            # password_line_edit.setStyleSheet("border-color: red;")
            return False
        # password_line_edit.setStyleSheet("border-color: green;")
        password_line_edit.setText(password)
        return password

    def mostrar_warning(self, mensaje):
        QtWidgets.QMessageBox.warning(self, "Validaciónes", mensaje)



class MainApp(QMainWindow, Ui_MainWindow):
    basedir = os.path.dirname(__file__)
    #Validaciones del perfil
    paso_foto_de_perfil = False
    paso_escoger_sexualidad = False
    paso_nombre_validado = False
    paso_apellido_validado = False
    paso_edad_validada = False
    ti_o_cc_validado = False
    direccion_validada = False
    telefono_validado = False
    edad_validada = False
    pasaporte_validado = False
    nacionalidad_validada = False
    biografia_validada = False

    pasos_totales = 9
    pasos_completados = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My travel app")


        self.menub.setHidden(True)

        self.home_small_button1.setChecked(True)
        self.mostrar_pagina_home()

        self.open_pic_to_profile_pic_2.setHidden(True)
        self.delete_profile_pic_2.setHidden(True)

        self.home_small_button1.clicked.connect(self.mostrar_pagina_home)
        self.home_small_button2.clicked.connect(self.mostrar_pagina_home)
        self.mytravels_small_button1.clicked.connect(self.mostrar_pagina_mis_viajes)
        self.mytravels_small_button2.clicked.connect(self.mostrar_pagina_mis_viajes)
        self.newtravel_small_button1.clicked.connect(self.mostrar_pagina_nuevo_viaje)
        self.newtravel_small_button2.clicked.connect(self.mostrar_pagina_nuevo_viaje)
        self.itinerary_small_button1.clicked.connect(self.mostrar_pagina_itinerario)
        self.itinerary_small_button2.clicked.connect(self.mostrar_pagina_itinerario)
        self.bills_small_button1.clicked.connect(self.mostrar_pagina_gastos)
        self.bills_small_button2.clicked.connect(self.mostrar_pagina_gastos)
        self.notify_small_button1.clicked.connect(self.mostrar_pagina_notificaciones)
        self.notify_small_button2.clicked.connect(self.mostrar_pagina_notificaciones)
        self.settings_small_button1.clicked.connect(self.mostrar_configuraciones_page)
        self.settings_small_button2.clicked.connect(self.mostrar_configuraciones_page)

        self.myprofile_button.clicked.connect(self.mostrar_pagina_perfil)
        

        #Botones de recordatorio
        self.agregar_recordatorio_nuevo.clicked.connect(self.mostrar_agregar_nuevo_recordatorio)
        self.volver_recordatorios_agregar_recordatorio_page.clicked.connect(self.mostrar_pagina_recordatorios)

        #Botones de settings
        self.suppor_button_settings.clicked.connect(self.mostrar_pagina_de_soporte)
        self.back_button_support.clicked.connect(self.mostrar_pagina_botones_configuraciones)
        self.about_us_button_settings.clicked.connect(self.mostrar_pagina_about_us)
        self.back_button_about_us.clicked.connect(self.mostrar_pagina_botones_configuraciones)

        #Botones del editar perfil
        self.open_pic_to_profile_pic_2.clicked.connect(self.cargar_foto_de_perfil)
        self.delete_profile_pic_2.clicked.connect(self.borrar_foto_de_perfil)
        self.edit_profile_2.clicked.connect(self.activar_edicion_de_perfil)

        #Grupo de botones para sexo
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.hombre_radio_profile_2)
        self.button_group.addButton(self.otro_radio_profile_2)
        self.button_group.addButton(self.mujer_radio_profile_2)
        self.button_group.addButton(self.none_radio_profile_2)
        self.button_group.buttonClicked.connect(self.validar_sexo)

        #Reloj
        self.Horas.setDigitCount(2)
        self.Horas.setSegmentStyle(QLCDNumber.Filled)
        self.minutos.setDigitCount(2)
        self.minutos.setSegmentStyle(QLCDNumber.Filled)

        self.timer_reloj = QTimer(self)
        self.timer_reloj.timeout.connect(self.update_time)
        self.timer_reloj.start(1000)

        self.actualizar_progreso()


    def activar_edicion_de_perfil(self):
        if self.edit_profile_2.text() == "Editar perfil":
            self.cargar_telefono()
            self.open_pic_to_profile_pic_2.setHidden(False)
            self.delete_profile_pic_2.setHidden(False)
            self.edit_profile_2.setText("Guardar")
            self.open_pic_to_profile_pic_2.setCheckable(True)
            self.open_pic_to_profile_pic_2.setEnabled(True)
            self.delete_profile_pic_2.setEnabled(True)
            self.delete_profile_pic_2.setCheckable(True)
            self.sexo_groupbox_profile_2.setEnabled(True)
            self.name_edit_profile_2.setEnabled(True)
            self.lastname_edit_profile_2.setEnabled(True)
            self.age_spinbox_profile_2.setEnabled(True)
            self.email_edit_profile_2.setEnabled(True)
            self.pass_edit_profile_2.setEnabled(True)
            self.id_edit_profile_2.setEnabled(True)
            self.country_edit_profile_2.setEnabled(True)
            self.passport_edit_profile_2.setEnabled(True)
            self.adress_edit_profile_2.setEnabled(True)
            self.telefono_edit_profile_3.setEnabled(True)
            self.biography_paintext_profile_2.setEnabled(True)
        else:
            if all(self.validar_formulario()):
                self.open_pic_to_profile_pic_2.setHidden(True)
                self.delete_profile_pic_2.setHidden(True)
                self.edit_profile_2.setText("Editar perfil")
                self.open_pic_to_profile_pic_2.setCheckable(False)
                self.open_pic_to_profile_pic_2.setEnabled(False)
                self.delete_profile_pic_2.setEnabled(False)
                self.delete_profile_pic_2.setCheckable(False)
                self.sexo_groupbox_profile_2.setEnabled(False)
                self.name_edit_profile_2.setEnabled(False)
                self.lastname_edit_profile_2.setEnabled(False)
                self.age_spinbox_profile_2.setEnabled(False)
                self.email_edit_profile_2.setEnabled(False)
                self.pass_edit_profile_2.setEnabled(False)
                self.id_edit_profile_2.setEnabled(False)
                self.country_edit_profile_2.setEnabled(False)
                self.passport_edit_profile_2.setEnabled(False)
                self.adress_edit_profile_2.setEnabled(False)
                self.telefono_edit_profile_3.setEnabled(False)
                self.biography_paintext_profile_2.setEnabled(False)
                self.actualizar_progreso()
            
    def validar_formulario(self):
        return [
            self.validar_nombre(),
            self.validar_sexo(),
            self.validar_apellido(),
            self.validar_id(),
            self.validar_biografia(),
            self.validar_direccion(),
            self.validar_telefono(),
            self.validar_pasaporte(),
            self.validar_nacionalidad(),
            self.validar_edad()
            ]

    
    def mostrar_warning(self, mensaje):
        QMessageBox.warning(self, "Validación de Formulario", mensaje)


    def validar_nombre(self):
        nombre = self.name_edit_profile_2.text().strip()
        if not nombre:
            self.mostrar_warning("El nombre no puede estar vacío.")
            return False
        elif not re.match(r'^[a-zA-Z\s]+$', nombre):
            self.mostrar_warning("El nombre no puede contener caracteres especiales ni dígitos.")
            return False
        elif len(nombre.split()) > 3:
            self.mostrar_warning("No puede haber más de tres nombres.")
            return False
        else:
            nombre = ' '.join(nombre.split()).title()
            self.name_edit_profile_2.setText(nombre)
            if not self.paso_nombre_validado:
                self.paso_nombre_validado = True
            return True

    def validar_apellido(self):
        apellido = self.lastname_edit_profile_2.text().strip()
        if not apellido:
            self.mostrar_warning("El apellido no puede estar vacío.")
            return False
        elif not re.match(r'^[a-zA-Z\s]+$', apellido):
            self.mostrar_warning("El apellido no puede contener caracteres especiales ni dígitos.")
            return False
        elif len(apellido.split()) > 3:
            self.mostrar_warning("No puede haber más de tres apellidos.")
            return False
        else:
            apellido = ' '.join(apellido.split()).title()
            self.lastname_edit_profile_2.setText(apellido)
            if not self.paso_apellido_validado:
                self.paso_apellido_validado = True
            return True

        
    def validar_email(self):
        email = self.email_edit_profile_2.text()
        if email.strip() == "":
            self.mostrar_warning("El email no puede estar vacio.")
            return False
            
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email.strip()):
            self.mostrar_warning("Debe colocar un email válido.")
            return False
        return True
    
    def validar_password(self):
        password = self.pass_edit_profile_2.text()
        if password.strip() == "":
            self.mostrar_warning("La contraseña no puede estar vacía.")
            return False

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_regex, password.strip()):
            self.mostrar_warning("La contraseña debe contener al menos 8 caracteres, incluyendo una letra mayúscula, una letra minúscula y un número. No se permiten caracteres especiales.")
            return False
        return True
    
    def validar_id(self):
        ti_o_cc = self.id_edit_profile_2.text()
        if ti_o_cc.strip() == "":
            self.id_edit_profile_2.setText("")
            if self.ti_o_cc_validado:
                self.pasos_completados -= 1
                self.ti_o_cc_validado = False
            return True
        elif all(i.isdigit() or i.isspace() for i in ti_o_cc.strip()):
            identificacion_sin_espacios = ''.join(ti_o_cc.split())
            self.id_edit_profile_2.setText(identificacion_sin_espacios)
            if not self.ti_o_cc_validado:
                self.ti_o_cc_validado = True
                self.pasos_completados += 1
            return True
        else:
            self.mostrar_warning("El número de identificación no puede tener letras o caracteres especiales")
            return False
            


    def validar_sexo(self):
        if self.none_radio_profile_2.isChecked():
            if self.paso_escoger_sexualidad:
                self.paso_escoger_sexualidad = False
                self.pasos_completados -= 1
                self.actualizar_progreso()
        else:
            if not self.paso_escoger_sexualidad:
                self.paso_escoger_sexualidad = True
                self.pasos_completados += 1
                self.actualizar_progreso()
        return True
    
    def validar_nacionalidad(self):
        nacionalidad = self.country_edit_profile_2.currentText().strip()
        if nacionalidad == "" or nacionalidad == "No Especificar":
            if self.nacionalidad_validada:
                self.nacionalidad_validada = False
                self.pasos_completados -= 1
            return True
        elif not re.match(r'^[a-zA-Z\s]+$', nacionalidad):
            if self.nacionalidad_validada:
                self.nacionalidad_validada = False
                self.pasos_completados -= 1
            self.mostrar_warning("La nacionalidad solo puede contener letras.")
            return False
        else:
            nacionalidad = ' '.join(nacionalidad.split()).title()
            self.country_edit_profile_2.setCurrentText(nacionalidad)
            if not self.nacionalidad_validada:
                self.nacionalidad_validada = True
                self.pasos_completados += 1
            return True

    def validar_edad(self):
        edad = self.age_spinbox_profile_2.value()
        if edad < 16:
            if self.edad_validada:
                self.edad_validada = False
                self.pasos_completados -= 1
            self.mostrar_warning("Debe tener al menos 16 años.")
            return False
        else:
            if not self.edad_validada:
                self.edad_validada = True
                self.pasos_completados += 1
            return True
        
    def validar_biografia(self):
        biografia = self.biography_paintext_profile_2.toPlainText().strip()
        if biografia == "":
            if self.biografia_validada:
                self.biografia_validada = False
                self.pasos_completados -= 1
            return True
        else:
            if not self.biografia_validada:
                self.biografia_validada = True
                self.pasos_completados += 1
            return True

    def validar_direccion(self):
        direccion = self.adress_edit_profile_2.text().strip()
        if direccion == "":
            if self.direccion_validada:
                self.direccion_validada = False
                self.pasos_completados -= 1
            return True
        else:
            if not self.direccion_validada:
                self.direccion_validada = True
                self.pasos_completados += 1
            return True
        
    def cargar_telefono(self):
        telefono = self.telefono_edit_profile_3.text()
        if telefono.startswith("+"):
            if telefono:
                prefijo_numero = self.telefono_edit_profile_3.text().split(" ")
                self.telefono_edit_profile_3.setText(f"{prefijo_numero[1]}")
        

    def validar_telefono(self):
        telefono = self.telefono_edit_profile_3.text().strip()
        nacionalidad = self.country_edit_profile_2.currentText().strip()
        
        if telefono == "":
            if self.telefono_validado:
                self.telefono_validado = False
                self.pasos_completados -= 1
            return True
        elif nacionalidad == "Colombia" and not re.match(r'^\d+$', telefono):
            self.mostrar_warning("El número de teléfono solo puede contener números para la nacionalidad Colombia.")
            return False
        else:
            if nacionalidad == "Colombia":
                telefono = f"+57 {telefono}"
            self.telefono_edit_profile_3.setText(telefono)
            if not self.telefono_validado:
                self.telefono_validado = True
                self.pasos_completados += 1
            return True

    def validar_pasaporte(self):
        pasaporte = self.passport_edit_profile_2.text().strip()
        if pasaporte == "":
            if self.pasaporte_validado:
                self.pasaporte_validado = False
                self.pasos_completados -= 1
            return True
        elif not re.match(r'^[A-Za-z0-9]+$', pasaporte):
            self.mostrar_warning("El pasaporte solo puede contener letras y números.")
            return False
        else:
            self.passport_edit_profile_2.setText(pasaporte)
            if not self.pasaporte_validado:
                self.pasaporte_validado = True
                self.pasos_completados += 1
            return True




            



    def cargar_foto_de_perfil(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            nueva_foto = QPixmap(file_name).scaled(QSize(self.label_myprofile_page_photo_2.width(), self.label_myprofile_page_photo_2.height()), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.poner_foto_de_perfil(nueva_foto)

    def borrar_foto_de_perfil(self):
        if self.paso_foto_de_perfil:
            foto_por_defecto = QPixmap(os.path.join(self.basedir, "icons/sinfoto.png")).scaled(QSize(self.label_myprofile_page_photo_2.width(), self.label_myprofile_page_photo_2.height()), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.pasos_completados -= 1
            self.label_myprofile_page_photo_2.setPixmap(foto_por_defecto)
            self.label_pic_small1.setPixmap(foto_por_defecto)
            self.label_pic_small2.setPixmap(foto_por_defecto)
            self.paso_foto_de_perfil = False
            self.actualizar_progreso()

    def poner_foto_de_perfil(self, pixmap):
        if not self.paso_foto_de_perfil:
            self.pasos_completados += 1
            self.label_myprofile_page_photo_2.setPixmap(pixmap)
            self.label_pic_small1.setPixmap(pixmap)
            self.label_pic_small2.setPixmap(pixmap)
            self.paso_foto_de_perfil = True
            self.actualizar_progreso()
        else:
            self.label_myprofile_page_photo_2.setPixmap(pixmap)
            self.label_pic_small1.setPixmap(pixmap)
            self.label_pic_small2.setPixmap(pixmap)


    def actualizar_progreso(self):
        self.progressbar_profile_2.setMaximum(self.pasos_totales)
        self.progressbar_profile_2.setValue(self.pasos_completados)

        if self.pasos_completados == self.pasos_totales:
            self.label_progressbar_profile_2.setText("Perfil Completo")
        else:
            self.label_progressbar_profile_2.setText(f"Completa tu perfil       {self.pasos_completados}/{self.pasos_totales}")

    def update_time(self):
        #Actualiza el reloj
        current_time = QTime.currentTime()
        hours = current_time.hour()
        minutes = current_time.minute()

        self.Horas.display(hours)
        self.minutos.display(minutes)

    def mostrar_pagina_de_soporte(self):
        self.configuraciones_stacked.setCurrentIndex(1)

    def mostrar_pagina_about_us(self):
        self.configuraciones_stacked.setCurrentIndex(2)

    def mostrar_pagina_botones_configuraciones(self):
        self.configuraciones_stacked.setCurrentIndex(0)

    def mostrar_agregar_nuevo_recordatorio(self):
        self.notifications_stacked.setCurrentIndex(1)

    def mostrar_pagina_recordatorios(self):
        self.notifications_stacked.setCurrentIndex(0)

    def mostrar_pagina_perfil(self):
        self.stackedWidget.setCurrentWidget(self.profile_page)

    def mostrar_pagina_home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)

    def mostrar_pagina_mis_viajes(self):
        self.stackedWidget.setCurrentWidget(self.mis_viajes_page)

    def mostrar_pagina_nuevo_viaje(self):
        self.stackedWidget.setCurrentWidget(self.nuevo_viaje_page)

    def mostrar_pagina_itinerario(self):
        self.stackedWidget.setCurrentWidget(self.Iinerario_page)

    def mostrar_pagina_gastos(self):
        self.stackedWidget.setCurrentWidget(self.gastos_page)

    def mostrar_pagina_notificaciones(self):
        self.stackedWidget.setCurrentWidget(self.notifications_page)

    def mostrar_configuraciones_page(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
