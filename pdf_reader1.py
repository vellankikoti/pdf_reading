#Reading Portable Document Format(PDF) as String in Python
import PyPDF2

file = open('watchdog.pdf','rb')
file_read = PyPDF2.PdfFileReader(file)
file_data = ''
for page in range(file_read.numPages):
	page_data = file_read.getPage(page)
	file_data += page_data.extractText()
file.close()
print(file_data)
