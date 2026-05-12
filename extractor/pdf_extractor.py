import fitz

def pdf_to_text(file_path):

    # 1. Open the document
    doc = fitz.open(file_path)
    full_text = ""

    # 2. Iterate through every page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load the specific page

        # 3. Extract text from that page
        page_text = page.get_text()
        full_text += f"\n--- Page {page_num + 1} ---\n" 
        full_text += page_text

    # 4. Clean up
    doc.close()
    
    return full_text

# test
my_text = pdf_to_text("The-Iran-War-and-The-Global-Terrorism-Threat.pdf")
print(my_text)