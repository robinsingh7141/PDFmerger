import PyPDF2
from tkinter import filedialog
from tkinter import Tk

# Create a root Tkinter window, hide it since we only want the file dialog
root = Tk()
root.withdraw()

# Empty list to hold the PDF files
pdfiles = []

while True:
    print("Please select a PDF file to merge (or press cancel to finish selecting files):")
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]) # Show an "Open" dialog box and return the path to the selected file
    if filename:
        pdfiles.append(filename)
    else:
        break

merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    with open(filename, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)

merger.write('Merged.pdf')
print("Merged file created as 'Merged.pdf'")