FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN mkdir -p /app/input_files /app/output_files
ENTRYPOINT ["python", "pii_scrubber.py"]
