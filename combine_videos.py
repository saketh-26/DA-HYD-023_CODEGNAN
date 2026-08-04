
import sys
from moviepy import VideoFileClip, concatenate_videoclips
 
 
def combine_videos(video1_path: str, video2_path: str, output_path: str):
    clip1 = VideoFileClip(video1_path)
    clip2 = VideoFileClip(video2_path)
 
    final_clip = concatenate_videoclips([clip1, clip2], method="compose")
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
 
    clip1.close()
    clip2.close()
    final_clip.close()
 
    print(f"Done. Combined video saved to: {output_path}")
 
 
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python combine_videos_moviepy.py video1.mp4 video2.mp4 output.mp4")
        sys.exit(1)
 
    video1, video2, output = sys.argv[1], sys.argv[2], sys.argv[3]
    combine_videos(video1, video2, output)
