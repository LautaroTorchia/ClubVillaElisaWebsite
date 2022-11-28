from flask import Blueprint, jsonify
from src.web.helpers.build_response import response
from src.core.board import get_associate_by_DNI
from src.core.auth import get_user_by
from datetime import datetime
from src.web.helpers.auth import jwt_required
from src.web.helpers.associate import is_up_to_date
from src.web.helpers.associate import generate_associate_card
import base64
import os
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

associate_api_blueprint = Blueprint("associate_api", __name__, url_prefix="")


@associate_api_blueprint.get("/disciplines/")
@jwt_required()
def index_api():
    """Args:
        id (int): id of the associate
    Returns:
        JSON: list of disciplines
    """
    current_user = get_jwt_identity()
    user = get_user_by(current_user)
    associate = get_associate_by_DNI(user.username)
    if associate.disciplines:
        disciplines = [
            {
                "name": discipline.name,
                "days": discipline.dates,
                "category": discipline.category,
                "teacher": discipline.instructors,
                "price": discipline.monthly_cost,
            }
            for discipline in associate.disciplines
        ]
        return response(200, disciplines)
    else:
        return response(200, [])


# make an api for the associate card
@associate_api_blueprint.get("/license/")
@jwt_required()
def associate_card_api():
    """Args:
        id (int): id of the associate
    Returns:
        JSON: associate card
    """
    current_user = get_jwt_identity()
    user = get_user_by(current_user)
    associate = get_associate_by_DNI(user.username)
    if associate:
        CARD_PATH = os.path.join(os.getcwd(), "public", "associate_card.png")
        QR_PATH = os.path.join(os.getcwd(), "public", "qr.png")
        generate_associate_card(associate, CARD_PATH, associate.profile_pic, QR_PATH)

        with open(associate.profile_pic, "rb") as img_file:
            profile_pic_in64 = base64.b64encode(img_file.read())
        with open(CARD_PATH, "rb") as img_file:
            card_in64 = base64.b64encode(img_file.read())
        card_data = {
            "name": associate.name,
            "surname": associate.surname,
            "dni": associate.DNI_number,
            "entry_date": f"{associate.entry_date.day}/{associate.entry_date.month}/{associate.entry_date.year}",
            "associate_number": associate.id,
            "status": "Al dia" if is_up_to_date(associate) else "Moroso",
            "profile_pic": str(profile_pic_in64.decode("utf-8")),
            "associate_card": str(card_in64.decode("utf-8")),
        }
        return response(200, card_data)
    return response(200, [])
