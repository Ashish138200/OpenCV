# OpenCV
![image](https://drive.google.com/uc?export=view&id=1fdeX9QP6yaXk68qPstHdB4aHen7R5XE1)<br/>
![Alt Text](https://img.shields.io/badge/Python-3.7.4-red) <br/>
### Installing the library

If you haven't installed OpenCV yet, please do so by following the instructions below.  If you don't know if you have OpenCV, please open Python and type import cv2. If you don't get an error, it means OpenCV is installed.

#### To install:
1. Open the command line and type
```bash
pip install opencv-python 
```
2. Then open a Python session and try:
```bash
import cv2 
```
3. If you get no errors, that means you installed OpenCV successfully. If you get an error please see the FAQs below:

### FAQs

1.**My opencv installation didn't go well on Windows**<br/>
Solution:
  1. Uninstall opencv with:
  ```bash
  pip uninstall opencv-python
  ```
  2. Download a wheel (.whl) file from this link and install it with pip. Make sure you download the correct file for your Windows version and your Python version. For example,     for Python 3.6 on Windows 64-bit you would do this:
  ```bash
  pip install opencv_python‑3.2.0‑cp36‑cp36m‑win_amd64.whl 
  ```
  3. Then try to import cv2 in Python again. If there's still an error, then please type the following again in the command line:
  ```bash
  pip install opencv-python 
  ```
  4. Now you should successfully import cv2 in Python

