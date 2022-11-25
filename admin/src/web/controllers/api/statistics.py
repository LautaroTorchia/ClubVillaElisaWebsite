from src.core.board import associate_disciplines, Associate, list_all_associates
from flask import Blueprint, jsonify, request
from src.web.helpers.associate import is_up_to_date
from src.core.db import db

statistics_api_blueprint = Blueprint("statistics_api", __name__, url_prefix="/stats")


@statistics_api_blueprint.get("/associates")
def disciplines_by_gender():
    res = []
    relationship = db.session.query(associate_disciplines).all()
    relationship.sort(key=lambda x: x[1])
    associates = (
        db.session.query(Associate)
        .filter(Associate.disciplines.any(), Associate.deleted == False)
        .all()
    )
    for associate in associates:
        associate = associate.to_dict(disciplines=True)
        for discipline in associate["disciplines"]:
            discipline["associated_at"] = list(
                map(
                    lambda y: y[2],
                    filter(
                        lambda tuple: tuple[0] == associate["id"]
                        and tuple[1] == discipline["id"],
                        relationship,
                    ),
                )
            )[0].strftime("%Y-%m-%d %H:%M:%S.%f")
        res += [associate]
    try:
        return jsonify(
            {
                "data": res,
                "years": [
                    relationship[0][2].strftime("%Y"),
                    relationship[-1][2].strftime("%Y"),
                ],
            }
        )  # YYYY-MM-DDTHH:mm:ss.sssZ
    except:
        return jsonify({"data": [], "years": []})  # YYYY-MM-DDTHH:mm:ss.sssZ


@statistics_api_blueprint.get("/associates_up_to_date")
def associates_up_to_date():
    up_to_date = 0
    not_up_to_date = 0
    for associate in list_all_associates():
        if is_up_to_date(associate):
            up_to_date += 1
        else:
            not_up_to_date += 1
    return jsonify(
        {"data": {"up_to_date": up_to_date, "not_up_to_date": not_up_to_date}}
    )
