import subprocess
import argparse

def concat_videos(video1, video2, output_video):
    command = f"ffmpeg -i {video1} -i {video2} -filter_complex \"[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[outv][outa]\" -map \"[outv]\" -map \"[outa]\" {output_video}"
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Concatenate two videos into one using FFmpeg')
    parser.add_argument('--video1', type=str, help='Path to the first video file')
    parser.add_argument('--video2', type=str, help='Path to the second video file')
    parser.add_argument('--output', type=str, default='output.mp4', help='Output path for the concatenated video')

    args = parser.parse_args()
    
    video1 = args.video1
    video2 = args.video2
    output_video = args.output

    concat_videos(video1, video2, output_video)
