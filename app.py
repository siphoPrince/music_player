import tkinter as tk
from pygame import mixer

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Python Music Player")

        mixer.init()  # Initialize the mixer module

        self.controls_frame = tk.Frame(master)
        self.controls_frame.pack()

        self.play_button = tk.Button(self.controls_frame, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.controls_frame, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.controls_frame, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.previous_button = tk.Button(self.controls_frame, text="Previous", command=self.previous)
        self.previous_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.controls_frame, text="Next", command=self.next)
        self.next_button.pack(side=tk.LEFT)

        self.volume_label = tk.Label(master, text="Volume:")
        self.volume_label.pack()

        self.volume_scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.pack()

        # Set initial volume to 50%
        self.set_volume(50)

        # List of songs in the playlist
        self.playlist = ["sound1.mp3", "sound2.mp3", "sound3.mp3"]  # Add more songs as needed
        self.current_index = 0

        # Load and play the first song in the playlist
        self.load_and_play(self.playlist[self.current_index])

    def play(self):
        mixer.music.unpause()  # Unpause the music

    def pause(self):
        mixer.music.pause()  # Pause the music

    def stop(self):
        mixer.music.stop()  # Stop the music

    def previous(self):
        # Move to the previous song in the playlist
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_and_play(self.playlist[self.current_index])

    def next(self):
        # Move to the next song in the playlist
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_and_play(self.playlist[self.current_index])

    def load_and_play(self, file_path):
        mixer.music.load(file_path)  # Load the music from the file path
        mixer.music.play()  # Start playing the music
        self.volume_scale.set(mixer.music.get_volume() * 100)  # Set volume scale to current volume level

    def set_volume(self, volume):
        mixer.music.set_volume(int(volume) / 100)  # Set the volume as a value between 0 and 1

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
