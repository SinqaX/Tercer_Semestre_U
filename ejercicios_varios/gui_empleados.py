from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import os
import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI SALARIO EMPLEADO")
        self.setMinimumSize(450, 800)

        # Layout para manejar las diferentes ventanas
        self.ventanas = QStackedLayout()

        self.datos()

        # Establecer el diseño principal de la ventana
        self.setLayout(self.ventanas)
        
    
    def datos(self):
        widget = QWidget()
        qvbox = QVBoxLayout()

        
        self.nombre = QLineEdit()
        self.fecha_nacimiento = QLineEdit()
        self.fecha_nacimiento.setPlaceholderText("dia/mes/año")
        self.email = QLineEdit()
        self.email.setPlaceholderText("ejemplo@gmail.com")
        self.salario = QLineEdit()
        form = QFormLayout()
        form.addRow("Nombre:", self.nombre)
        form.addRow("Fecha de Nacimiento:", self.fecha_nacimiento)
        form.addRow("Email:", self.email)
        form.addRow("Salario Base Deseado:", self.salario)


        #experiencia
        groupbox_exp= QGroupBox('¿Tiene mas de 10 años de experiencia?')
        vbox_group_exp = QVBoxLayout()
        vbox_group_exp.setSpacing(0)
        # Creamos los checkboxes
        self.exper_si = QRadioButton('Si')
        self.exper_no = QRadioButton('No')
        vbox_group_exp.addWidget(self.exper_si)
        vbox_group_exp.addWidget(self.exper_no)
        groupbox_exp.setLayout(vbox_group_exp)


        #idiaomas que habla 
        groupbox_idim = QGroupBox('¿Que idiomas habla?')
        vbox_group_idim = QVBoxLayout()
        vbox_group_idim.setSpacing(0)
        # Creamos los checkboxes
        self.idioma1 = QCheckBox('Ingles')
        self.idioma2 = QCheckBox('Frances')
        self.idioma3 = QCheckBox('Italiano')
        self.idioma4 = QCheckBox('Chino')
        # Añadimos los checkboxes al grupo
        vbox_group_idim.addWidget(self.idioma1)
        vbox_group_idim.addWidget(self.idioma2)
        vbox_group_idim.addWidget(self.idioma3)
        vbox_group_idim.addWidget(self.idioma4)
        groupbox_idim.setLayout(vbox_group_idim)


        #lenguajes de programacion que sabe
        groupbox_programacion = QGroupBox('¿Que lenguajes de programacion maneja?')
        vbox_group_prog = QVBoxLayout()
        vbox_group_prog.setSpacing(0)
        # Creamos los checkboxes
        self.lengua_prog1 = QCheckBox('JavaScript')
        self.lengua_prog2 = QCheckBox('python')
        self.lengua_prog3 = QCheckBox('Java')
        self.lengua_prog4 = QCheckBox('C#')
        self.lengua_prog5 = QCheckBox('P')
        self.lengua_prog6 = QCheckBox('C/C++')
        # Añadimos los checkboxes al grupo
        vbox_group_prog.addWidget(self.lengua_prog1)
        vbox_group_prog.addWidget(self.lengua_prog2)
        vbox_group_prog.addWidget(self.lengua_prog3)
        vbox_group_prog.addWidget(self.lengua_prog4)
        vbox_group_prog.addWidget(self.lengua_prog5)
        vbox_group_prog.addWidget(self.lengua_prog6)
        groupbox_programacion.setLayout(vbox_group_prog)


        #casado
        groupbox_cas= QGroupBox('¿Usted esta casado?')
        vbox_group_cas = QVBoxLayout()
        vbox_group_cas.setSpacing(0)
        # Creamos los checkboxes
        self.casad_si = QRadioButton('Si')
        self.casad_no = QRadioButton('No')
        vbox_group_cas.addWidget(self.casad_si)
        vbox_group_cas.addWidget(self.casad_no)
        groupbox_cas.setLayout(vbox_group_cas)


        #hijos
        groupbox_hij= QGroupBox('¿Usted tiene hijos?')
        vbox_group_hij = QVBoxLayout()
        vbox_group_hij.setSpacing(0)
        # Creamos los checkboxes
        self.hijos_si = QRadioButton('Si')
        self.hijos_no = QRadioButton('No')
        vbox_group_hij.addWidget(self.hijos_si)
        vbox_group_hij.addWidget(self.hijos_no)
        groupbox_hij.setLayout(vbox_group_hij)

        #seguro de vida
        groupbox_seg= QGroupBox('¿Usted quiere adquirir un seguro de vida?')
        vbox_group_seg = QVBoxLayout()
        vbox_group_seg.setSpacing(0)
        # Creamos los checkboxes
        self.seguro_si = QRadioButton('Si')
        self.seguro_no = QRadioButton('No')
        vbox_group_seg.addWidget(self.seguro_si)
        vbox_group_seg.addWidget(self.seguro_no)
        groupbox_seg.setLayout(vbox_group_seg)

        #boton verificar todos los datos completados 
        button = QPushButton("finalizar", self)
        button.clicked.connect(self.verificador_datos)
        

        self.label_dinamico = QLabel("", self)
        self.label_dinamico.setAlignment(Qt.AlignmentFlag.AlignCenter)

        qvbox.addLayout(form)
        qvbox.addWidget(groupbox_exp)
        qvbox.addWidget(groupbox_idim)
        qvbox.addWidget(groupbox_programacion)
        qvbox.addWidget(groupbox_cas)
        qvbox.addWidget(groupbox_hij)
        qvbox.addWidget(groupbox_seg)
        qvbox.addWidget(button)
        qvbox.addWidget(self.label_dinamico)

        widget.setLayout(qvbox)
        self.ventanas.addWidget(widget)

    

    
    def informe_final(self):
        widget_final = QWidget()
        qvbox_final = QVBoxLayout()


        groupbox = QGroupBox("INFORME FINAL CALCULO DE SALARIO EMPLEADO")
        vbox_group_seg = QVBoxLayout()
        label = QLabel(self)
        
        nombre = self.nombre.text()
        fecha_nacimiento = self.fecha_nacimiento.text()
        email = self.email.text()
        salario_base = self.salario.text()

        aumento_experiencia = round(self.porc_experiencia, 2)
        aumento_idioma = round(self.porc_idioma, 2)
        aumento_lenguaje_prog = round(self.porc_lenguaje_prog, 2)
        aumento_casado = round(self.porc_casado, 2)
        aumento_hijos = round(self.porc_hijos, 2)
        descuento_seguro = round(self.porc_seguro, 2)
        salario_final = round(self.salario_final, 2)

        label.setText(f"""
---------------------------------------------------------
                       DATOS                   
---------------------------------------------------------   


Nombre:                {nombre}
Fecha de nacimiento:   {fecha_nacimiento}
Correo electrónico:    {email}
Salario base deseado:  {salario_base}    


---------------------------------------------------------
                     AUMENTOS                            
---------------------------------------------------------


10 años de experiencia (10%):            {aumento_experiencia}
Idiomas que maneja (2% cada uno):        {aumento_idioma}
Lenguajes de programación (5% cada uno): {aumento_lenguaje_prog}
Estar casado (2%):                       {aumento_casado}
Tener hijos (3%):                        {aumento_hijos}


---------------------------------------------------------                                             
                    DESCUENTOS 
---------------------------------------------------------      


Seguro de vida:                          {descuento_seguro}


--------------------------------------------------------- 


            SALARIO FINAL: {salario_final}

        
---------------------------------------------------------
""")
        label.setFont(QFont("Courier", 10))  # Establecer la fuente a Courier, tamaño 10
        vbox_group_seg.addWidget(label)
        groupbox.setLayout(vbox_group_seg)
        

        
        qvbox_final.addWidget(groupbox)

        widget_final.setLayout(qvbox_final)
        self.ventanas.addWidget(widget_final)

    def calculo_de_salario(self):
        salario = self.salario.text().strip()
        salario_entero = int(salario)
        self.porc_idioma = 0
        self.porc_lenguaje_prog = 0
        self.porc_experiencia = 0
        self.porc_casado = 0
        self.porc_hijos = 0
        self.porc_seguro = 0

        # 2% por cada idioma seleccionado
        idioma_count = sum([self.idioma1.isChecked(),
                            self.idioma2.isChecked(),
                            self.idioma3.isChecked(),
                            self.idioma4.isChecked()])
        self.porc_idioma = (0.02 * idioma_count )* salario_entero

        # 5% por cada lenguaje de programación seleccionado
        lenguaje_programacion_count = sum([self.lengua_prog1.isChecked(),
                                        self.lengua_prog2.isChecked(),
                                        self.lengua_prog3.isChecked(),
                                        self.lengua_prog4.isChecked(),
                                        self.lengua_prog5.isChecked(),
                                        self.lengua_prog6.isChecked()])
        self.porc_lenguaje_prog = (0.05 * lenguaje_programacion_count )* salario_entero

        # 10% si tiene más de 10 años de experiencia
        if self.exper_si.isChecked():
            self.porc_experiencia = salario_entero * 0.10

        # 2% si está casado
        if self.casad_si.isChecked():
            self.porc_casado = salario_entero * 0.02

        # 3% si tiene hijos
        if self.hijos_si.isChecked():
            self.porc_hijos = salario_entero * 0.03

        # 7% menos si adquiere seguro de vida
        if self.seguro_si.isChecked():
            self.porc_seguro = salario_entero * 0.07

        salario_final = salario_entero + self.porc_idioma + self.porc_lenguaje_prog + self.porc_experiencia + self.porc_casado + self.porc_hijos - self.porc_seguro
        return salario_final

    def verificador_datos(self):
        nombre = self.nombre.text().strip()
        fecha_nacimiento = self.fecha_nacimiento.text().strip()
        email = self.email.text().strip()
        salario = self.salario.text().strip()

        if not nombre or not fecha_nacimiento or not email or not salario:
            self.label_dinamico.setText("COMPLETE TODOS LOS CAMPOS REQUERIDOS")
            self.ventanas.setCurrentIndex(0)
        else:
            # Verificar si el correo electrónico es válido
            if not self.validar_correo_electronico(email):
                self.label_dinamico.setText("Correo electrónico no válido")
            else:
                # Verificar si el salario es un número entero
                try:
                    salario_entero = int(salario)
                except ValueError:
                    self.label_dinamico.setText("Salario debe ser un número entero")
                else:
                    # Verificar el formato de fecha
                    
                    try:
                        fecha_nacimiento_dt = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
                    except ValueError:
                        self.label_dinamico.setText("Fecha de nacimiento debe estar en formato día/mes/año")
                    else:
                        if not self.exper_si.isChecked() and not self.exper_no.isChecked():
                            self.label_dinamico.setText("Seleccione si tiene más de 10 años de experiencia")
                        else:
                            # Verificar si algún radiobutton de estado civil está seleccionado
                            if not self.casad_si.isChecked() and not self.casad_no.isChecked():
                                self.label_dinamico.setText("Seleccione su estado civil")
                            else:
                                # Verificar si algún radiobutton de hijos está seleccionado
                                if not self.hijos_si.isChecked() and not self.hijos_no.isChecked():
                                    self.label_dinamico.setText("Seleccione si tiene hijos")
                                else:
                                    if not self.seguro_si.isChecked() and not self.seguro_no.isChecked():
                                        self.label_dinamico.setText("Seleccione si quiere adquirir el seguro de vida")
                                    else:
                                        # Todos los datos son válidos♣
                                        self.salario_final = self.calculo_de_salario()
                                        self.informe_final()
                                        self.ventanas.setCurrentIndex(1)
    

    def validar_correo_electronico(self, correo):
        try:
            # Usamos la función validate_email para validar el correo electrónico
            validador = validate_email(correo)
            # Si la dirección es válida, devuelve True
            return True
        except EmailNotValidError:
            # Si ocurre un error, significa que la dirección no es válida, entonces devuelve False
            return False




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
