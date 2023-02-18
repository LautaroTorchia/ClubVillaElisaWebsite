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


def generate_associate_card(associate, CARD_PATH, PROFILE_PIC_PATH, QR_PATH):
    """Generates the associate card"""
    from src.core.board.repositories.configuration import get_cfg
    from PIL import Image, ImageDraw, ImageFont, ImageOps

    if is_up_to_date(associate):
        up_to_date = "Al día"
    else:
        up_to_date = "Moroso"

    # draw using pillow
    FONT_PATH = os.path.join(os.getcwd(), "public", "fonts", "Roboto-Bold.ttf")
    FONT_TXT_PATH = os.path.join(os.getcwd(), "public", "fonts", "Roboto-Regular.ttf")
    card1 = Image.new("RGBA", (900, 500), "white")
    card = ImageOps.expand(card1, border=3, fill="black")
    draw = ImageDraw.Draw(card)

    profile_pic = Image.open(PROFILE_PIC_PATH)
    profile_pic = profile_pic.resize((200, 200))
    profile_pic = profile_pic.convert("RGBA")

    make_qr_code(associate, QR_PATH)
    qr = Image.open(QR_PATH)
    qr = qr.resize((200, 200))
    qr = qr.convert("RGBA")

    clubFont = ImageFont.truetype(FONT_PATH, size=40)
    titleFont = ImageFont.truetype(FONT_PATH, size=30)
    nameFont = ImageFont.truetype(FONT_TXT_PATH, size=20)

    draw.text((200, 10), "Club deportivo Villa Elisa", font=clubFont, fill="black")
    draw.line((0, 60, 900, 60), fill="black", width=2)

    card.paste(profile_pic, (70, 100), profile_pic)
    draw.text(
        (450, 70), f"{associate.name} {associate.surname}", (0, 0, 0), font=clubFont
    )
    draw.text((500, 150), f"DNI: {associate.DNI_number}", (0, 0, 0), font=titleFont)
    draw.text((500, 200), f"Socio: #{associate.id}", (0, 0, 0), font=titleFont)
    draw.text(
        (500, 250),
        f"Fecha alta: {associate.entry_date.day}/{associate.entry_date.month}/{associate.entry_date.year} ",
        (0, 0, 0),
        font=titleFont,
    )
    card.paste(qr, (500, 300), qr)

    draw.text((130, 350), "Estado: ", (0, 0, 0), font=titleFont)
    draw.text((130, 400), up_to_date, (0, 0, 0), font=titleFont)

    card.save(CARD_PATH)


def write_pdf_card(CARD_PATH, PDF_PATH):
    """Generates the associate card pdf"""
    from fpdf import FPDF
    from PIL import Image

    pdf = FPDF(format=(900, 500))
    pdf.add_page()

    img = Image.open(CARD_PATH)
    img = img.convert("RGB")
    pdf.image(CARD_PATH, 0, 0, 900, 500)

    pdf.output(PDF_PATH, "F")


# make qr code
def make_qr_code(associate, QR_PATH):
    import qrcode
    from flask import url_for

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(
        f"https://admin-grupo12.proyecto2022.linti.unlp.edu.ar{url_for('associate.club_card_view',id=associate.id)}"
    )
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(QR_PATH)
