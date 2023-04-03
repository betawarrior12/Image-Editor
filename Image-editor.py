from PIL import Image, ImageEnhance, ImageFilter
import os, shutil

path = "./imgs"
pathOut = "./editedImgs"
Extra = "C:\\Users\\USER\\Pemi\\Downloaded-images-and-videos\\Downloaded"

def edit_images(path, pathOut, Extra, ext=False):
    if ext == False:
        for filename in os.listdir(path):
            img = Image.open(f"{path}\\{filename}")

            edit = img.filter(ImageFilter.SHARPEN)

            factor = 1.5
            contrast = ImageEnhance.Contrast(edit)
            edit = contrast.enhance(factor)

            clean_name = os.path.splitext(filename)[0]

            edit.save(f"{pathOut}\\{clean_name}_edited.jpg")
    else:
        for filename in os.listdir(path):
            img = Image.open(f"{path}\\{filename}")

            edit = img.filter(ImageFilter.SHARPEN)

            factor = 1.5
            contrast = ImageEnhance.Contrast(edit)
            edit = contrast.enhance(factor)

            clean_name = os.path.splitext(filename)[0]

            edit.save(f"{pathOut}\\{clean_name}_edited.jpg")

        for filename in os.listdir(Extra + "\\Normal\\"):
            img = Image.open(f"{Extra}\\Normal\\{filename}")

            edit = img.filter(ImageFilter.SHARPEN)

            factor = 1.5
            contrast = ImageEnhance.Contrast(edit)
            edit = contrast.enhance(factor)

            clean_name = os.path.splitext(filename)[0]

            edit.save(f"{Extra}\\Edited\\{clean_name}_edited.jpg")

    print("Done: ")


def create_pathout(path):
    if path.strip("./") in os.listdir():
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)


def main():

    print("Started: ")
    create_pathout(pathOut)
    edit_images(path, pathOut, Extra, ext=False)
    print("Ended: ")


if __name__ == "__main__":
    main()
