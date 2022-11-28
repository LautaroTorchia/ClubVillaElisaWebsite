from datetime import datetime
import functools
import os
from PIL import Image, ImageDraw, ImageFont
from src.core.board.repositories.configuration import get_cfg

# get disciplines_fee_amount
def disciplines_fee_amount(associate):
    """Args:
        associate (Associate): Associate object
    Returns:
        float: Total amount of disciplines fees
    """
    return functools.reduce(lambda x, y: x + y.monthly_cost, associate.disciplines, 0)


def build_payment(last_fee, associate):
    """
        builds new fee to pay based on last fee paid
    Args:
        last_fee (Fee): Last fee paid by the associate
    Returns:
        flash_number (int): indicator of wich flash message to show, 1 for already paid,
        2 for successfull previous month payment, 3 for succesfull payment
        paid_latest (bool): indicator of if the associate has paid the latest fee
        fee_date (datetime): date of the new fee
        amount  (float): amount of the new fee
    """
    config = get_cfg()
    amount = disciplines_fee_amount(associate) + config.base_fee
    paid_late = False
    fee_date = datetime.now()

    if last_fee.installment_number != 0:  # if the associate has paid at least one fee

        if (
            last_fee.date.year == datetime.now().year
            and last_fee.date.month == datetime.now().month
        ):  # if the last fee was paid this month
            flash_number = 1

        elif (
            last_fee.date.year == datetime.now().year
            and datetime.now().month >= last_fee.date.month + 2
        ):  # if the last fee was paid more than one month ago
            flash_number = 2
            amount += amount * (config.due_fee / 100)
            fee_date = last_fee.date.replace(month=last_fee.date.month + 1)
            paid_late = True

        elif (
            last_fee.date.year + 1 == datetime.now().year
            and datetime.now().month + 11 > last_fee.date.month
        ):  # if the last fee was paid more than one month ago but year changed
            flash_number = 2
            amount += amount * (config.due_fee / 100)
            if last_fee.date.month == 12:
                fee_date = last_fee.date.replace(year=last_fee.date.year + 1, month=1)
            else:
                fee_date = last_fee.date.replace(month=last_fee.date.month + 1)
            paid_late = True

        elif (
            datetime.now().day > 10
        ):  # if the person is paying after the 10th of the month
            paid_late = True
            amount += amount * (config.due_fee / 100)
            flash_number = 3

    elif datetime.now().day > 10:  # if the person is paying after the 10th of the month
        paid_late = True
        amount += amount * (config.due_fee / 100)
        flash_number = 3

    else:  # if the associate has not paid any fee
        flash_number = 3

    return flash_number, paid_late, fee_date, amount


def make_receipt(payment, RCPT_PATH):
    """Builds a personalized PNG receipt file
    Args:
        payment (Payment): Payment object
        RCPT_PATH (str): Path to save the receipt
    """
    # draw a receipt for a payment
    dict_meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    FONT_PATH = os.path.join(os.getcwd(), "public", "fonts", "Roboto-Bold.ttf")
    FONT_TXT_PATH = os.path.join(os.getcwd(), "public", "fonts", "Roboto-Regular.ttf")
    receipt = Image.new("RGBA", (850, 300), "white")
    draw = ImageDraw.Draw(receipt)
    titleFont = ImageFont.truetype(FONT_PATH, size=25)
    nameFont = ImageFont.truetype(FONT_TXT_PATH, size=20)

    logo = Image.open(os.path.join(os.getcwd(), "public", "img", "logo_club.png"))
    logo = logo.convert("RGBA")
    receipt.paste(logo, (15, 40), logo)

    from src.core.board.repositories.configuration import get_cfg

    draw.text(
        (230, 10),
        f"{get_cfg().payment_header} #{payment.installment_number}",
        fill="black",
        font=titleFont,
    )
    draw.text(
        (615, 20),
        f"Fecha: {datetime.now().strftime('%d/%m/%Y')}",
        fill="black",
        font=nameFont,
    )
    draw.text(
        (230, 125),
        f"Recibimos de : {payment.associate.name} {payment.associate.surname}",
        fill="black",
        font=nameFont,
    )
    draw.text(
        (230, 175),
        f"el importe ${payment.amount} {get_cfg().currency}",
        fill="black",
        font=nameFont,
    )
    draw.text(
        (230, 225),
        f"Por el concepto de cuota societaria mes {dict_meses[payment.date.month]} {payment.date.year}",
        fill="black",
        font=nameFont,
    )
    receipt.save(RCPT_PATH)
