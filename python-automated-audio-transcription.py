import whisper
import sys
import os

model = whisper.load_model("base")
file_path = input('Path to file?')
name_to_save = os.path.basename(file_path)
result = model.transcribe(file_path)
print(name_to_save)
print(result["text"])

with open((name_to_save) + '.txt', 'w') as file:
    file.write(result["text"])
    file.close()
