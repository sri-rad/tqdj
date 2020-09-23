import time
import simpleaudio as sa
import asyncio
import threading
import random

import os

from simpleaudio._simpleaudio import SimpleaudioError

dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'music')


class Player():
    def __init__(self):
        self.audio_files = [{
            'path': os.path.join(dir_path, 'paradise.wav'),
            'name': 'Purrple Cat - lost paradise'
        },
            {
            'path': os.path.join(dir_path, 'jazzy.wav'),
            'name': 'Homie Cat - riverbed'
        },
            {
            'path': os.path.join(dir_path, 'mondays.wav'),
            'name': 'MusicByAden - Mondays'
        },
            {
            'path': os.path.join(dir_path, 'time.wav'),
            'name': 'KaizanBlue - Time'
        },
            {
            'path': os.path.join(dir_path, 'cruise.wav'),
            'name': 'David Renda - Cruisin Along'
        }
        ]
        random.shuffle(self.audio_files)

        self.play_obj = None
        self._stop = False
        self.playing_now = self.audio_files[0]['name']

    def _play(self):
        while True:
            for audio_file in self.audio_files:
                wave_obj = sa.WaveObject.from_wave_file(audio_file['path'])
                self.playing_now = audio_file['name']
                if not self._stop:
                    try:
                        self.play_obj = wave_obj.play()
                        self.play_obj.wait_done()
                    except SimpleaudioError:
                        print('cannot play audio')
                        self._stop = True

                if self._stop:
                    break

            if self._stop:
                break

    def play(self):
        self.thread = threading.Thread(target=self._play)
        self.thread.start()

    def stop(self):
        self._stop = True
        try:
            self.play_obj.stop()
        except AttributeError:
            pass
