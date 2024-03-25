from openai import OpenAI
from dotenv import load_dotenv
import os
from parallel_work_utils import TqdmMultiprocessing

load_dotenv()

client = OpenAI(
    api_key=os.getenv("APIKEY"),
    base_url=os.getenv('BASEURL')
    )

def translate_to_chinese(text):
    messages = [
        {
            "role": "system", 
            "content": "你是一个专业的英语翻译员，请你将下面的内容翻译成中文。请只返回翻译的中文内容，不要说多余的话。"
        },
        {
            "role": "user",
            "content": text
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
    )
    return response.choices[0].message.content.strip()

def is_time_stamp(line):
    return '-->' in line

def translate_subtitles(subtitle_file_path):
    # Determine the translated file's name
    translated_file_path = subtitle_file_path.rstrip('.vtt') + '-translate.vtt'

    # Read the original subtitle file
    with open(subtitle_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Translate and save the new subtitle file
    with open(translated_file_path, 'w', encoding='utf-8') as file:
        with TqdmMultiprocessing(_translation_core, processes=8) as q:
            translated_lines = q.tqdm(_translation_core, lines, total=len(lines))
        for line in translated_lines:
            file.write(line)
    
    # Return the path of the translated subtitle file
    return translated_file_path

def _translation_core(line):
    _translation_core.counter.value += 1
    if "WEBVTT" in line.strip() or is_time_stamp(line.strip()):
        return line
    elif line.strip():
        # Translate non-empty English content
        translated_text = translate_to_chinese(line.strip())
        return translated_text + '\n'
    else:
        # Preserve empty lines
        return '\n'

if __name__ == "__main__":
    # Use the function with an example subtitle file
    subtitle_file = 'ISO Standard Explained _ What is ISO _ Benefits of getting ISO certified _ How to get ISO certified_.vtt'
    translated_file = translate_subtitles(subtitle_file)
    print(f"The translated subtitle file has been saved as: {translated_file}")
