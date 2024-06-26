from bs4 import BeautifulSoup
import json
from datetime import datetime
import shutil, os

def extract_grid_from_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    cells = soup.find_all(class_='queens-cell')

    colors = []
    for cell in cells:
        class_attribute = cell.get('class')
        if class_attribute:
            for attribute in class_attribute:
                if 'cell-color-' in attribute:
                    color = int(attribute.split('-')[-1])
                    colors.append(color)
                    break

    return colors

html_file_path = "./queens.htm"
colors = extract_grid_from_html(html_file_path)

today = datetime.today()
formatted_date = today.strftime("%m_%d_%Y")
file_path = f"public/_grids/{formatted_date}.json"

data = {"gridData":colors}
with open(file_path, 'w') as f:
    json.dump(data, f)

# print(f"Grid saved to {file_path}")
print(f"{formatted_date}.json")
shutil.rmtree("./queens_files")
os.remove(html_file_path)