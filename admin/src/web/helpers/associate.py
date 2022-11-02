from datetime import datetime
import os
from src.core.board.repositories.payments import get_last_fee_paid


def is_up_to_date(associate):
    """Returns true if the associate is not in debt"""
    payment = get_last_fee_paid(associate)

    if payment.installment_number == 0:
        if (
            datetime.now().year == associate.entry_date.year
            and datetime.now().month == associate.entry_date.month
        ):
            return True

    elif (
        datetime.now().year == payment.date.year
        and datetime.now().month == payment.date.month
    ):
        return True

    elif (
        datetime.now().year == payment.date.year
        and datetime.now().month == payment.date.month + 1
        and datetime.now().day <= 10
        or datetime.now().year == payment.date.year + 1
        and datetime.now().month + 11 == payment.date.month
        and datetime.now().day <= 10
    ):
        return True

    return False



def generate_associate_card(associate,CARD_PATH):
    """Generates the associate card"""
    from src.core.board.repositories.configuration import get_cfg
    from PIL import Image, ImageDraw, ImageFont,ImageOps

    cfg = get_cfg()

    if associate.active:
        status = "Activo"
    else:
        status = "Inactivo"

    if is_up_to_date(associate):
        up_to_date = "Al día"
    else:
        up_to_date = "Moroso"
        

    #draw using pillow
    FONT_PATH = os.path.join(os.getcwd(), "public", "fonts", "Roboto-Bold.ttf")
    FONT_TXT_PATH = os.path.join(os.getcwd(), "public", "fonts", "Roboto-Regular.ttf")
    card1 = Image.new("RGBA", (900, 500), "white")
    card = ImageOps.expand(card1,border=1,fill='black')
    draw = ImageDraw.Draw(card)
    profile_pic = Image.open(os.path.join(os.getcwd(), "public", "profile_icon.png"))
    
    profile_pic = profile_pic.resize((200, 200))
    profile_pic = profile_pic.convert("RGBA")
    
    clubFont = ImageFont.truetype(FONT_PATH, size=40)
    titleFont = ImageFont.truetype(FONT_PATH, size=30)
    nameFont = ImageFont.truetype(FONT_TXT_PATH, size=20)
    
    draw.text((200, 10), "Club deportivo Villa Elisa", font=clubFont, fill="black")
    draw.line((0, 60, 850, 60), fill="black", width=2)
    
    card.paste(profile_pic, (70, 100), profile_pic)
    draw.text((450, 100), f"{associate.name} {associate.surname}", (0, 0, 0), font=clubFont)
    draw.text((500, 200), f"DNI: {associate.DNI_number}", (0, 0, 0), font=titleFont)
    draw.text((500, 250), f"Socio: #{associate.id}", (0, 0, 0), font=titleFont)
    draw.text((500, 300), f"Fecha alta: {associate.entry_date.day}/{associate.entry_date.month}/{associate.entry_date.year} ", (0, 0, 0), font=titleFont)

    
    draw.text((130, 350), "Estado: ", (0, 0, 0), font=titleFont)
    draw.text((130, 400), up_to_date, (0, 0, 0), font=titleFont)
    

    card.save(CARD_PATH)
    

def write_pdf_card(CARD_PATH, PDF_PATH,CARD_PATH_2):
    """Generates the associate card pdf"""
    from fpdf import FPDF
    from PIL import Image

    pdf = FPDF()
    pdf.add_page()
    #resize image to fit in pdf
    img = Image.open(CARD_PATH)
    img = img.resize((900, 500), Image.ANTIALIAS)
    img.save(CARD_PATH_2)
    pdf.image(CARD_PATH_2, 0, 0, 210, 297)
    
    pdf.output(PDF_PATH, "F")