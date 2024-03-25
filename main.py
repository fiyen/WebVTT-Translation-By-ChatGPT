# 需要先安装googletrans库，使用pip install googletrans==4.0.0-rc1
from googletrans import Translator, LANGUAGES

# 定义一个函数来翻译字幕内容
def translate_subtitle(file_path):
    # 初始化翻译器
    translator = Translator()
    translated_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        # 判断当前行是否为时间轴或WEBVTT标识，这些不需要翻译
        if "-->" in line or "WEBVTT" in line:
            translated_lines.append(line)
        elif line.strip() == '':
            translated_lines.append(line)
        else:
            # 使用googletrans进行翻译
            translated = translator.translate(line, src='en', dest='zh-cn')
            translated_lines.append(translated.text + '\n')
    
    return translated_lines

# 调用上面的函数，并保存输出到新的字幕文件
def save_translated_subtitle(input_path, output_path):
    translated_lines = translate_subtitle(input_path)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)

# 使用示例
input_subtitle_path = 'your_subtitle_file_path.vtt'  # 将'your_subtitle_file_path.vtt'替换为你的字幕文件路径
output_subtitle_path = 'translated_subtitle.vtt'  # 输出文件路径
save_translated_subtitle(input_subtitle_path, output_subtitle_path)

