# TRATAMENTO DE IMAGEM E OCR
from PIL import Image 
import cv2
import pytesseract
import json

def extraiNFMalte(imagem):    

    img_format = "png" # formato da imagem a ser analisada

    # declaracao do nome das imagens e variaveis
    images = [
        f"nota_fiscal.{img_format}",
        f"lote.{img_format}",
        f"peso.{img_format}",
        f"placa.{img_format}"
    ]

    msg = {} # dicionario para armazenar as informacoes para o mes

    Image1 = Image.open(imagem) 
    croppedIm_NF = Image1.crop((770, 70, 820, 105))
    croppedIm_NF.save(f"nota_fiscal.{img_format}")

    croppedIm_Lote = Image1.crop((260, 420, 300, 440))
    croppedIm_Lote.save(f"lote.{img_format}")

    croppedIm_Peso = Image1.crop((770, 155, 840, 177))
    croppedIm_Peso.save(f"peso.{img_format}")

    croppedIm_Placa = Image1.crop((770, 260, 840, 285))
    croppedIm_Placa.save(f"placa.{img_format}")


    for img in images:
        file_name = img
        image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
        w = int(image.shape[1] * 1.5)
        h = int(image.shape[0] * 1.5)
        resized = cv2.resize(image, (w,h), interpolation = cv2.INTER_AREA)

        '''cv2.imshow(file_name, resized)
        cv2.waitKey(0)'''

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        custom_config = r'--oem 3 --psm 6'

        extracted_text = pytesseract.image_to_string(resized,lang='por',config=custom_config)
        extracted_text_upper = extracted_text.upper().replace(":","").replace(';',"") # passando o texto para maiusculo eretirando : e ;
        print(extracted_text_upper)

        data = (extracted_text_upper[:extracted_text_upper.index('\n')])
        msg[file_name.split(".")[0]] = data

    msg = json.dumps(msg)
    #print(type(msg))