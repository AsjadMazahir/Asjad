# prompting the user
extensions = ('.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip')
file = input("Name of file: ").lower().strip()

# checking for extension
if file.endswith(extensions):
    name, ext = file.rsplit('.', 1)
    if ext == 'jpeg' or ext == 'jpg':
        print("image/jpeg")
    elif ext == 'png' or ext == 'gif':
        print(f"image/{ext}")
    elif ext == 'txt':
        print(f"text/{name}")
    else:
        print(f"application/{ext}")

else:
    print("application/octet-stream")
