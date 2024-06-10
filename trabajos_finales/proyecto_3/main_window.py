from PySide6.QtWidgets import QMainWindow, QSplitter, QTreeWidget, QTableWidget, QVBoxLayout, QWidget, QToolBar, QMenuBar, QTreeWidgetItem, QTableWidgetItem, QMessageBox, QInputDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Bodega de Reciclaje")
        self.setGeometry(100, 100, 800, 600)
        
        # Base de datos
        self.db = Database('reciclaje.db')
        
        # Menu Bar
        self.menuBar = self.menuBar()
        fileMenu = self.menuBar.addMenu('Archivo')
        editMenu = self.menuBar.addMenu('Editar')
        viewMenu = self.menuBar.addMenu('Ver')
        helpMenu = self.menuBar.addMenu('Ayuda')
        
        # Tool Bar
        self.toolbar = QToolBar("Barra de herramientas")
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        
        # Actions
        addCategoryAction = QAction("Añadir Categoría", self)
        addMaterialAction = QAction("Añadir Material", self)
        registerEntryAction = QAction("Registrar Entrada", self)
        registerExitAction = QAction("Registrar Salida", self)
        generateReportAction = QAction("Generar Reporte", self)
        
        addCategoryAction.triggered.connect(self.addCategory)
        addMaterialAction.triggered.connect(self.addMaterial)
        registerEntryAction.triggered.connect(self.registerEntry)
        registerExitAction.triggered.connect(self.registerExit)
        generateReportAction.triggered.connect(self.generateReport)
        
        # Add actions to toolbar
        self.toolbar.addAction(addCategoryAction)
        self.toolbar.addAction(addMaterialAction)
        self.toolbar.addAction(registerEntryAction)
        self.toolbar.addAction(registerExitAction)
        self.toolbar.addAction(generateReportAction)
        
        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        
        # QTreeWidget
        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderLabels(['Categorías'])
        splitter.addWidget(self.treeWidget)
        
        # QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Nombre', 'Cantidad', 'Última Entrada', 'Última Salida'])
        splitter.addWidget(self.tableWidget)
        
        # Main Layout
        centralWidget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
        # Populate TreeWidget with data from database
        self.populateTree()
        
        # Connect signals and slots
        self.treeWidget.itemClicked.connect(self.onItemClicked)
    
    def populateTree(self):
        self.treeWidget.clear()
        categories = self.db.get_categories()
        for category in categories:
            parent = QTreeWidgetItem(self.treeWidget, [category])
            materials = self.db.get_materials_by_category(category)
            for material in materials:
                QTreeWidgetItem(parent, [material['name']])
    
    def onItemClicked(self, item, column):
        self.tableWidget.setRowCount(0)
        if item.parent():
            material = self.db.get_material(item.text(0))
            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QTableWidgetItem(material['name']))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(str(material['quantity'])))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(material['last_entry']))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(material['last_exit']))
    
    def addCategory(self):
        category, ok = QInputDialog.getText(self, "Añadir Categoría", "Nombre de la Categoría:")
        if ok and category:
            self.db.add_category(category)
            self.populateTree()
    
    def addMaterial(self):
        item = self.treeWidget.currentItem()
        if not item or not item.parent() is None:
            QMessageBox.warning(self, "Error", "Selecciona una categoría para añadir el material.")
            return
        category = item.text(0)
        name, ok = QInputDialog.getText(self, "Añadir Material", "Nombre del Material:")
        if ok and name:
            self.db.add_material(name, category)
            self.populateTree()
    
    def registerEntry(self):
        item = self.treeWidget.currentItem()
        if not item or item.parent() is None:
            QMessageBox.warning(self, "Error", "Selecciona un material para registrar la entrada.")
            return
        material_name = item.text(0)
        quantity, ok = QInputDialog.getInt(self, "Registrar Entrada", "Cantidad:")
        if ok and quantity > 0:
            self.db.update_material_quantity(material_name, quantity, 'entry')
            self.populateTree()
    
    def registerExit(self):
        item = self.treeWidget.currentItem()
        if not item or item.parent() is None:
            QMessageBox.warning(self, "Error", "Selecciona un material para registrar la salida.")
            return
        material_name = item.text(0)
        quantity, ok = QInputDialog.getInt(self, "Registrar Salida", "Cantidad:")
        if ok and quantity > 0:
            self.db.update_material_quantity(material_name, quantity, 'exit')
            self.populateTree()
    
    def generateReport(self):
        QMessageBox.information(self, "Generar Reporte", "Funcionalidad no implementada.")
