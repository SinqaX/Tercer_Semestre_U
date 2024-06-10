#sebastian david ordoñez bolaños
#andres felipe martinez guerra


from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os

class Main(QMainWindow):
    usuarios = {}
    todos =[]
    lista_ejecutivo = []
    lista_economica = []
    basedir = os.path.dirname(__file__)
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nombre app")

        # self.icon_window = QPixmap(os.path.join())
        # self.setWindowIcon(self.icon_window)

        # self.resize(QSize(800, 500))

        self.root_layout = QVBoxLayout()
        self.root_layout.setSpacing(0)
        self.root_layout.setContentsMargins(20,0,20,0)

        self.frame_principal = QFrame()
        self.frame_principal_botones = QFrame()
        self.root_pirncipal = QHBoxLayout()
        self.root_pirncipal.addWidget(self.frame_principal)
        self.root_secundario = QHBoxLayout()
        self.root_secundario.addWidget(self.frame_principal_botones)
        self.root_secundario.setContentsMargins(0,0,0,-10)

        self.root_layout.addLayout(self.root_pirncipal)
        self.root_layout.addLayout(self.root_secundario)


        self.root_layout.addWidget(self.frame_principal)
        self.root_layout.addWidget(self.frame_principal_botones)
        self.seccion_1()
        self.seccion_2()
        self.seccion_3()
        self.botones()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.root_layout)
        self.setCentralWidget(self.main_widget)

    def seccion_1(self):
        widget = QWidget()
        widget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        principal = QVBoxLayout()

        label_ejecutiva = QLabel("Clase Ejecutiva")
        label_ejecutiva.setAlignment(Qt.AlignmentFlag.AlignCenter)

        group_ejecutiva = QGroupBox()
        qgrid = QGridLayout()
        self.check_1 = QCheckBox("1")
        self.check_2 = QCheckBox("2")
        self.check_3 = QCheckBox("3")
        self.check_4 = QCheckBox("4")
        self.check_5 = QCheckBox("5")
        self.check_6 = QCheckBox("6")
        self.check_7 = QCheckBox("7")
        self.check_8 = QCheckBox("8")
        qgrid.addWidget(self.check_1, 1,1)
        qgrid.addWidget(self.check_2, 1,2)
        qgrid.addWidget(self.check_3, 1,3)
        qgrid.addWidget(self.check_4, 1,4)
        qgrid.addWidget(self.check_5, 2,1)
        qgrid.addWidget(self.check_6, 2,2)
        qgrid.addWidget(self.check_7, 2,3)
        qgrid.addWidget(self.check_8, 2,4)
        group_ejecutiva.setLayout(qgrid)

        label_economica = QLabel("Clase Economica")
        label_economica.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        group_economica = QGroupBox()
        qgrid_economica = QGridLayout()
        self.check_9 = QCheckBox("9")
        self.check_10 = QCheckBox("10")
        self.check_11 = QCheckBox("11")
        self.check_12 = QCheckBox("12")
        self.check_13 = QCheckBox("13")
        self.check_14 = QCheckBox("14")
        self.check_15 = QCheckBox("15")
        self.check_16 = QCheckBox("16")
        self.check_17 = QCheckBox("17")
        self.check_18 = QCheckBox("18")
        self.check_19 = QCheckBox("19")
        self.check_20 = QCheckBox("20")
        self.check_21 = QCheckBox("21")
        self.check_22 = QCheckBox("22")
        self.check_23 = QCheckBox("23")
        self.check_24 = QCheckBox("24")
        qgrid_economica.addWidget(self.check_9, 1,1)
        qgrid_economica.addWidget(self.check_10, 1,2)
        qgrid_economica.addWidget(self.check_11, 1,3)
        qgrid_economica.addWidget(self.check_12, 1,4)
        qgrid_economica.addWidget(self.check_13, 2,1)
        qgrid_economica.addWidget(self.check_14, 2,2)
        qgrid_economica.addWidget(self.check_15, 2,3)
        qgrid_economica.addWidget(self.check_16, 2,4)
        qgrid_economica.addWidget(self.check_17, 3,1)
        qgrid_economica.addWidget(self.check_18, 3,2)
        qgrid_economica.addWidget(self.check_19, 3,3)
        qgrid_economica.addWidget(self.check_20, 3,4)
        qgrid_economica.addWidget(self.check_21, 4,1)
        qgrid_economica.addWidget(self.check_22, 4,2)
        qgrid_economica.addWidget(self.check_23, 4,3)
        qgrid_economica.addWidget(self.check_24, 4,4)
        group_economica.setLayout(qgrid_economica)

        self.lista_ejecutivo.extend([self.check_1,
                                    self.check_2,
                                    self.check_3,
                                    self.check_4,
                                    self.check_5,
                                    self.check_6,
                                    self.check_7,
                                    self.check_8])
        
        self.lista_economica.extend([self.check_9, 
                                    self.check_10,
                                    self.check_11,
                                    self.check_12,
                                    self.check_13,
                                    self.check_14,
                                    self.check_15,
                                    self.check_16,
                                    self.check_17,
                                    self.check_18,
                                    self.check_19,
                                    self.check_20,
                                    self.check_21,
                                    self.check_22,
                                    self.check_23,
                                    self.check_24])
        self.todos = self.lista_ejecutivo + self.lista_economica
        
        

        principal.setSpacing(0)
        principal.addStretch(1)
        principal.addWidget(label_ejecutiva)
        principal.addSpacing(15)
        principal.addWidget(group_ejecutiva)
        principal.addSpacing(15)
        principal.addWidget(label_economica)
        principal.addSpacing(15)
        principal.addWidget(group_economica)
    
        


        widget.setLayout(principal)
        self.root_pirncipal.addWidget(widget)
    


    def seccion_2(self):
        
        label_img = QLabel()
        img = QPixmap(os.path.join(self.basedir, "img", "avión.png"))
        label_img.setPixmap(img.scaled(250,250))
        label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.root_pirncipal.addWidget(label_img)

    def seccion_3(self):
        self.qsatake =  QStackedLayout()
        self.widget_registro = QWidget()
        self.widget_eliminacion = QWidget()
        self.widget_estadisticas = QWidget()


        #registro pasajero
        qvbox_registro = QVBoxLayout()

        label_titulo = QLabel("Registro de Pasajero", self)
        label_titulo.font().setBold(True)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        qform = QFormLayout()
        qform.setSpacing(15)

        self.No_documento = QLineEdit()

        qhbox_tipo = QHBoxLayout()
        self.radio_pasaporte = QRadioButton("Pasaporte")
        self.radio_cedula = QRadioButton("Cédula")
        self.radio_TI = QRadioButton("T.I.")
        qhbox_tipo.addWidget(self.radio_pasaporte)
        qhbox_tipo.addWidget(self.radio_cedula)
        qhbox_tipo.addWidget(self.radio_TI)

        qhbox_sexo = QHBoxLayout()
        group = QGroupBox()
        self.radio_femenino = QRadioButton("Femenino")
        self.radio_masculino = QRadioButton("Masculino")
        qhbox_sexo.addWidget(self.radio_femenino)
        qhbox_sexo.addWidget(self.radio_masculino)
        group.setLayout(qhbox_sexo)

        
          



        self.edad = QLineEdit()
        self.edad.setFixedSize(50,25)
        self.edad.setMaxLength(2)

        

        qform.addRow("No. Documento: ", self.No_documento)
        qform.addRow("Tipo Documento: ", qhbox_tipo)
        qform.addRow("Edad: ", self.edad)
        qform.addRow("Sexo: ", group)

        button_registro = QPushButton("Registro Pasajero")
        button_registro.clicked.connect(self.validar_registro)

        self.label_dinamico = QLabel("", self)

        qvbox_registro.addWidget(label_titulo)
        qvbox_registro.addLayout(qform)
        qvbox_registro.addSpacing(20)
        qvbox_registro.addWidget(button_registro)
        qvbox_registro.addWidget(self.label_dinamico)


        #eliminacion

        qvbox_elimiacion = QVBoxLayout()
        qform_eliminacion = QFormLayout()
        qform_eliminacion.setSpacing(15)

        label_titulo = QLabel("Eliminacion De Pasajero", self)
        label_titulo.font().setBold(True)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.No_documento_eliminacion = QLineEdit()

        qhbox_tipo_eliminacion = QHBoxLayout()
        self.radio_pasaporte_eliminacion = QRadioButton("Pasaporte")
        self.radio_cedula_eliminacion = QRadioButton("Cédula")
        self.radio_TI_eliminacion = QRadioButton("T.I.")
        qhbox_tipo_eliminacion.addWidget(self.radio_pasaporte_eliminacion)
        qhbox_tipo_eliminacion.addWidget(self.radio_cedula_eliminacion)
        qhbox_tipo_eliminacion.addWidget(self.radio_TI_eliminacion)

        qform_eliminacion.addRow("No. Documento: ", self.No_documento_eliminacion)
        qform_eliminacion.addRow("Tipo Documento: ", qhbox_tipo_eliminacion)


        button_eliminar = QPushButton("Eliminar")

        self.label_dinamico_eliminacion = QLabel("", self)

        qvbox_elimiacion.addWidget(label_titulo)
        qvbox_elimiacion.addLayout(qform_eliminacion)
        qvbox_elimiacion.addSpacing(20)
        qvbox_elimiacion.addWidget(button_eliminar)
        qvbox_elimiacion.addWidget(self.label_dinamico_eliminacion)

        #ESTADISTICAS

        qvbox_estadisticas = QVBoxLayout()
        qform_estadisticas = QFormLayout()
        qform_estadisticas.setSpacing(10)

        label_titulo = QLabel("Estadisticas del Vuelo", self)
        label_titulo.font().setBold(True)
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.porcentaje_ocupacion = QLineEdit()
        self.porcentaje_ocupacion.setReadOnly(True)
        self.ocupacion_ejecutiva = QLineEdit()
        self.ocupacion_ejecutiva.setReadOnly(True)
        self.ocupacion_economica = QLineEdit()
        self.ocupacion_economica.setReadOnly(True)
        self.ocupacion_sexo = QLineEdit()
        self.ocupacion_sexo.setReadOnly(True)
        qhbox_sexo = QHBoxLayout()
        self.femenino_estadistica = QRadioButton()
        self.femenino_estadistica.setText("Femenino")
        self.masculino_estadistica = QRadioButton()
        self.masculino_estadistica.setText("Masculino")
        qhbox_sexo.addWidget(self.femenino_estadistica)
        qhbox_sexo.addWidget(self.masculino_estadistica)

        self.ocupacion_edad = QLineEdit()
        self.ocupacion_edad.setReadOnly(True)
        self.check_mayores_edad = QCheckBox("Mayores de edad")

        qform_estadisticas.addRow("Porcentaje de ocupacion: ", self.porcentaje_ocupacion)
        qform_estadisticas.addRow("Ocupacion Ejecutiva: ", self.ocupacion_ejecutiva)
        qform_estadisticas.addRow("Ocupacion Economica:", self.ocupacion_economica)
        qform_estadisticas.addRow("Ocupacion por Sexo", self.ocupacion_sexo)
        qform_estadisticas.addRow("", qhbox_sexo)
        qform_estadisticas.addRow("Ocupacion por Edad", self.ocupacion_edad)
        qform_estadisticas.addRow("", self.check_mayores_edad)

        qvbox_estadisticas.addWidget(label_titulo)
        qvbox_estadisticas.addLayout(qform_estadisticas)


        self.widget_registro.setLayout(qvbox_registro)
        self.widget_eliminacion.setLayout(qvbox_elimiacion)
        self.widget_estadisticas.setLayout(qvbox_estadisticas)

        
        self.root_pirncipal.addWidget(self.widget_registro)
        self.root_pirncipal.addWidget(self.widget_eliminacion)
        self.root_pirncipal.addWidget(self.widget_estadisticas)
        self.qsatake.addWidget(self.widget_registro)
        self.qsatake.addWidget(self.widget_eliminacion)
        self.qsatake.addWidget(self.widget_estadisticas)
    
        

    def botones(self):
        qhbox = QHBoxLayout()
        qhbox.setContentsMargins(0,0,0,0)

        self.button_registro = QPushButton("Registro", self)
        self.button_registro.setFixedSize(100,30)
        self.button_registro.clicked.connect(self.show_registro)

        self.button_eliminar = QPushButton("Eliminar Pasajero", self)
        self.button_eliminar.setFixedSize(140,30)
        self.button_eliminar.clicked.connect(self.show_eliminacion)

        self.button_estadisticas = QPushButton("Estadisticas", self)
        self.button_estadisticas.setFixedSize(120,30)
        self.button_estadisticas.clicked.connect(self.show_estadisticas)

        qhbox.addWidget(self.button_registro, alignment=Qt.AlignmentFlag.AlignLeft)
        qhbox.addWidget(self.button_eliminar, alignment=Qt.AlignmentFlag.AlignCenter)
        qhbox.addWidget(self.button_estadisticas, alignment=Qt.AlignmentFlag.AlignRight)

        self.frame_principal_botones.setLayout(qhbox)

    def show_registro(self):
        self.qsatake.setCurrentWidget(self.widget_registro)

    def show_eliminacion(self):
        self.qsatake.setCurrentWidget(self.widget_eliminacion)

    def show_estadisticas(self):
        self.qsatake.setCurrentWidget(self.widget_estadisticas)

    def validar_registro(self):
        edad = self.edad.text().split()
        no_doc = self.No_documento.text().split()
        tipo_documento = None
        sexo_usuario = None
        silla = None
        sexos = [self.radio_femenino, self.radio_masculino]

        # Obtener la silla seleccionada
        for i in self.todos:
            if i.isChecked() and i.isCheckable():
                silla = i.text()
        
        # Validar la información del pasajero
        if silla:
            if no_doc:
                if edad:
                    try:
                        no_doc = int(no_doc[0]) 
                        edad = int(edad[0])
                    except ValueError:
                        self.label_dinamico.setText("El número de documento y la edad deben ser números enteros")
                        return False

                    if len(str(no_doc)) >= 2:  # Corregido: verificar la longitud del número de documento
                        for i in [self.radio_pasaporte, self.radio_cedula, self.radio_TI]:
                            if i.isChecked():
                                if i.text() == "Cédula":
                                    if edad < 18:
                                        self.label_dinamico.setText("Un pasajero menor de edad no tiene cédula")
                                        return False
                                    else:
                                        tipo_documento = i.text()
                                elif i.text() == "T.I.":
                                    if edad >= 18:
                                        self.label_dinamico.setText("Un pasajero mayor de edad no tiene T.I")
                                        return False
                                    else:
                                        tipo_documento = i.text()
                                elif i.text() == "Pasaporte":
                                    tipo_documento = i.text()
                        
                        # Obtener el sexo del pasajero
                        for j in sexos:
                            if j.isChecked():
                                sexo_usuario = j.text()
                                break  # Salir del bucle cuando se haya encontrado el sexo

                        if sexo_usuario:
                            self.usuarios[no_doc] = [no_doc, tipo_documento, edad, sexo_usuario, silla]
                            self.label_dinamico.setText(f"Pasajero {no_doc} registrado en silla {silla}")
                            print(f"Se agregó el usuario {self.usuarios[no_doc]}")
                            return True
                        else:
                            self.label_dinamico.setText("Debe seleccionar su sexo")
                    else:
                        self.label_dinamico.setText("El número de documento debe tener al menos 2 caracteres")
                else:
                    self.label_dinamico.setText("Ingrese su edad")
            else:
                self.label_dinamico.setText("Ingrese su número de documento")
        else:
            self.label_dinamico.setText("Seleccione una silla")



        
        
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exit(app.exec())