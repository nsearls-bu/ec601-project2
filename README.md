# ec601-project2 - ChatGPT PII Scrubber

## Mission Statement

Our mission is to protect user privacy by developing a robust, automated PII scrubber capable of processing text documents and audio transcripts. Utilizing advanced natural language processing and customizable K-anonymity settings, our tool ensures compliance with privacy regulations (such as HIPAA) by progressively removing identifiable information to safeguard individuals in diverse contexts.

## Features

- **Redacts First-Level PII**: Names, SSNs, emails, phone numbers, addresses, and more.
- **K-Anonymity Slider**: Allows users to control the level of redaction, removing identifiable information based on group size (e.g., up to 10,000 people).
- **Customizable Models**: Users can choose between using OpenAI’s large language models or locally hosted models via an OpenAPI-compatible interface for enhanced data privacy.
- **Simple Command-Line Interface**: Provides an easy-to-use interface with configurable options for file upload, redaction levels, and model selection.
- **Input/Output System**: Files are selected from an input folder and redacted files are placed in a specified output folder.

## User Stories

- **Healthcare Professional**: Automatically redact PII from a transcript of a patient’s consultation to safely share for research purposes.
- **Legal Compliance Officer**: Remove direct and quasi-identifiers from text documents to ensure compliance with privacy regulations.
- **Data Analyst**: Anonymize customer feedback by removing city, company, or group identifiers to aggregate data without exposing personal information.
- **User**: Choose redaction level based on context using a K-anonymity slider for flexibility and control.

## Minimum Viable Product (MVP)

The MVP will focus on the core functionality of redacting first-level PII using customizable models. The key features include:

### Input/Output:

- Upload text documents or transcripts through a command-line interface.
- Redacted files are downloaded into a specified output folder.

### First-Level PII Redaction:

- Redact names (first and last), social security numbers, street addresses, city/state details, emails, and phone numbers.

### K-Anonymity Slider:

- Basic redaction levels configurable via flags in the command line (e.g., redact just names and SSNs or extend to broader quasi-identifiers).

### Model Selection:

- Choose between OpenAI’s models or a locally hosted model (via OpenAPI). This ensures data privacy by keeping data processing local if needed.
- Users can specify their API token and model selection as command-line options.

### User Interface:

- Command-line interface for specifying input folder, output folder, model selection, API tokens, and PII redaction flags.
- Output is a redacted document with masked PII (using symbols such as asterisks or similar).

## Usage

### Command-Line Tool

#### 1. Install dependencies:

To run the script locally, you need to have Python 3.9+ and the required dependencies.

```bash
pip install openai
```

#### 2. Prepare the folders:

Create input and output folders for processing the files.

```bash
mkdir input_files output_files
```

##### 3. Running the PII Scrubber:

```bash

python pii_scrubber.py --input-folder ./input_files --output-folder ./output_files --model openai --api-token your_openai_token --k-anonymity 2

    --input-folder: Path to the folder containing .txt files for redaction.
    --output-folder: Path to the folder where redacted files will be saved.
    --model: Choose between openai (for OpenAI models) or local (for local model).
    --api-token: Your OpenAI API token (required for OpenAI model).
    --k-anonymity: Level of K-anonymity to define how much PII to redact (higher value = more anonymity).
```

## Docker Support

You can also run the PII Scrubber inside a Docker container.

#### 1. Build the Docker image:

```bash

docker build -t pii-scrubber .
```

#### 2. Run the Docker container:

```bash
docker run --rm -v $(pwd)/input_files:/app/input_files -v $(pwd)/output_files:/app/output_files pii-scrubber --input-folder /app/input_files --output-folder /app/output_files --model openai --api-token your_openai_token --k-anonymity 2

    $(pwd)/input_files:/app/input_files: Maps the local input folder to the container’s input folder.
    $(pwd)/output_files:/app/
```

**output_files**: Maps the local output folder to the container’s output folder.
The rest of the flags (--input-folder, --output-folder, --model, --api-token, --k-anonymity) are the same as for the local run.
