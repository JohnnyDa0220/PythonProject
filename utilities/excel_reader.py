from openpyxl import load_workbook

def read_excel(path, sheetname, row, col):
    workbook = load_workbook(path)
    sheet = workbook[sheetname]
    value = sheet.cell(row=row, column=col).value
    return value