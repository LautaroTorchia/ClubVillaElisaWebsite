import csv
from fpdf import FPDF


def write_csv_file(filename, data):
    """Args:
    filename (str): Name of the file to be written
    data (list): Data to be written
    """
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(
            ["Nombre", "Apellido", "DNI", "Email", "Direccion", "Estado", "Telefono"]
        )
        for associate in data:
            writer.writerow(
                [
                    associate.name,
                    associate.surname,
                    associate.DNI_number,
                    associate.email,
                    associate.address,
                    "Activo" if associate.active else "Inactivo",
                    associate.phone_number,
                ]
            )


class PDF(FPDF):
    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font("Arial", "I", 8)
        # Print centered page number
        self.line(10, 282, 200, 282)
        self.cell(0, 10, "Página %s" % self.page_no(), 0, 0, "L")


def write_pdf_file(filename, data):
    """Args:
    filename (str): Name of the file to be written
    data (list): Data to be written
    """
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=25, style="B")

    pdf.set_fill_color(181, 161, 102)
    # create a cell
    pdf.cell(190, 30, txt="Club Deportivo Villa Elisa", ln=1, align="C")

    # add another cell
    pdf.set_font("Arial", size=15)
    pdf.cell(190, 20, txt="Reporte completo del listado de asociados", ln=2, align="C")

    pdf.set_font("Arial", size=12)
    for associate in data:
        pdf.cell(
            190, 6, txt="Información personal", border=1, ln=1, align="C", fill=True
        )
        pdf.multi_cell(
            190,
            7,
            txt=f"""Nombre: {associate.name} {associate.surname}\nDNI: {associate.DNI_number}\nEmail: {associate.email}\nDireccion: {associate.address}\nEstado: {"Activo" if associate.active else "Inactivo"}\nTelefono: {associate.phone_number}""",
            border=1,
            align="L",
        )
        pdf.ln(6)

    pdf.output(filename)
