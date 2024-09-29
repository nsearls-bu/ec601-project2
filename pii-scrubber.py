'''Generated using LLM tools'''
import argparse
import os
import openai

def openai_redaction(api_token, text, redaction_level):
    '''Uses OpenAI API to redact PII based on the redaction level.'''
    openai.api_key = api_token
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Redact PII at level {redaction_level} from the following text:\n\n{text}",
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def process_file(file_path, model, api_token, k_anonymity):
    '''Processes the file, applying multiple passes of redaction based on K-anonymity.'''
    with open(file_path, 'r') as file:
        text = file.read()

    for level in range(1, k_anonymity + 1):
        if model == 'openai':
            text = openai_redaction(api_token, text, level)

    return text

def main():
    '''Parses arguments and processes each file for PII redaction.'''
    parser = argparse.ArgumentParser(description="PII Scrubber Command-Line Tool")
    parser.add_argument('--input-folder', type=str, required=True, help="Folder containing files to redact.")
    parser.add_argument('--output-folder', type=str, required=True, help="Folder to save redacted files.")
    parser.add_argument('--model', type=str, choices=['openai', 'local'], required=True, help="Choose between 'openai' or 'local' models.")
    parser.add_argument('--api-token', type=str, required=False, help="Your OpenAI API token (required for OpenAI model).")
    parser.add_argument('--k-anonymity', type=int, default=1, help="Level of K-anonymity redaction (default: 1).")

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    model = args.model
    api_token = args.api_token
    k_anonymity = args.k_anonymity

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            print(f"Processing file: {file_path}")

            try:
                redacted_text = process_file(file_path, model, api_token, k_anonymity)
                output_path = os.path.join(output_folder, filename)

                with open(output_path, 'w') as output_file:
                    output_file.write(redacted_text)

                print(f"Redacted file saved: {output_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")

if __name__ == "__main__":
    main()
