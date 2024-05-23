import os
from pathlib import Path

# p = './data/images/horses.jpg'
p = 'D:\\UdemyYolo\\yolov9\\data\\images\\horses.jpg'
print(p)

p = str(Path(p).resolve())
print(p)


if os.path.isfile(p):
    print("True")

else:
    print("False")