from pathlib import Path
from youtube_dl.ydl import Ydl


def main():
    url: str = input("Enter url: ")
    out_path: str = input("Enter output path (default = ~/Downloads): ")
    fname: str = input("Enter filename (default = video): ")

    ydl = Ydl()  # if want mp4, Ydl(video_ext="mp4", audio_ext="m4a", out_ext="mp4")

    r = ydl.download(
        url,
        out_path=Path(out_path) if out_path else Path.home() / "Downloads",
        fname=fname or "video",
    )

    print("--------------------")
    print("       Success      " if r else "       Failed       ")
    print("--------------------")


if __name__ == "__main__":
    main()
