A tool to translate WebVTT files from English to Chinese.

## How to use
It is easy to use this tool, firstly you should add the required module by
```
pip install -r requirements.txt
```
in the terminal.

Secondly, copy `.env.example` and rename it to `.env`, and add `APIKEY` and `BASEURL` in `.env`. Note that if you use the api from openai, the `BASEURL` is `https://api.openai.com/v1`, don't forget to add `\v1`.
Thirdly, change the value of the file name `subtitle_file` to the path your `.vtt` name locates, and run the following command:
```
python main.py
```
