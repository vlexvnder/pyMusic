class Note:

    def __init__(self, moment, noteName, length ):
        self.moment = moment
        self.noteName = noteName
        self.length = length

        self.notes = {"C4": AudioSegment.from_mp3("../Audio/piano-mp3/C4.mp3")}  # Dict of names : AudioSegments

    def __str__(self):
        return str(self.noteName) + " at "+str(self.moment) + " for " + str(self.length)

   def getNoteAudio(self, tempo):
        return self.notes[self.noteName][:((60*1000)/tempo)*self.length] #cuts the note to 1 beat (1/4 note) times the length of the note
