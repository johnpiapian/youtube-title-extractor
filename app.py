import sys
import xlsxwriter
import extract_title

def createSpreadsheet(name, pl_id):
    workbook = xlsxwriter.Workbook(fr'{name}.xlsx')
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
    
    # get titles using the improted module
    titles = extract_title.getTitles(pl_id)

    row = 1
    for title in titles:
        worksheet.write(row, 0, title)
        row += 1

    max_width = len(max(titles, key=len))
    worksheet.set_column(0, 0, max_width)
    
    # Conclude the file
    workbook.close()

def app():
    # 1st: filename, 2nd: playlist_id, 3rd: spreadsheet's name
    arguments = sys.argv
    playlist_id = None
    spreadsheet_name = None

    # if empty give spreadsheet a default name
    if len(arguments) == 2:
        arguments.append("titles")

    if len(arguments) >= 3:
        playlist_id = arguments[1]
        spreadsheet_name = arguments[2]

        try:
            createSpreadsheet(spreadsheet_name, playlist_id)
        except:
            print("An unexpected error occured!")
    else:
        print("Invalid input!")  

      
app()