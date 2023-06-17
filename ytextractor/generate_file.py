import xlsxwriter

class SpreadSheet:
    def __init__(self, name):
        self.name = name

    def generate(self, titles):
        workbook = xlsxwriter.Workbook(fr'{self.name}.xlsx')
        worksheet = workbook.add_worksheet()

        # General worksheet formatting/styling
        worksheet.set_default_row(20)
        worksheet.set_default_row(hide_unused_rows=True)

        # Cell format template
        cell_format = workbook.add_format()
        cell_format.set_bold()
        cell_format.set_align('center')
        cell_format.set_align('vcenter')

        # Add cell title
        worksheet.write('A1', 'Video Titles', cell_format)

        row = 1
        for title in titles:
            worksheet.write(row, 0, title)
            row += 1

        max_width = len(max(titles, key=len))
        worksheet.set_column(0, 0, max_width)

        # Conclude the file
        workbook.close()

class CSV:
    def __init__(self, name):
        self.name = name

    def generate(self, titles):
        with open(fr'{self.name}.csv', 'w') as file:
            for title in titles:
                file.write(f'{title}\n')

class FileManager:
    def __init__(self, name, titles):
        self.name = name
        self.titles = titles
    
    def generate_xlsx(self):
        spreadsheet = SpreadSheet(self.name)
        spreadsheet.generate(self.titles)
    
    def generate_csv(self):
        csv = CSV(self.name)
        csv.generate(self.titles)