"""
Make a short, small GIF from a video clip for embedding in READMEs.
GitHub renders GIFs inline; it does not render video files inline.

Usage:
    python scripts/make_gif.py --input data/videos/output/resnet18/challenge_video_annotated.mp4 \
                                --output docs/images/resnet_sample.gif \
                                --start 0 --duration 4 --fps 10 --width 480
"""

import argparse

from moviepy.editor import VideoFileClip


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--start", type=float, default=0, help="Start time in seconds")
    parser.add_argument("--duration", type=float, default=4, help="Clip length in seconds")
    parser.add_argument("--fps", type=int, default=10)
    parser.add_argument("--width", type=int, default=480, help="Resize width (keeps aspect ratio)")
    args = parser.parse_args()

    clip = VideoFileClip(args.input).subclip(args.start, args.start + args.duration)
    clip = clip.resize(width=args.width)
    clip.write_gif(args.output, fps=args.fps)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
