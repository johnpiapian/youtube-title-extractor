import env
import os
from ytextractor import SpreadSheet, CSV, FileManager

class TestExtractor:
    filename = 'test'
    titles = ['a', 'b', 'c']

    def test_spreadsheet(self):
        spreadsheet = SpreadSheet(self.filename, self.titles)
        spreadsheet.generate()

        assert os.path.exists(fr'{self.filename}.xlsx')
        
        os.remove(fr'{self.filename}.xlsx')

    def test_csv(self):
        csv = CSV(self.filename, self.titles)
        csv.generate()

        assert os.path.exists(fr'{self.filename}.csv')

        os.remove(fr'{self.filename}.csv')

    def test_file_manager(self):
        file_manager = FileManager(self.filename, self.titles)
        file_manager.generate_xlsx()
        file_manager.generate_csv()

        assert os.path.exists(fr'{self.filename}.xlsx')
        assert os.path.exists(fr'{self.filename}.csv')

        os.remove(fr'{self.filename}.xlsx')
        os.remove(fr'{self.filename}.csv')