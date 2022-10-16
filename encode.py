from stegano import lsb
import cv2
import os
import sys
import aesutil

VIDEO_TO_ENCODE = sys.argv[1]

def createTmp():
    temp_folder = "tmp2"
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
createTmp() 
def countFrames():
    cap = cv2.VideoCapture(VIDEO_TO_ENCODE)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frame in video are : {length}")
    return length
countFrames()

FRAMES = list(map(int, input("Type FRAME NUMBERS seperated by space in ascending order : ").split()))
#print(FRAMES)
# key = input("Enter the key : ")
TEXT_TO_ENCODE = input("Enter text to encode : ")

def textEncrypt():
    res=TEXT_TO_ENCODE
    key123=int(input("Choose key type /n 1.HEX /n 2.ASCII"))
    key = input("Enter the key : ")
    if key123==1:
        msg = aesutil.encrypt(key=key,source=res) 
    else:
        msg = aesutil.encrypt(key=key,source=res,keyType='ascii')
    print(f"AES-256 encoded message: \n {msg}")
textEncrypt()

def prepare():
    global TEXT_MAPPED_TO_FRAMES
    global TEXT_TO_ENCODE
    # Prepare the parts of text to be encoded in respective frames
    st=0
    end=45
    length = len(TEXT_TO_ENCODE)
    for fn in Frames:
        txt = TEXT_TO_ENCODE[st:end]
        TEXT_MAPPED_TO_FRAMES[fn]=txt
        print(f"[INFO] Frame {fn} has {txt} ")
        st = endend = st + 45
        if end>length:
            end=length
def encodeVideo():
    #Split video into frames
    cap = cv2.VideoCapture(Main_Video)
    while True:
        success, frame = cap.read()
        if not success:
            break  
   """