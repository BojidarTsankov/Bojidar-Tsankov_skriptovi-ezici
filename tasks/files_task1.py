from pathlib import Path

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

documents_path = Path("C:\\Users\\bjtsa\\Documents\\")

for file_name in myFiles:
    file_path = documents_path / file_name

    f = open(file_path, 'w')
    f.write(f"Hello {file_name}")
    f.close()

    print(f"Created file: {file_path}")
