#from pydub import AudioSegment
from Note import Note

class Song:


    def __init__(self):

        self.notes = []

        self.tempo = 120  # bpm
        self.milli_between_beats = (60 / self.tempo) * 1000
        self.cur_beat = 1

    def addNote(self, note):
        self.notes.append(note)

    def setTempo(self,bpm):
        self.tempo = bpm
        self.milli_between_beats = (60 / self.tempo) * 1000



    def orderSong(self):
        sorted_song = self.notes
        sorted_song.sort(key=lambda x: x.moment)
        return sorted_song

    # for each song, call playKey
    # return mp3

    def playKey(self, note, beat):
        pass #TODO





s = Song()
first = Note(1,"D",1)
sec = Note(2,"D",1)

s.addNote(sec)
s.addNote(first)
print(s.notes)
for a in s.orderSong():
    print(a)
print(s.orderSong())