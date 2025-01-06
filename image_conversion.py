# image manipulation
from PIL import Image
# access the os(file system) and provide cla(command-line argument)
import sys , os

for arg in sys.argv[1:]:
    filename,extension = os.path.splitext(arg) # divide into file name and extension separately and add jpg
    add_extension = filename + '.jpg'
    # save the new file conversion if the file given exist on the user's os
    if add_extension != arg:
        try:
            with Image.open(arg) as img:
                img.save(add_extension)
        except:
            print('Image cant be converted into JPG')

