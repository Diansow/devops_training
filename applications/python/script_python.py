# PDF to Images 
# pip install PyMuPDF 
import fitz 
def  pdf_to_images ( pdf_file ): 
    doc = fitz. ouvrir (pdf_file) 
    pour p dans doc : 
        pix = p.get_pixmap() 
        output = f"page {p.number} .png"
         pix.writePNG(output) 
pdf_to_images( "test.pdf" )