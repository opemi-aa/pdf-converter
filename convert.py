from pdf2docx import Converter
pdf_file = "use.pdf"
docx_file = "cloding.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()