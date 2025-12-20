from openpyxl import load_workbook
import os

def read_excel(path, sheet_name, row, col):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Excel file not found: {path}")

    if not path.endswith(".xlsx"):
        raise ValueError(f"Invalid Excel file format (must be .xlsx): {path}")

    workbook = load_workbook(path)
    sheet = workbook[sheet_name]
    return sheet.cell(row=row, column=col).value
