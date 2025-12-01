import os
import sys
from PIL import Image

PCB_LAYER_F_CU = "F.Cu"
PCB_LAYER_B_CU = "B.Cu"
PCB_LAYER_F_MASK = "F.Mask"
PCB_LAYER_B_MASK = "B.Mask"
PCB_LAYER_F_SILKSCREEN = "F.Silkscreen"
PCB_LAYER_B_SILKSCREEN = "B.Silkscreen"
PCB_LAYER_EDGE_CUTS = "Edge.Cuts"
PCB_USER_DRAWINGS = "User.Drawings"
PCB_USER_NONE = "None"

PCB_LAYER_F_CU_PREFIX = "F-CU"
PCB_LAYER_B_CU_PREFIX = "B-CU"
PCB_LAYER_F_MASK_PREFIX = "F-MASK"
PCB_LAYER_B_MASK_PREFIX = "B-MASK"
PCB_LAYER_F_SILKSCREEN_PREFIX = "F-SILK"
PCB_LAYER_B_SILKSCREEN_PREFIX = "B-SILK"
PCB_LAYER_EDGE_CUTS_PREFIX = "EDGE-CUTS"
PCB_USER_DRAWINGS_PREFIX = "U-DRAWINGS"
PCB_USER_NONE_PREFIX = "NONE"

PCB_LAYER_LIST:str = [ 
    PCB_LAYER_F_CU,
    PCB_LAYER_B_CU,
    PCB_LAYER_F_MASK,
    PCB_LAYER_B_MASK,
    PCB_LAYER_F_SILKSCREEN,
    PCB_LAYER_B_SILKSCREEN,
    PCB_LAYER_EDGE_CUTS,
    PCB_USER_DRAWINGS,
    PCB_USER_NONE
]

PCB_LAYER_DICT:str = {
    PCB_LAYER_F_CU: PCB_LAYER_F_CU_PREFIX,
    PCB_LAYER_B_CU: PCB_LAYER_B_CU_PREFIX,
    PCB_LAYER_F_MASK: PCB_LAYER_F_MASK_PREFIX,
    PCB_LAYER_B_MASK: PCB_LAYER_B_MASK_PREFIX,
    PCB_LAYER_F_SILKSCREEN: PCB_LAYER_F_SILKSCREEN_PREFIX,
    PCB_LAYER_B_SILKSCREEN: PCB_LAYER_B_SILKSCREEN_PREFIX,
    PCB_LAYER_EDGE_CUTS: PCB_LAYER_EDGE_CUTS_PREFIX,
    PCB_USER_DRAWINGS: PCB_USER_DRAWINGS_PREFIX,
    PCB_USER_NONE: PCB_USER_NONE_PREFIX
} 


NOTES = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: "\2610"; }
li.checked::marker { content: "\2612"; }
</style></head><body style=" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:700;">NOTE:</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:700;">Layer 1: Silkscreen + None</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">- silkscreen usually corresponds to white </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">- use lightest color</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:700;">Layer 2: Copper + Mask</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">- creates metalic color on PCB</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">- use mid color</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:700;">Layer 3:  User.Drawings + None</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">- no etching of PCB, usually corresponds to green color</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">- use darkest color</p></body></html>
"""


class KiCadImageLayers:
    def __init__(self):
        self.png_path:str = None
        self.layer_1_paths:str = None
        self.layer_2_paths:str = None
        self.layer_3_paths:str = None
        self.layer_1_color:str = None
        self.layer_2_color:str = None
        self.layer_3_color:str = None


    def get_PCB_layer_list(self)-> list[str]:
        pcb_layer_list = PCB_LAYER_LIST  
        return pcb_layer_list   

    def get_PCB_layer_F_Cu(self)-> str:
        return PCB_LAYER_F_CU

    def get_PCB_layer_B_Cu(self)-> str:
        return PCB_LAYER_B_CU

    def get_PCB_layer_F_Mask(self)-> str:
        return PCB_LAYER_F_MASK

    def get_PCB_layer_B_Mask(self)-> str:
        return PCB_LAYER_B_MASK

    def get_PCB_layer_F_Silkscreen(self)-> str:
        return PCB_LAYER_F_SILKSCREEN

    def get_PCB_layer_B_Silkscreen(self)-> str:
        return PCB_LAYER_B_SILKSCREEN

    def get_PCB_layer_Edge_Cuts(self)-> str:
        return PCB_LAYER_EDGE_CUTS
    
    def get_PCB_layer_User_Drawings(self)-> str:
        return PCB_USER_DRAWINGS
    
    def get_PCB_layer_None(self)-> str:
        return PCB_USER_NONE

    def set_png_path(self, png_path:str):
        self.png_path = png_path     
    
    def set_layer_1_path(self, layer_1_paths:str):
        self.layer_1_path = layer_1_paths

    def set_layer_2_path(self, layer_2_paths:str):
        self.layer_2_path = layer_2_paths

    def set_layer_3_path(self, layer_3_paths:str):
        self.layer_3_path = layer_3_paths

    def set_layer_1_color(self, layer_1_color:str):
        self.layer_1_color = layer_1_color

    def set_layer_2_color(self, layer_2_color:str):
        self.layer_2_color = layer_2_color

    def set_layer_3_color(self, layer_3_color:str):
        self.layer_3_color = layer_3_color
    
    def get_color_magnitude(self, color_value: tuple[int,int,int]) -> int:
        r = color_value[0]
        g = color_value[1]
        b = color_value[2]
        magnitude = (r**2 + g**2 + b**2) ** 0.5
        
        return int(magnitude)
    
    def get_all_colors_from_image(self) -> "ImageInfo":
        img_path = self.png_path
        img_info_obj = ImageInfo()
       
        try:
            img = Image.open(img_path)
            img = img.convert("RGB")
            unique_colors_set = set(img.getdata())
            img_width, img_height = img.size
            num_of_colors = len(unique_colors_set)
            img_info_obj.set_file_path(img_path)
            img_info_obj.set_img_width(img_width)
            img_info_obj.set_img_height(img_height)
            img_info_obj.set_num_of_colors(num_of_colors)

            for x in range(img_width):
                for y in range(img_height):
                    pixel_color = img.getpixel((x, y))

                    hex_color_value = img_info_obj.color_2_hex_value(pixel_color)

                    if hex_color_value in img_info_obj.color_dict:
                        img_info_obj.color_dict[hex_color_value] += 1
                    else:
                        img_info_obj.color_dict[hex_color_value] = 1    

        except FileNotFoundError:
            print(f"Error: Image file not found at {img_path}")
            return -1
        except Exception as e:
            print(f"An error occurred: {e}")
            return -1
        
        return img_info_obj

    def color_2_hex_value(self, color_value: tuple[int,int,int]) -> str:
        r = color_value[0]
        g = color_value[1]
        b = color_value[2]
        hex_value = "#{:02x}{:02x}{:02x}".format(r, g, b)
        return hex_value



    
class ImageInfo:
    def __init__(self):
        self.file_path:str = None
        self.img_width:int = None   
        self.img_height:int = None
        self.num_of_colors:int = None
        self.color_dict:dict[str] = {}
    
    def set_file_path(self, file_path:str):
        self.file_path = file_path

    def set_img_width(self, img_width:int):
        self.img_width = img_width
    
    def set_img_height(self, img_height:int):
        self.img_height = img_height
    
    def set_num_of_colors(self, num_of_colors:int):
        self.num_of_colors = num_of_colors  
    
    def set_colors_dict(self, color_tuple: tuple[int,int,int], count:int):

        color_hex_value = self.color_2_hex_value(color_tuple)
        self.color_dict[color_hex_value] = count

    def get_file_path(self)-> str:
        return self.file_path  

    def get_img_width(self)-> int:
        return self.img_width
    
    def get_img_height(self)-> int:
        return self.img_height
    
    def get_num_of_colors(self)-> int:
        return self.num_of_colors
    
    def get_colors_dict(self)-> dict[str]:
        return self.colors_dict  
    
    def print_image_info(self):
        print(f"Image File Path: {self.get_file_path()}")
        print(f"Image Width: {self.get_img_width()} pixels")
        print(f"Image Height: {self.get_img_height()} pixels")
        print(f"Number of Unique Colors: {self.get_num_of_colors()}")
  
