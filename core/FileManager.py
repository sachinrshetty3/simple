from datetime import datetime
import os

PDF_STORAGE = os.path.join("storage", "pdfs")

class FileManager:

    def save_file(self, uploaded_file):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{uploaded_file.name}"
        #file_path = os.path.join("storage", "pdfs")
        file_path = os.path.join(PDF_STORAGE, filename)
        # Write the binary file -> wb
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        return file_path