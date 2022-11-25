import os
from src.core.board.repositories.configuration import get_cfg
from werkzeug.utils import secure_filename
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file,
    session,
)
from src.core.board import (
    create_associate,
    delete_associate,
    get_associate_by_id,
    list_associates,
    update_associate,
    add_discipline_to_associate,
    remove_discipline_to_associate,
    get_discipline,
    list_all_associates,
    list_all_disciplines,
    update_associate_profile_pic,
)
from src.core.auth import (
    get_role,
    create_user,
    add_role_to_user,
)

from passlib.hash import sha256_crypt
from src.web.forms.associate import CreateAssociateForm, UpdateAssociateForm
from src.web.helpers.writers import write_csv_file, write_pdf_file
from src.web.helpers.auth import has_permission
from src.web.helpers.pagination import pagination_generator
from src.web.helpers.associate import (
    generate_associate_card,
    is_up_to_date,
    write_pdf_card,
)
from src.web.helpers.pagination import pagination_generator
from src.core.board import get_associate_by_id

associate_blueprint = Blueprint("associate", __name__, url_prefix="/asociados")


# Listing associates
@associate_blueprint.route("/")
@has_permission("associate_index")
def index():
    """Returns:
    HTML: List of associates.
    """
    pairs = [("surname", "Apellido"), ("true", "Activo"), ("false", "Inactivo")]

    if request.args.get("column") in ["true", "false"]:
        paginated_query_data = pagination_generator(
            list_associates("active", request.args.get("column")), request, "associates"
        )
    elif request.args.get("search"):
        paginated_query_data = pagination_generator(
            list_associates(request.args.get("column"), request.args.get("search")),
            request,
            "associates",
        )
    else:
        paginated_query_data = pagination_generator(
            list_associates(), request, "associates"
        )

    return render_template("associate/list.html", pairs=pairs, **paginated_query_data)


# adding associates
@associate_blueprint.get("/agregar")
@has_permission("associate_create")
def get_add():
    """Returns:
    HTML: Form to create an associate.
    """
    return render_template("associate/add.html", form=CreateAssociateForm())


@associate_blueprint.post("/agregar")
@has_permission("associate_create")
def post_add():
    """Returns:
    HTML: Redirect to associate list.
    """
    form = CreateAssociateForm(request.form)
    if form.validate():
        user_dict = dict(form.data)
        user_dict["username"] = user_dict["DNI_number"]
        user_dict["password"] = sha256_crypt.encrypt(user_dict["password"])
        user = create_user(user_dict)
        add_role_to_user(user, get_role("Socio"))
        associate = create_associate(form.data)
        flash(f"Se agregó {associate}", category="alert alert-info")
        return redirect(url_for("associate.index"))
    return render_template("associate/add.html", form=form)


# deleting associates
@associate_blueprint.post("/borrar/<id>")
@has_permission("associate_destroy")
def delete(id):
    """Args:
        id (int): id of the associate
    Returns:
        HTML: Redirect to associate list.
    """
    flash(f"Se elimino al asociado satisfactoriamente", category="alert alert-warning")
    delete_associate(id)
    return redirect(url_for("associate.index"))


# updating associates
@associate_blueprint.get("/actualizar/<id>")
@has_permission("associate_update")
def get_update(id):
    """Args:
        id (int): id of the associate
    Returns:
        _type_: _description_
    """
    associate = get_associate_by_id(id)
    form = UpdateAssociateForm(obj=associate)
    return render_template("associate/update.html", form=form)


# updating associates
@associate_blueprint.post("/actualizar/<id>")
@has_permission("associate_update")
def post_update(id):
    """Args:
        id (int): id of the associate
    Returns:
        HTML: Redirect to associate list.
    """
    form = UpdateAssociateForm(request.form)
    if form.validate():
        flash(f"Se actualizó {get_associate_by_id(id)}", category="alert alert-info")
        update_associate(form.data, id)
        return redirect(url_for("associate.index"))
    return render_template("associate/add.html", form=form)


# csv_writing associates
@associate_blueprint.get("/creador_csv")
@has_permission("associate_index")
def write_csv():
    """Returns:
    CSV: List of associates.
    """
    args = dict(request.args)
    CSV_PATH = os.path.join(os.getcwd(), "public", "Associate_list_report.csv")
    if request.args.get("search"):
        write_csv_file(CSV_PATH, list_all_associates(args["column"], args["search"]))
    else:
        write_csv_file(CSV_PATH, list_all_associates())

    return send_file(CSV_PATH, as_attachment=True)


# pdf_writing associates
@associate_blueprint.get("/creador_pdf")
@has_permission("associate_index")
def write_pdf():
    """Returns:
    PDF: List of associates.
    """
    args = dict(request.args)
    PDF_PATH = os.path.join(os.getcwd(), "public", "Associate_list_report.pdf")
    if request.args.get("search"):
        write_pdf_file(PDF_PATH, list_all_associates(args["column"], args["search"]))
    else:
        write_pdf_file(PDF_PATH, list_all_associates())

    return send_file(PDF_PATH, as_attachment=True)


# add a new discipline to the associate
@associate_blueprint.get("/agregar/<id>")
@has_permission("associate_update")
def add_discipline(id):
    """Args:
        id (int): id of the associate
    Returns:
        HTML: Redirect to associate list.
    """
    associate = get_associate_by_id(id)
    if is_up_to_date(associate):
        pairs = [("name", "Nombre")]

        if request.args.get("search"):
            disciplines = list_all_disciplines(
                request.args.get("column"), request.args.get("search")
            )
        else:
            disciplines = list_all_disciplines()
        return render_template(
            "associate/add_discipline.html",
            pairs=pairs,
            disciplines=disciplines,
            associate=associate,
            currency=get_cfg().currency,
        )

    else:
        flash(
            f"El asociado {associate.name} {associate.surname} esta moroso, no se le puede agregar una disciplina",
            category="alert alert-warning",
        )
        return redirect(url_for("associate.index"))


# add a discipline to the associate
@associate_blueprint.post("/agregar_disciplina/<id>/<discipline_id>")
@has_permission("associate_update")
def register_discipline(id, discipline_id):
    """Args:
        id (int): id of the associate
        discipline_id (int): id of the discipline to add to the associate
    Returns:
        HTML: Redirect to associate list.
    """
    associate = get_associate_by_id(id)
    discipline = get_discipline(discipline_id)

    if discipline.available:
        add_discipline_to_associate(associate, discipline)
        flash(
            f"Se agregó la disciplina {discipline.name} al asociado {associate}",
            category="alert alert-info",
        )
        return redirect(url_for("associate.add_discipline", id=id))

    flash(
        f"La disciplina {discipline.name} no está disponible",
        category="alert alert-danger",
    )
    return redirect(url_for("associate.add_discipline", id=id))


# delete a discipline from the associate
@associate_blueprint.post("/quitar_disciplina/<id>/<discipline_id>")
@has_permission("associate_update")
def delete_discipline(id, discipline_id):
    """Args:
        id (int): id of the associate
        discipline_id (int): id of the discipline to delete from the associate
    Returns:
        HTML: Redirect to associate list.
    """
    associate = get_associate_by_id(id)
    discipline = get_discipline(discipline_id)
    remove_discipline_to_associate(associate, discipline)
    flash(
        f"Se eliminó la disciplina {discipline} del asociado {associate.name} {associate.surname}",
        category="alert alert-info",
    )
    return redirect(url_for("associate.add_discipline", id=id))


# view the associate club card
@associate_blueprint.get("/carnet/<id>")
@has_permission("associate_index")
def club_card_view(id):
    """Args:
        id (int): id of the associate
    Returns:
        HTML: Redirect to associate list.
    """
    associate = get_associate_by_id(id)
    CARD_PATH = os.path.join(os.getcwd(), "public", "associate_card.png")
    QR_PATH = os.path.join(os.getcwd(), "public", "qr.png")
    PROFILE_PIC_PATH = associate.profile_pic
    generate_associate_card(associate, CARD_PATH, PROFILE_PIC_PATH, QR_PATH)
    return render_template("associate/club_card.html", associate=associate)


@associate_blueprint.post("/carnet/<id>")
@has_permission("associate_index")
def club_card_view_post(id):
    """Args:
        id (int): id of the associate
    Returns:
        HTML: Redirect to associate list.
    """
    associate = get_associate_by_id(id)
    image_data = request.files["image"]
    if image_data.filename == "":
        flash(
            "No se subio ninguna foto",
            category="alert alert-danger",
        )
        return redirect(request.url)

    image_data.filename = f"{associate.name}_{associate.surname}_{image_data.filename}"
    secure_filename(image_data.filename)
    profile_path = os.path.join(
        os.getcwd(), "public", "associate_pics", image_data.filename
    )
    image_data.save(profile_path)
    associate.profile_pic = profile_path
    update_associate_profile_pic(associate)

    return redirect(url_for("associate.club_card_view", id=id))


# download the card
@associate_blueprint.post("/carnet_descargar/<id>")
@has_permission("associate_create")
def club_card_download(id):
    """Args:
        id (int): id of the associate
    Returns:
        HTML: Redirect to associate list.
    """
    CARD_PATH = os.path.join(os.getcwd(), "public", "associate_card.png")
    return send_file(CARD_PATH, as_attachment=True)


# download the card
@associate_blueprint.post("/carnet_descargar_pdf/<id>")
@has_permission("associate_create")
def club_card_download_pdf(id):
    """Args:
        id (int): id of the associate
    Returns:
        HTML: Redirect to associate list.
    """
    CARD_PATH = os.path.join(os.getcwd(), "public", "associate_card.png")
    PDF_CARD_PATH = os.path.join(os.getcwd(), "public", "associate_card.pdf")

    write_pdf_card(CARD_PATH, PDF_CARD_PATH)
    return send_file(PDF_CARD_PATH, as_attachment=True)
