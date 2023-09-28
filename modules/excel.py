import pandas as pd
from openpyxl import load_workbook
import time
import xlwt
# file = 'table.xlsx'

arr_EN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Excel():
    def get_file(self):
        file = "./schedule-mi-3.xlsx"
        try:
            wb = load_workbook(file)
            self.wb = wb
            return wb
        except Exception as ex:
            print("Something went wrong while loading the file.")
            time.sleep(3)
            raise SystemExit(1)

    def get_sheet(self):

            # for i in self.wb.sheetnames:
            #     print(f"{i}", end=" ")
            # print()

            sheetName = "Sheet1"
            try:
                sheet = self.wb[sheetName]
                self.sheet = sheet
                return sheet

            except Exception as ex:
                print("Something went wrong with a sheet.")
                time.sleep(3)
                raise SystemExit(1)

    def get_data(self, field, row):
        return self.sheet[f"{field}{row}"].value
    def get_data_by_text(self, a):
        return self.sheet[a].value