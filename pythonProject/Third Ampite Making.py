import tkinter  # For makes GUI
import cv2  # openCV  (pip install opencv-python)
# PIL - Python Imaging Library to display the image on GUI (pip install pillow)
import PIL.Image, PIL.ImageTk
from functools import partial  # For give agruments into the functions
import threading  # It prevents from block program
import imutils  # It resizes photos
import time

# Global Variables

# for making a pop up screen took height and width
SET_WIDTH = 650
SET_HEIGHT = 368

flag = True

stream = cv2.VideoCapture("clip5.mp4")


# This function for button to speed control
def play(speed):
    global flag
    # Play the video reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    if flag:
        canvas.create_text(170, 25, fill="red", font="Time 27 italic bold", text="Decision Pending...")
    flag = not flag

    print(f"You clicked on play. Speed is {speed}")


# This function will return out
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


# It will give the final decision
def pending(decision):
    # 1.Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))  # To get image object
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 2.Wait for 2 sec
    time.sleep(2)

    # 3.Display sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))  # To get image object
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 4.Wait for 1.5 sec
    time.sleep(1.5)

    # 5.Display out/not out
    if decision == 'out':
        decisionImg = 'out.png'
    else:
        decisionImg = 'not out.png'
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))  # To get image object
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


# This function will return not out
def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


# To get a pop up window and title . tkinter GUI starts from here
window = tkinter.Tk()
window.title("Bappy's Third Umpire Decision Review System")

# To canvas welcome.png into GUI
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<<Previous (Fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<<Previous (Slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (Fast)>>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Next (Slow)>>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Give Out!", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out!", width=50, command=not_out)
btn.pack()

window.mainloop()