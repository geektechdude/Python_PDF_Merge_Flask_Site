# pulls down the current Python image
FROM python

# changes working directory to app
WORKDIR /app

# copies contents of the geektechstuff_pdf_merge_flask folder to the working directory
COPY . /app

# Runs PIP and installs the modules mentioned in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV NAME world

# Opens pdfmerge_flask.py
CMD ["python", "pdfmerge_flask.py"]

