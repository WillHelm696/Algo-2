import PyPDF2

# Open the PDF file in binary mode
pdf_file = open('input.pdf', 'rb')
# Create a PDF file reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Initialize an empty string to store the text
text = ""

# Loop through each page in the PDF
for page_num in range(pdf_reader.numPages):
    # Get the page object
    page_obj = pdf_reader.getPage(page_num)

    # Extract the text from the page
    text += page_obj.extractText()

# Close the PDF file
pdf_file.close()

# Open a text file to write the extracted text
txt_file = open('output.txt', 'w')

# Write the extracted text to the text file
txt_file.write(text)

# Close the text file
txt_file.close()
