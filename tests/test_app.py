import os
import subprocess

class TestApp:
    cmd = "python app.py"
    arguments = { "playlist_id": "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU", "file_name": "titles", "file_type": "xlsx" }

    def test_app_create(self):
        full_cmd = "{} {} {} {}".format(self.cmd, self.arguments["playlist_id"], self.arguments["file_name"], self.arguments["file_type"])
        result = subprocess.run(full_cmd, stdout=subprocess.PIPE, shell=True)

        assert result.stdout == b"Successfully created!\n"

    def test_app_file_exists(self):
        filename = "{}.{}".format(self.arguments["file_name"], self.arguments["file_type"])

        assert os.path.exists(filename)

        os.remove(filename)
