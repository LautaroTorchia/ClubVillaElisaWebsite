import csv 


def write_csv_file(filename,data):
    """
    Write a csv file with the data provided
    """
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Nombre","Apellido","DNI","Email","Direccion","Estado","Telefono"])
        for associate in data:
            writer.writerow([associate.name,associate.surname,associate.DNI_number,associate.email,associate.address,associate.active,associate.phone_number])
    
        