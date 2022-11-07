import xlrd
from library.config import Config


class ReadExcel:

    def read_testdata(self):
        wb = xlrd.open_workbook(Config.test_data_path)
        ws = wb.sheet_by_name(Config.PROFILE_TESTDATA_SHEET)
        columns = ws.ncols
        rows = ws.get_rows()  # generator object
        header = next(rows)
        data = []
        for row in rows:
            values = ()
            for j in range(columns):
                values += (row[j].value,)
            data.append(values)
        return data

    def read_locators(self, sheetname):
        wb = xlrd.open_workbook(Config.test_locator_path)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)

        return d


n = ReadExcel()
h = n.read_locators(Config.PROFILE_LOCATOR_SHEET)
# print(h)
locator = h["Add_to_Story"]
print(locator)