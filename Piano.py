from pydub import AudioSegment, playback
import Parser as p
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
        m = sorted_song[0].moment
        temp=[]
        final = []
        for n in sorted_song:
            if(n.moment != m):
                
                temp.sort(key=lambda x: x.length, reverse=True)
                final.append(temp)
                temp=[]
                temp.append(n)
                m=n.moment
            else:
                temp.append(n)
           
        temp.sort(key=lambda x: x.length, reverse=True)
        final.append(temp)
        
        return final
    
    def compileSong(self):

        song = AudioSegment.silent(duration=1)
        orderedSong = self.orderSong()
        nextSound = AudioSegment.silent(duration=orderedSong[0][0].getLength_milli(self.tempo))
        cur_moment=1
        for x in orderedSong:
            try:
                nextSound = AudioSegment.silent(duration=x[0].getLength_milli(self.tempo))
            except:
                nextSound = AudioSegment.silent(duration=self.milli_between_beats)
            for n in x:
                nextSound=nextSound.overlay(n.getNoteAudio(self.tempo))
                
            song = song + nextSound
            
            
            cur_moment+=1
        
        return song
   

    





