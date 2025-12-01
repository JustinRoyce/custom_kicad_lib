import os
import sys
from kicad_image_layers import KiCadImageLayers 
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow,QColorDialog,QGraphicsScene, QGraphicsView
from PySide6.QtGui import QIcon, QPixmap, QImage
from kicad_image_layers_pyside6 import Ui_MainWindow
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QRectF
from pathlib import Path

# Define paths for media assets
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(SCRIPT_DIR, "media")
COLORPICKER_IMAGE_PATH = os.path.join(MEDIA_DIR, "colorpicker.png")
KICAD_IMAGE_PATH = os.path.join(MEDIA_DIR, "KiCad_Logo.png")
INKSCAPE_IMAGE_PATH = os.path.join(MEDIA_DIR, "Inkscape_Logo.png")



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
        self.uneditable_line_edits()
        self.add_color_label_size()

        self.load_images_to_scene()

    def connect_slots(self):
        self.ui.PB_Layer1_Color.clicked.connect(self.open_layer1_color_dialog)
        self.ui.PB_Layer2_Color.clicked.connect(self.open_layer2_color_dialog)
        self.ui.PB_Layer3_Color.clicked.connect(self.open_layer3_color_dialog)
        self.ui.PB_PNG_Path.clicked.connect(self.clicked_png_path)
        self.ui.PB_Layer1_Path.clicked.connect(self.open_layer1_path_dialog)
        self.ui.PB_Layer2_Path.clicked.connect(self.open_layer2_path_dialog)
        self.ui.PB_Layer3_Path.clicked.connect(self.open_layer3_path_dialog)
        self.ui.PB_Auto_Generator.clicked.connect(self.autogenerate_parameters)       

        return None
    # Auto-generate parameters functionality to be implemented
    def autogenerate_parameters(self):
        #validate png path
        if not self.is_valid_png_path():
            # Show error message or handle invalid path
            print("Invalid PNG path. Please select a valid PNG file.")
            return
        
        # read parameters from image
        png_path = self.ui.LE_PNG_Path.text()
        
        self.KIL_obj.set_png_path(png_path)
        image_info = self.KIL_obj.get_all_colors_from_image()
        if image_info is None:
            print("Failed to extract image information.")
            return
        return None

    def is_valid_png_path(self):
        png_path = self.ui.LE_PNG_Path.text()
        if png_path.lower().endswith('.png') and os.path.isfile(png_path):
            return True
        return False
    
    def add_color_label_size(self):
        color_box_size = 18
        self.ui.LB_Layer1_Color_Viewer.setFixedSize(color_box_size,color_box_size)
        self.ui.LB_Layer2_Color_Viewer.setFixedSize(color_box_size,color_box_size)
        self.ui.LB_Layer3_Color_Viewer.setFixedSize(color_box_size,color_box_size)
        return None
    
    def uneditable_line_edits(self):
        self.ui.LE_Layer1_Color.setReadOnly(True)
        self.ui.LE_Layer2_Color.setReadOnly(True)
        self.ui.LE_Layer3_Color.setReadOnly(True)
        self.ui.LE_PNG_Path.setReadOnly(True)

        return None
    
    def load_images_to_scene(self):
        kicad_image_path = KICAD_IMAGE_PATH
        inkscape_image_path = INKSCAPE_IMAGE_PATH

        
        kicad_image = QImage(kicad_image_path)
        inkscape_image = QImage(inkscape_image_path)
        
        kicad_scene = QGraphicsScene()
        inkscape_scene = QGraphicsScene()

        kicad_pixmap = QPixmap.fromImage(kicad_image)
        inkscape_pixmap = QPixmap.fromImage(inkscape_image)

        kicad_scene.addPixmap(kicad_pixmap)
        inkscape_scene.addPixmap(inkscape_pixmap)
        
      
        kicad_size = self.ui.GV_KiCAD.geometry()
        inkscape_size = self.ui.GV_Inkscape.geometry()

        kicad_scaleWidth = kicad_size.width()  + 50
        kicad_scaleHeight = kicad_size.height()- 100

        inkscape_scaleWidth = inkscape_size.width()  + 25
        inkscape_scaleHeight = inkscape_size.height() - 100

        self.ui.GV_KiCAD.setScene(kicad_scene)
        self.ui.GV_Inkscape.setScene(inkscape_scene)

        self.ui.GV_KiCAD.fitInView(QRectF(0, 0, kicad_scaleWidth, kicad_scaleHeight),)
        self.ui.GV_Inkscape.fitInView(QRectF(0, 0, inkscape_scaleWidth, inkscape_scaleHeight))

        self.ui.GV_KiCAD.setStyleSheet("background-color: {}".format("#FEFEFE"))
        self.ui.GV_Inkscape.setStyleSheet("background-color: {}".format("#FEFEFE"))

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

    def open_layer1_color_dialog(self):
        color_dialog = QColorDialog.getColor()
        color_value = color_dialog.getRgb()
        hex_color_value = self.color_2_hex_value(color_value)
        self.set_layer1_color(hex_color_value)
        return None
    
    def open_layer2_color_dialog(self):
        color_dialog = QColorDialog.getColor()
        color_value = color_dialog.getRgb()
        hex_color_value = self.color_2_hex_value(color_value)
        self.set_layer2_color(hex_color_value)
        return None
    
    def open_layer3_color_dialog(self):
        color_dialog = QColorDialog.getColor()
        color_value = color_dialog.getRgb()
        hex_color_value = self.color_2_hex_value(color_value)
        self.set_layer3_color(hex_color_value)
        return None

    def set_layer1_color(self, hex_color_value):
        self.ui.LE_Layer1_Color.setText(hex_color_value)
        self.ui.LB_Layer1_Color_Viewer.setStyleSheet("background-color: {}".format(hex_color_value))
        return None

    def set_layer2_color(self, hex_color_value):
        self.ui.LE_Layer2_Color.setText(hex_color_value)
        self.ui.LB_Layer2_Color_Viewer.setStyleSheet("background-color: {}".format(hex_color_value))
        return None

    def set_layer3_color(self, hex_color_value):
        self.ui.LE_Layer3_Color.setText(hex_color_value)
        self.ui.LB_Layer3_Color_Viewer.setStyleSheet("background-color: {}".format(hex_color_value))    
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

        png_path = Path(SCRIPT_DIR)
        png_path = png_path.parent

        fileName = QFileDialog.getOpenFileName(self,
        "Select Image", 
         png_path.as_posix() , 
        "Image Files (*.png *.jpg *.bmp)")

        if fileName[0]:
            return fileName[0]
        
        return None
        
    def open_layer1_path_dialog(self):

        png_path = Path(SCRIPT_DIR)
        png_path = png_path.parent

        folder_path = QFileDialog.getExistingDirectory(self,
        "Select Folder", 
         png_path.as_posix())

        if folder_path: 
            self.ui.LE_Layer1_Path.setText(folder_path)
        
        return None
    
    def open_layer2_path_dialog(self):

        png_path = Path(SCRIPT_DIR)
        png_path = png_path.parent

        folder_path = QFileDialog.getExistingDirectory(self,
        "Select Folder", 
         png_path.as_posix())

        if folder_path: 
            self.ui.LE_Layer2_Path.setText(folder_path)
        
        return None
    
    def open_layer3_path_dialog(self):

        png_path = Path(SCRIPT_DIR)
        png_path = png_path.parent

        folder_path = QFileDialog.getExistingDirectory(self,
        "Select Folder", 
         png_path.as_posix())

        if folder_path: 
            self.ui.LE_Layer3_Path.setText(folder_path) 

        return None

if __name__ == "__main__":
    print("GUI initialized")
    app = QApplication(sys.argv)

    gui = KiCadImageLayerGUI()  
    gui.show()
    sys.exit(app.exec())
   
