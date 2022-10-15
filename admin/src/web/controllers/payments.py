from flask import Blueprint, render_template, request, redirect, url_for,flash,send_file
from src.web.helpers.auth import login_required
from src.web.helpers.pagination import pagination_generator
from src.core.board import list_payments

payments_blueprint = Blueprint("payments", __name__, url_prefix="/pagos")


#listing payments
@payments_blueprint.route("/")
@login_required
def index():
    pairs=[("surname","Apellido")]
    if request.args.get("search"):
        paginated_query_data = pagination_generator(list_payments(request.args.get("column"),request.args.get("search")), request,"payments")
    else:
        paginated_query_data = pagination_generator(list_payments(), request,"payments")
    return render_template("payments/list.html", pairs=pairs,**paginated_query_data)