from Piano import Song 

s = Song()
s.setTempo(60)

#Put song here
s.addNote(Note(1,"G4",1))
s.addNote(Note(2,"G4",1))
s.addNote(Note(3, "D4",1))
s.addNote(Note(4, "D4",1))
s.addNote(Note(5, "E4",1))
s.addNote(Note(6, "E4",1))
s.addNote(Note(7, "D4",1))
s.addNote(Note(8, "C4",1))
s.addNote(Note(9, "C4",1))
s.addNote(Note(10, "B4",1))
s.addNote(Note(11, "B4",1))
s.addNote(Note(12, "A4",1))
s.addNote(Note(13, "A4",1))
s.addNote(Note(14, "G4",1))
s.addNote(Note(15, "D4",1))
s.addNote(Note(16, "S", 3))
s.addNote(Note(17, "D4",1))













(s.compileSong()).export("s1.mp3", format="mp3")
