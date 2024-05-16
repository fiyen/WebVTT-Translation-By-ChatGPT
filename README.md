A tool to translate WebVTT files from English to Chinese.

## How to use
It is easy to use this tool, firstly you should add the required module by
```
pip install -r requirements.txt
```
in the terminal.

Secondly, copy `.env.example` and rename it to `.env`, and add `APIKEY` and `BASEURL` in `.env`. Note that if you use the api from openai, the `BASEURL` is `https://api.openai.com/v1`, don't forget to add `/v1`.

Thirdly, change the value of the file name `subtitle` to the path your `.vtt` file locates, and run the following command:
```
python main.py --subtitle `XXX.vtt`
```
where `XXX.vtt` is the path of your subtitle file.

Then you will get a new `.vtt` file with the name same as the source `.vtt` file but contains an extented content of `-translate`. For example. `XXX-translate.vtt`.

## To merge the subtitle to .mp4 file
After translating subtitle, you can directly merge this subtitle to .mp4 file where being subtitle extracted from. You should first install `ffmpeg`. To install `ffmpeg` you should follow these steps:

### Windows

1. **Downloadmpeg**:
   - Visit the [download page](https://ffmpeg.org/download.html) on the official FFmpeg website.
   - Click on the "Windows builds from gyan.dev" link or other available Windows builds.
   - Download the latest "release" build archive.

2. **Extract FFmpeg**:
   - After downloading, extract the files to your desired location, e.g., `C:\ffmpeg`.

3. **Add FFmpeg to the system's path**:
   - Open Control Panel -> System and Security -> System -> Advanced system settings -> Environment Variables.
   - Under System Variables, find and select "Path," then click "Edit."
   - Click "New" and add the path to the `bin` directory of FFmpeg, e.g., `C:\ffmpeg\bin`.
   - Click "OK" to save the changes.

4. **Verify the installation**:
   - Open Command Prompt (cmd) and enter `ffmpeg -version`. If the version information is displayed, the installation was successful.

### macOS

1. **Install using Homebrew**:
   - First, ensure that you have Homebrew installed. If not, you can install Homebrew by running the following command in Terminal:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Use the following command to install FFmpeg via Homebrew:
     ```bash
     brew install ffmpeg
     ```

2. **Verify the installation**:
   - Open Terminal and enter `ffmpeg -version`. If the version information is displayed, the installation was successful.

### Linux

1. **Install using package manager**:
   - For Debian-based systems (e.g., Ubuntu), you can use the following command to install:
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
   - For RPM-based systems (e.g., Fedora or CentOS), you can use the following command to install:
     ```bash
     sudo dnf install ffmpeg
     ```
     For older versions of CentOS, you may need to enable the EPEL repository first:
     ```bash
     sudo yum install epel-release
     sudo yum install ffmpeg
     ```

2. **Verify the installation**:
   - Open Terminal and enter `ffmpeg -version`. If the version information is displayed, the installation was successful.

After `ffmpeg` is installed, run the following commands to merge .mp4 and its translated subtitle:

```
python merge.py --video {XXX.mp4} --subtitle {XXX.vtt}
```

replace {XXX.mpt} with the .mp4 file you need to operate, and replace {XXX.vtt} with the subtitle need to be merged. 

## to split mp4 file to pieces.
For videos longer than 20 mins, there may occurs error for some stt tools that subtitles are keeping outputing one single sentence. To solve this problem,
cut.py can be used to split long video to pieces of shorter videos. Use:

```
python cut.py --video {XXX.mp4} --n {number_pieces:int}
```
where n is the number of pieces.

Then call merge.py to merge subtitles to pieces of videos, and then call concat.py to get a full video:

```
python concat.py --video1 {XXX1.mp4} --video2 {XXX2.mp4} --output {XXX.mp4}
```

## to extract the frames of mp4 file 

```
python extract_frames.py --file {XXX.mp4} --save_file {XXX.rar}
```
