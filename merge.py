import subprocess
import argparse

def merge_video_subtitle(video_file, subtitle_file):
    output_video_file = video_file.rstrip('.mp4') + '-with-subtitles.mp4'
    
    # Command for ffpmeg to embed subtitles into the video
    command = [
        'ffmpeg',
        '-i', video_file,     # Input video file
        '-vf', f'subtitles={subtitle_file}',  # Filter to overlay subtitles
        '-codec:a', 'copy',  # Copy audio without re-encoding
        output_video_file    # Output video file
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f'Successfully merged the video with subtitles as {output_video_file}')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred while merging the video and subtitles: {e}')


def main():
    # 创建argparse解析器
    parser = argparse.ArgumentParser(description='Merge video and subtitle files.')
    # 添加--mp4参数
    parser.add_argument('--mp4', required=True, help='The input video file path.')
    # 添加--subtitle参数
    parser.add_argument('--subtitle', required=True, help='The input subtitle file path.')
    
    # 解析命令行参数
    args = parser.parse_args()

    # 执行合并操作
    merge_video_subtitle(args.mp4, args.subtitle)


if __name__ == '__main__':
    main()
    
