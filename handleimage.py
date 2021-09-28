import sys

from PIL import Image

###########################################---MENU BUILDER---###########################################

def set_line(size=50):
    return '-' * size


def header(text):
    print(set_line())
    print(text.center(50))
    print(set_line())


def menu(list):
    header('MAIN MENU')
    print('Select your option to start:\n')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    print('\n{}'.format(set_line()))


menu(['Image Pixels Counter', 'Image Rotator', 'Image Dimensions', 'Exit'])

##########################################################################################################

# Importing a simples bird image for a variable called 'image'
image = Image.open("image/bird.png")


def imgPixelCounter():
    global image
    width = image.size[0]
    height = image.size[1]

    print('This bird image has:')
    print('\nWidth: {}'.format(width))
    print('\nHeight: {}'.format(height))


def rotatorImg():
    global image
    img01 = image
    img01_rotated = img01.rotate(30)
    img01_rotated.show()

    img02 = image
    img02_rotated = img02.rotate(60)
    img02_rotated.show()


def showImgDimensions():
    global image
    print(image.format)
    print(image.mode)
    print("'l' means 8-bit pixels, black and white")


def gettingOut():
    print('Bye, but before...')
    print(set_line())
    print('\nRômulo Melendez Lima')
    print('Matrícula: 2016202466')
    print('Centro Universitário Unicarioca')
    print('28/09/2021 - 02:02 - Terça-feira\n')
    print(set_line())
    sys.exit()


def default():
    print('Wrong option dude, try again later!')


def switch(caseSelected):
    if caseSelected == 1:
        return imgPixelCounter()
    elif caseSelected == 2:
        return rotatorImg()
    elif caseSelected == 3:
        return showImgDimensions()
    elif caseSelected == 4:
        return gettingOut()
    else:
        default()


if __name__ == '__main__':
    caseSelected = int(input())
    switch(caseSelected)
