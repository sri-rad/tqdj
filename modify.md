To add or change the music in tqdj, there are a few steps you have to take.

#### Requirements
- The files must be in .wav format.

#### Steps
1. First, you need to figure out what song you would like to add, and then find a .wav formatted file that has that song on it.
2. Next, put that file into the folder /tqdj/music.
3. Once the file is in the /music folder, go back up to the /tqdj folder and open up player.py.
4. From there, copy this code into the self.audio_files list under the definition \_\_init\_\_
`python
>>> {
            'path': os.path.join(dir_path, 'cruise.wav'),
            'name': 'David Renda - Cruisin Along'
        }
`
Don't forget to add a comma after the previous song! (Cruisin' Along)
5. Once this is done, save and quit, and your custom songs should be added!