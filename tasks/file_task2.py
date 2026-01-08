from pathlib import Path

os_type = str(input("Enter your os (W/L): ")).upper()

file_path = str(input("Path: "))

p = Path(file_path)

if os_type == 'W':
    if p.drive != "":
        print("Yes")
    else:
        print("No")

elif os_type == 'L':
    if p.is_absolute() and file_path.startswith("/"):
        print("Yes")
    else:
        print("No")

else:
    print("Invalid os!")
