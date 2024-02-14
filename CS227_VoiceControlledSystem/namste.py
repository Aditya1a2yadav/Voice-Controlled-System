from PIL import Image
import time
def namaste():
    image_path="C:/Users/Dell/Desktop/Mini_Project/namaste.png"
    image = Image.open(image_path)

    image.show()
    time.sleep(5)
    image.close()