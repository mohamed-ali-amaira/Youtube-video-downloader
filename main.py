from pytube import YouTube
import tkinter as tk
from tkinter import messagebox as msgbox


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(" Youtube downloader ++ ")
        self.video_url = tk.StringVar()

        self.url_label = tk.Label(self, text="Enter the video URL that you want to download")
        self.url_label.pack(fill=tk.BOTH, padx=10, pady=10)

        self.url_input = tk.Entry(self, textvar=self.video_url)
        self.url_input.pack(fill=tk.BOTH, padx=20, pady=20)

        self.submit_btn = tk.Button(self, text="Download", command=self.submit)
        self.submit_btn.pack(side=tk.RIGHT, padx=5, pady=5)

    def submit(self):
        url = self.video_url.get()
        video = YouTube(url=url).streams.first().download()
        msgbox.showinfo("Operation finished", "Check out your download it is done!!")


if __name__ == '__main__':
    Window().mainloop()