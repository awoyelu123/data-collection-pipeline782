import json
import requests
import os 
from .scraper import Scraper

class Transformer():
    def _init__(self):
        pass

    
    def save__single_product_info_json_locally(self):
        data_point_path = '/'.join([
        os.getcwd(), 
        'waterstones/test_data', 
        self.product_list[0]['isbn']])
        
        print(data_point_path)


        if not os.path.exists(data_point_path):
            os.makedirs(data_point_path)
        with open(data_point_path +'/data.json',mode='w+') as f:
            json.dump(self.product_list[0], f, indent=4)
    print ("Data point saved locally !")


    def save_all_product_info_json_locally(self):
        for data in range(len(self.product_list)):
            data_point_path = '/'.join([
            os.getcwd(), 
            'waterstones/test_data', 
            self.product_list[data]['isbn']])
            


            if not os.path.exists(data_point_path):
                os.makedirs(data_point_path)
            with open(data_point_path +'/data.json',mode='w+') as f:
                json.dump(self.product_list[data], f, indent=4)

        print("All product data saved locally !")        


    def save_single_product_image_locally(self):

        image_folder_path = '/'.join([
        os.getcwd(), 
        'waterstones/test_data', 
        self.product_list[0]['isbn'], 
        'images'])

        if not os.path.exists(image_folder_path):
                os.makedirs(image_folder_path)

        image_name = image_folder_path + '/' + '1' + '.jpg'

        img_data= requests.get(self.product_list[0]['product_img_link']).content

        with open(image_name, 'wb') as handler:
                handler.write(img_data)

        print("Single product image saved!")

    def save_all_images_locally(self):
        for img in range (len(self.product_list)):
            image_folder_path = '/'.join([
                os.getcwd(), 
                'waterstones/test_data', 
                self.product_list[img]['isbn'], 
                'images'])

            image_name = image_folder_path + '/' + str(img + 1) + '.jpg'

            if not os.path.exists(image_folder_path):
                os.makedirs(image_folder_path)

            img_data= requests.get(self.product_list[img]['product_img_link']).content

            with open(image_name, 'wb') as handler:
                handler.write(img_data)
        print ("All image data saved locally!")