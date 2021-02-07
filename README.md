# pyMusic
🔨 This project is currently undergoing cleanup! 📏

Requires the pydub audio library.

pyMusic is a library to compose piano music with python. Using it is simple. First import Song and Note and create a song:

```
from Piano import Song 
from Note import Note
s = Song()
```

Set the tempo in bpm:
```
s.setTempo(60)
```

Then, make your song! 
```
s.addNote(Note(1,"G4",1))
s.addNote(Note(2,"G4",1))
s.addNote(Note(3, "D4",1))
```
A Note requires:
-A starting beat
-A note
-A length (in beats)

So, Note(1, "G4", 1) would play the note G4 at beat one for one beat

To finish and export the song,
```
finishedSong = s.compileSong()
```
And use your prefered method to play or export the song
```
finishedSong.export("song.mp3", format="mp3")
```
