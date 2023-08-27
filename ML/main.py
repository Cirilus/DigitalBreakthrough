import subprocess
import os
import base64
import tempfile

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import re
import pandas as pd
import markdown
import time
from dotenv import load_dotenv
from pdflatex import PDFLaTeX


def extract_markdown_between_delimiters(text):
    delimiter = '---'
    lines = text.strip().split('\n')

    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if line.strip() == delimiter:
            if start_index is None:
                start_index = i
            else:
                end_index = i
                break

    if start_index is not None and end_index is not None:
        markdown_lines = lines[start_index + 1: end_index]
        extracted_markdown = '\n'.join(markdown_lines)
        return extracted_markdown
    else:
        return None


load_dotenv()

API_KEY = os.getenv("API_KEY")
# df_competition = pd.read_csv('./startups.csv', sep=';')
openai = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=API_KEY,  # openai_key
)


def get_pdf(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    return base64_pdf


def filter_beamer(multi_line_string):
    latex_match = re.search(r'\\documentclass.*?\\end{document}', multi_line_string, re.DOTALL)
    if latex_match:
        latex_document = latex_match.group(0)
        print(latex_document)
    else:
        print("No LaTeX document found.")
        latex_document = ''
    return latex_document


def generate_pitch_deck(user_prompt, competition, team, market_analysis, traction):
    prompt = """Please create a pitch-deck style presentation on the following topic using reveal.js Markdown code. Topic: """ + str(
        user_prompt) + """. Please provide only Markdown code for the reveal.js slides:
    1. Project title and team""" + str(team) + """
    2. Problem and target audience
    3. Description and Value proposition of the startup
    4. Key competition summary and insights according to the given table:""" + competition + """
    5. Market Analysis estimates""" + market_analysis + """
    6. Traction and Roadmap""" + traction + """
     Provide only Markdown code."""
    messages = [
        SystemMessage(
            content="you are PitchDeckGPT: you create a pitch-deck style presentations from plain text into reveal.js Markdown format. You answer only with correct Markdown code according to reveal.js format for slides and bullet points."
        ),
        HumanMessage(
            content=prompt
        ),
    ]

    output = openai(messages).content
    return output


def classify_area(problem):
    prompt = """Based on the following startup value introduction, answer with the most fitting class of tech for the startup from the list. Please give only the class in answer.:
     Business Software',
     'IndustrialTech',
     'E-commerce',
     'Advertising & Marketing',
     'Hardware',
     'RetailTech',
     'ConstructionTech',
     'Web3',
     'EdTech',
     'Business Intelligence',
     'Cybersecurity',
     'HrTech',
     'Telecom & Communication',
     'Media & Entertainment',
     'FinTech',
     'MedTech',
     'Transport & Logistics',
     'Gaming',
     'FoodTech',
     'AI',
     'WorkTech',
     'Consumer Goods & Services',
     'Aero & SpaceTech',
     'Legal & RegTech',
     'Travel',
     'PropTech',
     'Energy',
     'GreenTech'
    Startup introduction: """ + str(problem)

    messages = [
        HumanMessage(
            content=prompt
        ),
    ]

    output = openai(messages).content
    return output


def get_competitors(df, class_name):
    return df[df['Рынок'] == class_name].dropna(axis='columns').to_string()


def latex_to_pdf_base64(latex_string):
    with tempfile.TemporaryDirectory() as temp_dir:
        tex_file_path = os.path.join(temp_dir, 'document.tex')
        pdf_file_path = os.path.join(temp_dir, 'document.pdf')

        with open(tex_file_path, 'w') as tex_file:
            tex_file.write(latex_string)

        print(subprocess.run(['pdflatex', '-output-directory', temp_dir, tex_file_path]))

        if not os.path.exists(pdf_file_path):
            raise FileNotFoundError(f"PDF file not generated at {pdf_file_path}")

        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')

        return pdf_base64


def get_pdf_pitch_desk(user_prompt, competition, team, market_analysis, traction):
    pitch_deck = generate_pitch_deck(user_prompt, competition, team, market_analysis, traction)
    pitch_deck = extract_markdown_between_delimiters(pitch_deck)
    print(pitch_deck)
    pdf = latex_to_pdf_base64(pitch_deck)
    return pdf
