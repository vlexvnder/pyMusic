class Song:
    notes = {"C":"c.mp3"}
    song = [] 

    tempo = 120 #bpm
    milli_between_beats = (60/tempo)*1000
    cur_beat = 1
    def __init__(self):
        pass
    
    def setTempo(bpm):
        self.tempo=bpm
        self.milli_between_beats = (60/self.tempo)*1000
    
    def addNote(self, key)
        song.add(key)

    def compileSong(self)
        for s in self.song:
            #for each song, call playKey
        #return mp3
    

    def playKey(self, note, beat=self.cur_beat, style="normal"):
        #beat is the point of the song to insert note at. By default, it will insert at the maximum beat
        
        time_to_place = (beat/tempo)*60*1000

        offset = self.milli_between_beats #or whatever the length between beats is

        clipAt = 1000 #when to stop the note

        sound_file = self.notes[note]

        if(style="staccato"):
            pass #change note length/offset to be staccato
        
        
