import filetype

filename = "/path/to/file.jpg"

if filetype.image(filename):
    print(f"{filename} is a valid image...")
elif filetype.video(filename):
    print(f"{filename} is a valid video...")
else:
    print("not image file")
