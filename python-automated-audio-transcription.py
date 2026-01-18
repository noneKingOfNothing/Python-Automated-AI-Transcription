#Jonathan 'Jack' Thompson
#1/18/26
#automated ai transcription - requires whisper

#pull libraries - whisper transcribes, the others allow file manipulation
import whisper
import sys
import os

#load the model so it can be used to process an audio file, determine the path of the file or folder you want to transcribe.
model = whisper.load_model("base")
file_path = input('Path to file?')
#create a name for the output file using the name of the input file
name_to_save = os.path.basename(file_path)
#process the file
result = model.transcribe(file_path)

#print results to the terminal so I know it works without opening files
print(name_to_save)
print(result["text"])

#save the result to a file named after the input
with open((name_to_save) + '.txt', 'w') as file:
    file.write(result["text"])
    file.close()

#profit
