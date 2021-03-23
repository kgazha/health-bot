from src.excel_parser import ExcelParser


full_file_name = r"C:\Users\gazhakv\Documents\Вопросы  Робот  v17.xlsx"
excelParser = ExcelParser()
excelParser.load_data_source(full_file_name)
data = excelParser.extract_data().iloc[:-1, :3]
print(data)
