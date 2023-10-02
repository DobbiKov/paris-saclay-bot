from openpyxl import load_workbook
import time
import xlwt
# file = 'table.xlsx'

arr_EN = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Excel():
    def get_file(self, file):
        # file = "./schedule-mi-3.xlsx"
        try:
            wb = load_workbook(file)
            self.wb = wb
            return wb
        except Exception as ex:
            print("Something went wrong while loading the file.")
            time.sleep(3)
            raise SystemExit(1)

    def get_sheet(self, sheet):

            for i in self.wb.sheetnames:
                print(f"{i}", end=" ")
            print()

            sheetName = sheet
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
    
    def get_formation_sheet(self, formation):
        sheets = {
            'L1-MI1': 'L1 MI-1',
            'L1-MI2': 'L1 MI-2',
            'L1-MI3': 'L1 MI-3',
            'L1-MI4': 'L1 MI-4',

            'LDD1-IM1': 'LDD1 IM-1',
            'LDD1-IM2': 'LDD1 IM-2',

            'L1-MP-A1': ' A1 ',
            'L1-MP-A2': 'A2',
            'L1-MP-A3': 'A3 ',
            'L1-MP-B1': 'B1 ',
            'L1-MP-B2': 'B2 ',

            'LDD1-MPSI-B3': 'B3 LDD1 MPSI',
            'LDD1-MPSI-B4': 'B4 LDD1 MPSI',
            'LDD1-MPSI-STAPS-B5': 'B5 LDD1 STAPS',
        }
        return sheets[formation]

    def get_formation_file(self, formation):
        files = {
            'L1-MI1': './Semainier_L1 MI_LDD1_IM_23-24-2.xlsx',
            'L1-MI2': './Semainier_L1 MI_LDD1_IM_23-24-2.xlsx',
            'L1-MI3': './Semainier_L1 MI_LDD1_IM_23-24-2.xlsx',
            'L1-MI4': './Semainier_L1 MI_LDD1_IM_23-24-2.xlsx',

            'LDD1-IM1': './Semainier_L1 MI_LDD1_IM_23-24-2.xlsx',
            'LDD1-IM2': './Semainier_L1 MI_LDD1_IM_23-24-2.xlsx',

            'L1-MP-A1': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',
            'L1-MP-A2': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',
            'L1-MP-A3': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',
            'L1-MP-B1': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',
            'L1-MP-B2': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',

            'LDD1-MPSI-B3': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',
            'LDD1-MPSI-B4': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',
            'LDD1-MPSI-STAPS-B5': './Semainier_L1 MP_LDD1 MPSI_STAPS_23-24.xlsx',
        }
        return files[formation]

    #     button1 = InlineKeyboardButton("L1-MI1", callback_data="choose_form:L1-MI1")
    # button2 = InlineKeyboardButton("L1-MI2", callback_data="choose_form:L1-MI2")
    # button3 = InlineKeyboardButton("L1-MI3", callback_data="choose_form:L1-MI3")
    # button4 = InlineKeyboardButton("L1-MI4", callback_data="choose_form:L1-MI4")


    # button5 = InlineKeyboardButton("LDD1-IM1", callback_data="choose_form:LDD1-IM1")
    # button6 = InlineKeyboardButton("LDD1-IM2", callback_data="choose_form:LDD1-IM2")

    # button7 = InlineKeyboardButton("L1-MP-A1", callback_data="choose_form:L1-MP-A1")
    # button8 = InlineKeyboardButton("L1-MP-A2", callback_data="choose_form:L1-MP-A2")
    # button9 = InlineKeyboardButton("L1-MP-A3", callback_data="choose_form:L1-MP-A3")
    # button10 = InlineKeyboardButton("L1-MP-B1", callback_data="choose_form:L1-MP-B1")
    # button11 = InlineKeyboardButton("L1-MP-B2", callback_data="choose_form:L1-MP-B2")

    # button12 = InlineKeyboardButton("LDD1-MPSI-B3", callback_data="choose_form:LDD1-MPSI-B3")
    # button13 = InlineKeyboardButton("LDD1-MPSI-B4", callback_data="choose_form:LDD1-MPSI-B4")
    # button14 = InlineKeyboardButton("LDD1-MPSI-STAPS-B5", callback_data="choose_form:LDD1-MPSI-STAPS-B5")

    # keyboard = InlineKeyboardMarkup()
    # keyboard.add(button1, button2, button3, button4)
    # keyboard.add(button5, button6)
    # keyboard.add(button7, button8, button9, button10, button11)
    # keyboard.add(button12, button13, button14)