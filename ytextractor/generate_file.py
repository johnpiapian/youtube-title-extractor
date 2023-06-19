import xlsxwriter
import csv

class SpreadSheet:
    def __init__(self, name, videos):
        self.name = name
        self.videos = videos

    def generate(self):
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

        # Select fields to be written
        selected_fields = [{
            'Title': video['title'],
            'Url': f'https://www.youtube.com/watch?v={video["videoId"]}'
            } for video in self.videos]

        # Write header
        headers = list(selected_fields[0].keys())
        for idx, header in enumerate(headers):
            worksheet.write(0, idx, header, cell_format)

        # Write data rows
        for row_num, video in enumerate(selected_fields, start=1):  # start=1 to skip header row
            for col_num, (key, value) in enumerate(video.items()):
                worksheet.write(row_num, col_num, value)

        # Conclude the file
        workbook.close()

class CSV:
    def __init__(self, name, videos):
        self.name = name
        self.videos = videos

    def generate(self):
        # Select fields to be written
        selected_fields = [{
            'Title': video['title'], 
            'Url': f'https://www.youtube.com/watch?v={video["videoId"]}'
            } for video in self.videos]

        with open(fr'{self.name}.csv', 'w', newline='') as file:
            # Get fieldnames dynamically from the first dictionary in selected_fields
            fieldnames = list(selected_fields[0].keys()) if selected_fields else []

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(selected_fields)

class FileManager:
    def __init__(self, name, videos):
        self.name = name
        self.videos = videos
    
    def generate_xlsx(self):
        spreadsheet = SpreadSheet(self.name, self.videos)
        spreadsheet.generate()
    
    def generate_csv(self):
        csv = CSV(self.name, self.videos)
        csv.generate()