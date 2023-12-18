from pathlib import Path
import yt_dlp


class Ydl:
    __opts: dict = {
        "format": None,
        "outtmpl": None,
        "merge_output_format": None,
        "postprocessors": None,
    }

    def __init__(
        self, video_ext: str = "webm", audio_ext: str = "webm", out_ext: str = "webm"
    ) -> None:
        self.__opts[
            "format"
        ] = f"bestvideo[ext={video_ext}]+bestaudio[ext={audio_ext}]/best[ext={out_ext}]"
        self.__opts["merge_output_format"] = out_ext
        self.__opts["postprocessors"] = [
            {"key": "FFmpegVideoConvertor", "preferedformat": f"{out_ext}"}
        ]

    def download(
        self,
        url: str,
        out_path: Path = Path.home() / "Downloads",
        fname: str = "video",
    ) -> bool:
        self.__opts["outtmpl"] = str(out_path / f"{fname}.%(ext)s")

        if not url:
            print("url cannot be empty")
            return False

        with yt_dlp.YoutubeDL(self.__opts) as ydl:
            ydl.download([url])

        return True
