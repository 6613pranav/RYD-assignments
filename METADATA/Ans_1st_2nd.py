from PyPDF2 import PdfFileReader
def get_info(book):
    with open(book, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        
    title = info.title
    print("Title : ",title)
    author = info.author
    print("Author : ",author)
    
    
if __name__ == '__main__':
    book = 'book_name.pdf'
    get_info(book)
    
