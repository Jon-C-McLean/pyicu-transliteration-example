from polyglot.text import Text

script_file = open("input/Thai-Script.txt", "r")

script_text = script_file.read()
polytext = Text(script_text)

transliterated_script = ""

for x in polytext.transliterate("en"):
    transliterated_script += str(x)

    if str(x) != " ":
        transliterated_script += " "

print(transliterated_script)