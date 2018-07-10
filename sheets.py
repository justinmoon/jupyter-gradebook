import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
key = "https://docs.google.com/spreadsheets/d/13iWTp5TkuuZUxjLgdfk3Y_Aqy4CatIlhs54ZfrJ3xes"
key = "gradebook"
wks = gc.open(key).sheet1

wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = wks.range('A1:B7')
