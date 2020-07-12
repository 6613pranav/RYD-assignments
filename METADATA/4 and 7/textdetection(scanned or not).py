import fitz

def check_pdf_scanned_plain(file_name):
    # This algorithm calculates the percentage of document that is covered by (searchable) text

    page_num = 0
    text_perc = 0.0

    doc = fitz.open(file_name)

    for page in doc:
        page_num = page_num + 1

        page_area = abs(page.rect)
        text_area = 0.0
        for b in page.getTextBlocks():
            r = fitz.Rect(b[:4]) # rectangle where block text appears
            text_area = text_area + abs(r)
        text_perc = text_perc + (text_area / page_area)

    text_perc = text_perc / page_num

    # If the percentage of text is very low, the document is most likely a scanned PDF
    if text_perc < 0.09:
        print("fully scanned PDF, need OCR library to extract text")
    else:
        print("it is a text PDF, we  need pypdf library to extract text")
