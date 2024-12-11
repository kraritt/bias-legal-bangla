import re 
import PyPDF2
import os 

import re

def clean_text_bangla(text):

    text = re.sub(r'(\।{৩})', '!ELLIPSIS! ', text)
    
    text = re.sub(r'(\।)(?=[\u0980-\u09FF]{2,})', '!PERIOD! ', text)
    
    text = re.sub(r'(\।)(?=[\u0980-\u09FF][\u0980-\u09FF])', '!PERIOD! ', text)
    
    text = re.sub(r'(\। )(?=[\u0980-\u09FF])', '!PERIOD! ', text)
    text = text.replace('!ELLIPSIS!', '।।।')
    
    text = re.sub(r'[^\u0980-\u09FF0-9 \?!,;\-।।।]+', '', text)
    text = text.replace('!PERIOD!', '।')
    
    text = re.sub(r'\n', '', text)
    
    text = re.sub(r'প্রক্রিয়া[0-9]{১১}', '[CODE]', text)
    text = text.replace('[CODE]', '')
    
    text = re.sub(r'(?<=[0-9])(?=[\u0980-\u09FF])', ' ', text)
    
    text = re.sub(r'(\d+)', '[NUMBER]', text)
    
    text = text.replace('[NUMBER]', '')
    
    text = re.sub(r'নির্বাহী বিভাগ, উচ্চ আদালত, রাজশাহী', '', text, flags=re.IGNORECASE)
    text = re.sub(r'উচ্চ আদালত, নির্বাহী বিভাগ, রাজশাহী', '', text, flags=re.IGNORECASE)
    
    text = re.sub(r'\b(পৃ|পৃস)\b', '', text)
    
    text = re.sub(r' +', ' ', text)
    
    text = re.sub(r'(ইলেকট্রনিক স্বাক্ষর|ইলেকট্রনিক স্বাক্ষরিত)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'(এই নথি আসল কপির অনুলিপি, ডিজিটালি স্বাক্ষরিত।*?প্রক্রিয়া নম্বর)', '', text)
    text = re.sub(r'(মূল কপি যাচাই করতে.*?প্রক্রিয়া নম্বর)', '', text)
    
    return text.strip()


def text_extractor(path):

	directory = os.fsencode(path)

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		text_full = '' 
		if filename.endswith(".pdf"):		
			pdf_file = open(filename, "rb")
			pdf_reader = PyPDF2.PdfFileReader(pdf_file, strict=False)

			for page in pdf_reader.pages:
				text_page = page.extractText() 
				text_full = text_full + text_page + ' '

			text = clean_text_bangla(text_full)
			text_filename = filename[:len(filename)-4] + ".txt"
			textfile = open(path + text_filename, "a+")
			textfile.write(text)
			textfile.close()

path = os.path.abspath(os.getcwd()) + "/"
text_extractor(path)