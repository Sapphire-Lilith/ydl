import os
import yt_dlp


# download video and audio separately as webm, then merge them into webm
def download(url: str, output_path: str = "~/Downloads", filename: str = "video") -> str:
    ydl_opts = {
        "format": "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]",
        "outtmpl": os.path.join(output_path, f"{filename}.%(ext)s"),
        "merge_output_format": "webm",
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "webm"}],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "Success!"
