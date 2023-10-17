import PyPDF2

# import sys
#
# inputs = sys.argv[1:]
#
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
#
# pdf_combiner(inputs)
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     # print(len(reader.pages))
#     page = reader.pages[0].rotate(180)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

path_original_pdf = 'super.pdf'
path_watermark_pdf = 'wtr.pdf'
path_watermarked_pdf = 'waterpdf.pdf'

with open(path_original_pdf, 'rb') as original_pdf, open(path_watermark_pdf, 'rb') as watermark_pdf:
    original_pdf_reader = PyPDF2.PdfReader(original_pdf)
    watermark_pdf_reader = PyPDF2.PdfReader(watermark_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(original_pdf_reader.pages)):
        page = original_pdf_reader.pages[page_num]
        page.merge_page(watermark_pdf_reader.pages[0])

        pdf_writer.add_page(page)

    with open(path_watermarked_pdf, 'wb') as watermarked_pdf:
        pdf_writer.write(watermarked_pdf)
print('Watermark add with success')
