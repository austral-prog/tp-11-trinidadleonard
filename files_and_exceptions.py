def read_file_to_dict(data):
    try:
		with open(data, "r") as archivo:
			contenido = archivo.read().strip()
			ventas = contenido.split(";")
			dictionario = dict()

			for venta in ventas:
				producto, valor_str = venta.split(":")
				valor = float(valor_str)

				if producto not in dictionario:
					dictionario[producto] = [valor]
				else:
					dictionario[producto].append(valor)
			return dictionario

	except FileNotFoundError:
		print(f"Error: el archivo {data} no fue encontrado.")
    


def process_dict(dictionario):
    for producto, values in dictionario.items():
		total = sum(values)
		promedio = total / len(values)
		print(f"{producto}: ventas totales ${total}, promedio ${promedio}")
