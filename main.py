from polyglot.text import Text
import json as j

script_file = open("input/Thai-Script.txt", "r")

script_text = script_file.read()
polytext = Text(script_text)

transcription_output = open("input/output.json", "r").read()
json = j.loads(transcription_output)
video_words = json['results'][0]['alternatives'][0]['words']

script_output = []
video_output = []

for x in polytext.transliterate("en"):
    script_output += [str(x)]

for x in video_words:
    t = Text(x['word'])
    word = t.transliterate("en")[0]

    if word != None:
        video_output += [(word, x['startTime'], x['endTime'])]


script_output = list(filter(None, script_output))

