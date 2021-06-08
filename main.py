from polyglot.text import Text

script_file = open("input/Thai-Script.txt", "r")

script_text = script_file.read()
polytext = Text(script_text)

for x in polytext.transliterate("en"):
    print(x)