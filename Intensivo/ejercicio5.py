import pandas

source = r'.xlsx' # Agregar ruta del archivo Excel a convertir
file = r'archivo.csv'

excel_reader = pandas.read_excel(source)
csv_file = excel_reader.to_csv(file, index= True, header=True, encoding='utf-8')
