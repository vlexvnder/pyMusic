def parseRawSong(instruction, delim):
    instruction_array =  instruction.split(delim)
    return instruction_array

def parse(instruction):
    instruction_array = instruction.split();
    return instruction_array

def createNote(instruction):

    # instructions have:
    # a moment (the location of the note in the song, in beats)
    # a noteName (the name of the audioSegment associated with the note
    # a length (expressed in beats)

    moment = instruction[0]

    noteName = instruction[1]