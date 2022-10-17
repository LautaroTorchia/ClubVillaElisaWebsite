from datetime import datetime
import functools
import os
from PIL import Image,ImageDraw,ImageFont

#get disciplines_fee_amount
def disciplines_fee_amount(associate):
    """Args:
        associate (Associate): Associate object
    Returns:
        float: Total amount of disciplines fees
    """    
    return functools.reduce(lambda x,y: x+y.monthly_cost,associate.disciplines,0)


def make_receipt(payment,RCPT_PATH):
    """Args:
        payment (Payment): Payment object
        RCPT_PATH (str): Path to save the receipt
    """    
    #draw a receipt for a payment
    dict_meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
    FONT_PATH=os.path.join(os.getcwd(),"public","font","Roboto-Bold.ttf")
    receipt=Image.new("RGB",(1000,400),"white")
    draw=ImageDraw.Draw(receipt)
    titleFont=ImageFont.truetype(FONT_PATH,size=25)
    nameFont=ImageFont.truetype(FONT_PATH,size=20)
    
    logo=Image.open(os.path.join(os.getcwd(),"public","img","logo_club.png"))
    receipt.paste(logo,(0,0))
    
    draw.text((215,10),f"Recibo de pago #{payment.installment_number}",fill="black",font=titleFont)
    draw.text((800,20),f"Fecha: {datetime.now().strftime('%d/%m/%Y')}",fill="black",font=nameFont)
    draw.text((215,125),f"Recibimos de : {payment.associate.name} {payment.associate.surname}",fill="black",font=nameFont)
    draw.text((215,175),f"El importe en pesos de ${payment.amount}",fill="black",font=nameFont)
    draw.text((215,225),f"Por concepto de cuota societaria Para el mes de {dict_meses[payment.date.month]} {payment.date.year}",fill="black",font=nameFont)
    receipt.save(RCPT_PATH)

