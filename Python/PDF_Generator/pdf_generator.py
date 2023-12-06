import os
import img2pdf
from pdf2image import convert_from_path

# *.jpg to output_filename.pdf convertor
with open("output_filename.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))

# file.pdf to output_images_folder_name/page_no.jpg convertor
pages = convert_from_path('input_filename.pdf', 500)
for page_no, page in enumerate(pages):
    pages[page_no].save(
        f'output_images_folder_name/output_page_{page_no + 1}.jpg', 'JPEG'
    )