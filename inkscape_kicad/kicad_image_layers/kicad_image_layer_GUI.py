import os
import sys
from kicad_image_layers import KiCadImageLayers 
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow,QColorDialog
from PySide6.QtGui import QIcon 
from kicad_image_layers_pyside6 import Ui_MainWindow
from PySide6.QtGui import QColor


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(SCRIPT_DIR, "media")
COLORPICKER_IMAGE_PATH = os.path.join(MEDIA_DIR, "colorpicker.png")

class KiCadImageLayerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.KIL_obj = KiCadImageLayers()
        self.PCB_layers_list = self.KIL_obj.get_PCB_layer_list()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_colorpicker_image()
        self.load_combo_boxes_data()

        self.connect_slots()


    def connect_slots(self):
        self.ui.PB_Layer1_Color.clicked.connect(self.get_layer1_color)
        #self.ui.PB_Layer2_Color.clicked.connect(self.get_layer2_color)
        #self.ui.PB_Layer3_Color.clicked.connect(self.get_layer3_color)
        self.ui.PB_PNG_Path.clicked.connect(self.clicked_png_path)
        return None

    def load_colorpicker_image(self):
        colorpicker_path = COLORPICKER_IMAGE_PATH
        colorpicker_icon_obj =  QIcon(colorpicker_path)
        self.ui.PB_Layer1_Color.setIcon(colorpicker_icon_obj)
        self.ui.PB_Layer2_Color.setIcon(colorpicker_icon_obj)
        self.ui.PB_Layer3_Color.setIcon(colorpicker_icon_obj)
        return None
    
    def load_combo_boxes_data(self):
        pcb_layer_list = self.PCB_layers_list
        self.ui.CB_Layer1_Color_1.addItems(pcb_layer_list)   
        self.ui.CB_Layer2_Color_1.addItems(pcb_layer_list)
        self.ui.CB_Layer3_Color_1.addItems(pcb_layer_list)

        self.ui.CB_Layer1_Color_2.addItems(pcb_layer_list)   
        self.ui.CB_Layer2_Color_2.addItems(pcb_layer_list)
        self.ui.CB_Layer3_Color_2.addItems(pcb_layer_list)

        f_cu_str = self.KIL_obj.get_PCB_layer_F_Cu()
        f_mask_str = self.KIL_obj.get_PCB_layer_F_Mask()
        f_silkscreen_str = self.KIL_obj.get_PCB_layer_F_Silkscreen()
        f_user_drawings_str = self.KIL_obj.get_PCB_layer_User_Drawings()
        f_none_str = self.KIL_obj.get_PCB_layer_None()


        self.ui.CB_Layer1_Color_1.setCurrentText(f_silkscreen_str)
        self.ui.CB_Layer2_Color_1.setCurrentText(f_cu_str)
        self.ui.CB_Layer3_Color_1.setCurrentText(f_user_drawings_str)

        self.ui.CB_Layer1_Color_2.setCurrentText(f_none_str)
        self.ui.CB_Layer2_Color_2.setCurrentText(f_mask_str)
        self.ui.CB_Layer3_Color_2.setCurrentText(f_none_str)
        pass

    def get_layer1_color(self):
        color_dialog = QColorDialog.getColor()
        color_value = color_dialog.getRgb()
        hex_color_value = self.color_2_hex_value(color_value)
        print("Layer 1 Color RGB Value:", hex_color_value)
        self.ui.LE_Layer1_Color.setText(hex_color_value)
        
        return None
    
    def color_2_hex_value(self, color_value: tuple[int,int,int,int]) -> str:
        r = color_value[0]
        g = color_value[1]
        b = color_value[2]
        hex_value = "#{:02x}{:02x}{:02x}".format(r, g, b)
        return hex_value
    
    def clicked_png_path(self):
        png_path = self.get_png_path_from_dialog()
        if png_path is not None:
            self.ui.LE_PNG_Path.setText(png_path)
            self.KIL_obj.set_png_path(png_path)
        return None

    def get_png_path_from_dialog(self) -> str:

        fileName = QFileDialog.getOpenFileName(self,
        "Select Image", 
        SCRIPT_DIR , 
        "Image Files (*.png *.jpg *.bmp)")

        if fileName[0]:
            return fileName[0]
        else:
            return None

if __name__ == "__main__":
    print("GUI initialized")
    app = QApplication(sys.argv)

    gui = KiCadImageLayerGUI()  
    gui.show()
    sys.exit(app.exec())
   
