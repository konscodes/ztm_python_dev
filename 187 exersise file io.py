from pathlib import Path
from googletrans import Translator

translator = Translator()
script_path = Path(__file__).resolve()
script_parent = script_path.parent
data_file_path = script_parent / 'files' / 'text.txt'

with open(data_file_path) as my_file:
    input = my_file.read()
    result = translator.translate(input, dest='ja')
    print(result.text)
