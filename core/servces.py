from datetime import datetime

from db.repository import DocumentRepository
from datetime import datetime
import os
from core.FileManager import FileManager
from core.thumnail import ThumbnailGenerator
from core.reader import PDFReader
from core.models import Document

PDF_STORAGE = os.path.join("storage", "pdfs")

class DocumentService:
    def __init__(self):
        self.repo = DocumentRepository()
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()
        self.reader = PDFReader()

    def upload_document(self, uploaded_file, tags, description,lecture_date=None):
        #doc = []
        # 1. save file
        # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        # filename = f"{timestamp}_{uploaded_file.name}"
        # #file_path = os.path.join("storage", "pdfs")
        # file_path = os.path.join(PDF_STORAGE, filename)
        # # Write the binary file -> wb
        # with open(file_path, "wb") as f:
        #     f.write(uploaded_file.read())

        file_path = self.file_manager.save_file(uploaded_file)

        #2. Generate thumbnail

        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)

        #3. Get total pages

        total_pages = self.thumbnail_generator.get_total_pages(file_path)

        #4. Convert to the images

        self.reader.convert_pdf_to_images(file_path)

        upload_date = datetime.now().strftime("%Y-%m-%d")
       
        #6. Save to db

        # doc.append(uploaded_file.name)
        # doc.append(file_path)
        # doc.append(thumbnail_path)
        # doc.append(tags)
        # doc.append(description)
        # doc.append(upload_date)
        # doc.append(lecture_date)
        # doc.append(total_pages)
        doc = Document(
            id=None,
            name = uploaded_file.name,
            path= file_path,
            thumbnail_path=thumbnail_path,
            tags = tags,
            description=description,
            uploaded_date=upload_date,
            lecturer_date=lecture_date,
            total_pages=total_pages
        )

       
        self.repo.add_document(doc)

    def search_documents(self, tag=None, date=None):
        return self.repo.search_documents(tag, date)
    
    def get_all_documents(self):
        return self.repo.get_all_documents()