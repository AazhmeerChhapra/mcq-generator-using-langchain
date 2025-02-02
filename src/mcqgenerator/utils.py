import os 
import json
import PyPDF2
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error Reading the PDF file")
    elif file.name.endswith(".txt"):
        return file.read().decode('utf-8')
    else:
        raise Exception("Unsupported file format")

def get_table(str):
    try:
        quiz = json.loads(str)
        quiz_table_data = []
        for key, values in quiz.items():
            mcq = values['mcq']
            options = " || ".join(
                [
                f"{option} -> {option_value}" for option, option_value in values['options'].items()
                ]
            )
            correct_value = values['correct']
            quiz_table_data.append({"MCQ":mcq, "Options":options, "Correct":correct_value})
        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
