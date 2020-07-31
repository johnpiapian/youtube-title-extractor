import title
import xlsxwriter

workbook = xlsxwriter.Workbook('titles.xlsx')
worksheet = workbook.add_worksheet()

# Cell format template
cell_format = workbook.add_format()
cell_format.set_bold()
cell_format.set_align('center')
cell_format.set_align('vcenter')

# Add title
worksheet.write('A1', 'Video Titles', cell_format)

row = 1
max_width = 0

for title in title.vid_titles:
    worksheet.write(row, 0, title)

    if len(title) > max_width:
        max_width = len(title)

    row += 1

# Last formatting/styling
worksheet.set_default_row(20)
worksheet.set_default_row(hide_unused_rows=True)
worksheet.set_column(0, 0, max_width)


workbook.close()