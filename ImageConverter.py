from PIL import Image
import os

def convert_to_jpeg(path):
    filename = path[:-4]
    image = Image.open(path)
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, (0, 0), image)
    new_image.convert('RGB').save(filename + '.jpg', "JPEG")


def convert_Cwd(path=os.getcwd(), top=''):
##    print('PATH', path)
##    print('TOP', top)
    newtop = top + '\\'
    if top == '':
        newtop =  ''
    allfiles = os.listdir(path)
##    print("ALL FILES IN", path)
##    print(allfiles)
    for file in allfiles:
        if file[-4:] == '.png':
##            print(newtop + file)
            convert_to_jpeg(newtop + file)
        else:
            
##            print("checking to see if ",file," is a folder...")
            if os.path.isdir(path + '\\' + file):
##                print(file + " Is a folder")
                convert_Cwd(path + '\\' + file,newtop + file)
##            else:
##                print("it wasnt a folder")


            
        

if __name__ == '__main__':
    print("FILES IN CURRENT DIRECTORY:\n", os.listdir(os.getcwd()))
    print("Converting Images...")
    convert_Cwd()
    print('Done')
