# BlackInk2Colour

Often the black ink in a printer is first to run out or stops working. If you have a colour printer you can substitute black for another colour.

## Requirements

Python 3

[pdf2image](https://github.com/Belval/pdf2image)

### Windows

If using windows you need to [download poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/) a PDF rendering library.

### Mac

Install [popler for mac](http://macappstore.org/poppler/)

### Linux

Most linux distros already come with the required modules. If not, install poppler-utils

## Usage

If using Windows open config.txt and update poppler_path to location of poppler bianry. Example:

    poppler_path = "C:\poppler-21.03.0\Library\bin"

You can also change the default colour by changing default_colour. Example:

    default_colour = "66, 135, 245"

### Running the script

    $ python BlackInk2Colour [pdf_file_path] [(Optional) RGB Values in R,G,F format]
    // Example 1
    $ python BlackInk2Colour dummy.pdf
    // Example 2
    python BlackInk2Colour dummy.pdf (150, 120, 125)

### Test Input

![Input](https://i.imgur.com/pGE5vnq.jpg)

### Test Output

![Output](https://i.imgur.com/RUCW6AA.jpg)
