from core.auth.repositories.permission import get_permission
from src.core.auth import (
    create_user,
    get_by_usr_and_pwd,
    create_role,
    get_role,
    add_role_to_user,
)
from src.core.board.repositories.discipline import add_discipline
from src.core.board.repositories.associate import create_associate
from passlib.hash import sha256_crypt


def run():
    if get_role("Admin") is None:
        create_role("Admin")
    if get_role("Operario") is None:
        create_role("Operario")
    if get_role("Usuario") is None:
        create_role("Usuario")

    if get_by_usr_and_pwd("admin", "1234") is None:
        create_user(
            {
                "first_name": "admin",
                "last_name": "admin",
                "email": "admin@villaelisa.com",
                "username": "admin",
                "password": sha256_crypt.encrypt("1234"),
            }
        )
        add_role_to_user(get_by_usr_and_pwd("admin", "1234"), get_role("Admin"))


def populate():
    names = ["Juan", "Pablo", "Maria", "Diana", "Horacio", "Pedro", "Kevin", "César"]
    last_names = [
        "Perez",
        "Gonzalez",
        "Garcia",
        "Rodriguez",
        "Lopez",
        "Martinez",
        "Hernandez",
        "Gomez",
    ]
    emails = [
        "juan@gmail.com",
        "pablo@gmail.com",
        "maria@gmail.com",
        "diana@gmail.com",
        "horacio@gmail.com",
        "pedro@gmail.com",
        "kevin@gmail.com",
        "cesar@gmail.com",
    ]
    more_emails = [f"{last_name.lower()}@gmail.com" for last_name in last_names]
    usernames = [
        "juan",
        "pablo",
        "maria",
        "diana",
        "pedro",
        "horacio",
        "kevin",
        "cesar",
    ]
    passwords = ["1234", "1234", "1234", "1234", "1234", "1234", "1234", "1234"]

    dicipline_name = [
        "Futbol",
        "Basquetbol",
        "Voleibol",
        "Natacion",
        "Atletismo",
        "Tenis",
        "Beisbol",
        "Softbol",
    ]
    dicipline_category = [
        "12 a 14 años",
        "16 a 20 años",
        "16 a 20 años",
        "10 a 12 años",
        "20 a 26 años",
        "20 a 26 años",
        "14 a 18 años",
        "12 a 14 años",
    ]
    instructors = [
        "Juan",
        "Pablo",
        "Maria",
        "Diana",
        "Horacio",
        "Pedro",
        "Kevin",
        "César",
    ]
    days_and_hours = [
        "Lunes 6:00pm - 8:00pm",
        "Martes 6:00pm - 8:00pm",
        "Miercoles 6:00pm - 8:00pm",
        "Lunes 2:00pm - 4:00pm",
        "Viernes 6:00pm - 8:00pm",
        "Sabado 6:00pm - 8:00pm",
        "Martes 4:00pm - 6:00pm",
        "Jueves 4:00pm - 6:00pm",
    ]
    monthly_cost = [800, 800, 800, 600, 800, 600, 800, 600]

    dni = [
        22583743,
        46583754,
        20583743,
        42583443,
        28582754,
        30583741,
        14583743,
        23683784,
    ]
    address = [
        "Calle 1",
        "Calle 2",
        "Calle 3",
        "Calle 4",
        "Calle 5",
        "Calle 6",
        "Calle 7",
        "Calle 8",
    ]
    telephones = [
        22123456,
        22123457,
        22123458,
        22123459,
        22123460,
        22123461,
        22123462,
        22123463,
    ]
    genders = ["male", "male", "female", "other", "male", "male", "other", "male"]

    try:
        for i in range(0, 7):
            create_user(
                {
                    "first_name": names[i],
                    "last_name": last_names[i],
                    "email": emails[i],
                    "username": usernames[i],
                    "password": sha256_crypt.encrypt(passwords[i]),
                }
            )
            add_discipline(
                {
                    "name": dicipline_name[i],
                    "category": dicipline_category[i],
                    "instructors": instructors[i],
                    "dates": days_and_hours[i],
                    "monthly_cost": monthly_cost[i],
                    "currency": "Pesos",
                    "available": True,
                }
            )
            create_associate(
                {
                    "DNI_number": dni[i],
                    "DNI_type": "DNI",
                    "name": names[i],
                    "surname": last_names[i],
                    "email": more_emails[i],
                    "gender": genders[i],
                    "address": address[i],
                    "phone_number": telephones[i],
                }
            )
    except:
        pass
