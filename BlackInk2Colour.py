from pdf2image import convert_from_path
from PIL import Image
import sys
from typing import Optional

# Configuration
with open("config.txt") as f:
    lines = f.readlines()
    if lines[1].startswith("poppler_path = ") and lines[3].startswith("default_colour = "):
        poppler_path = lines[1].split('"')[1]
        default_colour = [int(i) for i in lines[3].split('"')[1].split(",")]
        default_colour = tuple(default_colour)
    else:
        raise Exception(
            "Error: config.txt has been altered. Please redownload.")


def change_black_ink(pdf_path: str, new_colour: Optional[tuple] = None):
    """Function that takes an pdf, seperates pdf into seperate jpg images
    and then changes all black pixels to a print friendly colour

    Args:
        pdf_path (str): Path to pdf file
        new_colour (Optional[tuple], optional): Colour to change black pixels to. If None
            it will take the default value from the config.txt file.
   """

    rgb = default_colour if new_colour == None else new_colour
    print("rgb: ", rgb)

    # Windows requires path to poppler binary file. Path is specified in config.txt
    if sys.platform.startswith("win"):
        pdf_pages = convert_from_path(pdf_path, poppler_path=poppler_path)
    else:
        pdf_pages = convert_from_path(pdf_path)

    saved_pages = []
    for i, page in enumerate(pdf_pages):
        file_name = f"page {i}.jpg"
        page.save(file_name, "JPEG")
        saved_pages.append(file_name)
        print(file_name + " saved")

    for image in saved_pages:
        print(image)
        img = Image.open(image).convert("RGB")
        pixdata = img.load()

        img_width, img_height = img.size[0], img.size[1]

        # Loop each indivudal pixel
        for width in range(img_width):
            for height in range(img_height):
                pixel_colour = pixdata[width, height]
                # If all red, green, blue under 60
                if sum([i < 60 for i in pixel_colour]) == 3:
                    pixdata[width, height] = rgb

        img.save(image)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        change_black_ink(args[1])
    elif len(args) == 3:
        print("arg 2:", args[2])
        try:
            tuple([int(i) for i in args[2].split(",")])
            new_colour = tuple([int(i) for i in args[2].split(",")])
        except:
            raise Exception(
                """Error: Second parameter new_colours could not be read.
                Needs to be in R,G,B format for example 150,150,150""")
        change_black_ink(args[1], new_colour)
    else:
        print("Error: Incorrect amount of paramters given \n"
              "To Run program: \n$ python BlackInk2Colour file.pdf")
