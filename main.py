import openpyxl
import json
import sys
import io

# korean Unicode convert error solved.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook("word.xlsx")
sheet = wb.active

words = []
for row in sheet.iter_rows(min_row=1, values_only=True):
    if row[0] and row[1]:
        words.append({"word": row[0], "definition": row[1]})

js_code = "const words = [\n"
for i, entry in enumerate(words):
    comma = "," if i < len(words) - 1 else ""
    js_code += f"  {{ word: {json.dumps(entry['word'], ensure_ascii=False)}, definition: {json.dumps(entry['definition'], ensure_ascii=False)} }}{comma}\n"
js_code += "];"

print(js_code)


