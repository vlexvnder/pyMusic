from Note import Note
def parseRawSong(instruction, delim):
    instruction_array =  instruction.split(delim)
    return instruction_array

def parse(instruction):
    instruction_array = instruction.split(" ")
    return instruction_array

def createNote(instruction, moment=""):

    # instructions have:
    # a moment (the location of the note in the song, in beats)
    # a noteName (the name of the audioSegment associated with the note
    # a length (expressed in beats)
    instruction = parse(instruction)
    if(moment == ""):
        moment = instruction[0]

        noteName = instruction[1]

        noteLength = instruction[2]
    else:
        noteName = instruction[0]

        noteLength = instruction[1]

    return Note(moment, noteName, noteLength)