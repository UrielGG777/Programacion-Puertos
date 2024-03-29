import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P5_VerticalSlider.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.datos_persona = {
            1: ["Badillo", "Jugar", 20, "o+", ":/meme/Imagen/badillo .png"],
            2: ["Eduardo", "?", 20, "o+", ":/meme/Imagen/JuarezBeltran.png"],
            3: ["Sofia", "?", 20, "o+", ":/meme/Imagen/sofi.png"],
            4: ["Uriel", "?", 20, "o+", ":/meme/Imagen/GonzalezUriel.png"],
            }
        self.vs_personas.setMinimum(1)
        self.vs_personas.setMaximum(4)
        self.vs_personas.setSingleStep(1)
        self.vs_personas.setValue(1)
        self.vs_personas.valueChanged.connect(self.cambia)
        # Área de los Slots

    def cambia(self):
        dataClave = self.vs_personas.value()
        print(dataClave)
        imagen = self.datos_persona[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

