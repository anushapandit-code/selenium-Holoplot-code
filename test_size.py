import unittest
from circlemaker import draw_image
from PIL import Image, ImageDraw


class TestCircle(unittest.TestCase):
    def test_circle_size(self):
        draw_image(89, 89, "test.jpg")
        file_name = "test.jpg"
        with Image.open(file_name) as image:
            width, height = image.size
            print("size of the 'test1.png' image: " + str(image.size))
            print("mode of the 'test1.png' image: " + str(image.mode))

        try:
            img = Image.open("test.jpg")
            img.thumbnail((100, 100))
            img.save("new_test.png")
            file_name = "new_test.png"
            with Image.open(file_name) as image:
                width, height = image.size
            print("size of the 'test1.png' image: " + str(image.size))
            print("mode of the 'test1.png' image: " + str(image.mode))

        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
    print("everything is passed")


