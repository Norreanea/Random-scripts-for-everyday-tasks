#Script that tracks which page numbers contain color content and prints them at the end
import fitz  # PyMuPDF
import numpy as np

# Open the PDF
doc = fitz.open("test.pdf")
total_pages = doc.page_count

# List to store the page numbers that have color content
color_page_numbers = []

for i in range(total_pages):
    page = doc.load_page(i)
    # Render the page as a pixmap in RGB colorspace.
    pix = page.get_pixmap(colorspace=fitz.csRGB)
    # Convert pixmap to a numpy array.
    data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
    
    # Check if the page is purely grayscale.
    # A page is grayscale if all pixels have equal R, G, and B values.
    if not np.allclose(data[:, :, 0], data[:, :, 1]) or not np.allclose(data[:, :, 0], data[:, :, 2]):
        # If this condition is True, the page has some color
        color_page_numbers.append(i + 1)  # use 1-based indexing

print(f"Total pages in PDF: {total_pages}")
print(f"Number of pages with color content: {len(color_page_numbers)}")
print("Color pages:", color_page_numbers)
