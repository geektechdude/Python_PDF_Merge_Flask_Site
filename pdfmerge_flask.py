# geektechstuff PDF Merge as a Flask site

from flask import Flask, render_template, request
from werkzeug import secure_filename
import PyPDF2
import datetime
import random

now = datetime.datetime.now()

app = Flask(__name__, static_folder='', static_url_path='')

@app.route('/pdf')
def upload_file():
   return render_template('pdf.html')
	
@app.route('/pdfmerge', methods = ['GET', 'POST'])
def upload_files():
   pdfWriter = PyPDF2.PdfFileWriter()
   if request.method == 'POST':
      files_to_upload = request.files.getlist("file")
      print(files_to_upload)
      for item in files_to_upload:
         f = item
         f.save(secure_filename(f.filename))
         pdfFileObj = open(f.filename, 'rb')
         pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
         for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
   date = str(now.strftime("%Y-%m-%d"))
   rand = str(random.randint(1,10000))
   seq = date+rand
   file_name_pdf = 'geektechstuff'+seq+'.pdf'
   pdfOutput=open(file_name_pdf,'wb')
   pdfWriter.write(pdfOutput)
   pdfOutput.close()
   return app.send_static_file(file_name_pdf)

if __name__ == '__main__':
   app.run(debug = True)