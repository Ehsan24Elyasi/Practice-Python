import argparse
from pytubefix import YouTube
from pathlib import Path
from typing import Optional
from tqdm import tqdm


class YouTubeDownloader():
    def __init__(self, url: str, output_path: Optional[str] = None, quality: Optional[str] = None):
        self.url = url
        self.outpute_path = output_path or Path.cwd()
        self.quality = quality or "highest"
        self.yt = YouTube(
            self.url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete
            )

    def download(self):
        if self.quality == "highest":
            stream = self.yt.streams.filter(
            progressive=True,
            file_extension="mp4"
            ).get_highest_resolution

        else:
            stream = self.yt.streams.filter(
                progressive=True,
                file_extension="mp4",
                res=self.quality
                ).filter()

        self.pbar = tqdm(
                total=stream.filesize,
                unit="B",
                unit_scale=True,
                desc=self.yt.title,
            )
        
        stream.download(self.output_path)
    
    def on_progress(self, stream, chunk, bytes_remaining):
       current = stream.filesize - bytes_remaining
       self.pbar.update(current - self.pbar.n) 

    def  on_complete(self, stream, file_path ):
       self.pbar.close()
       print(f"\nDownloaded '{self.yt.title}' successfully to: {file_path}")


if __name__ == "__main__":
        parser= argparse.ArgumentParser(
            description=" YouTube Downloder "
        )
        parser.add_argument("url", help="YouTube url")
        parser.add_argument("-q", "--quality", help="YouTube quality", default="highest")
        parser.add_argument("-p", "--path", help="YouTube path", default=None)

        args = parser.parse_args()

        YouTubeDownloader(
            url = args.url,
            quality = args.quality,
            output_path = args.path
        ).download()
        