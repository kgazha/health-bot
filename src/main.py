from src.excel.excel_handler import ExcelHandler


filename = r"C:\Users\gazhakv\Documents\Вопросы  Робот  v17.xlsx"
excel_parser = ExcelHandler()
excel_parser.load_data_source(filename)
df = excel_parser.extract_data()
df = df.iloc[:-1, :3]
df['cleaned_samples'] = None
df['cleaned_answers'] = None
# print(df.columns, df.shape)
print(df)
