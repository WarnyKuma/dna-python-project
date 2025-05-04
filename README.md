# 🧬 DNA Utility Web App

A simple Flask web app for manipulating DNA sequences — crop, translate, search patterns, detect mutations, reverse, and reverse-complement. Built with Python, Docker, and deployable on Google Cloud.

---

## Features

- Crop DNA sequences by index
- Translate DNA to protein using codon table
- Find patterns in sequences
- Detect mutations between reference and sample
- Reverse a sequence
- Compute reverse complement (e.g., for transcription)
- Web UI with Bootstrap dark mode
- Dockerized for easy deployment

---

## Accessing the App

DNA tool is available on https://dna-tool-254912217801.us-west2.run.app/

Alternatively, it can be launched locally:

1. Clone the repository
2. Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
3.Install required packages
```
pip install -r requirements.txt
```   
4.Run the program
```
export FLASK_APP=app
flask run
```
