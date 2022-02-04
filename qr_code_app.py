#QRCode script done by Lyon

#Refer to qr_code_app_version.txt for version history

#(Current) V1.2 as of 280122:
# - Create introduction page to prompt user for app use
# - Allow user to scan and read QR code from camera
# - Save QR Code in PNG format for better web quality 

from cProfile import label
from winreg import HKEY_LOCAL_MACHINE
from cv2 import VideoCapture
import qrcode
from PIL import Image
import cv2 
import webbrowser

#QRCode Generator Function
def igenerate():
    print("You may enter your desired link to convert.")
    g_source = input("What is the link? ")
    g_img_name = input("What name do you want to save your QR code as?(only underscores are allowed) ")
    g_img = qrcode.make(g_source)
    g_img.save("{}QR.png".format(g_img_name))

#QRCode Reader Function
def iread():
    det = cv2.QRCodeDetector()
    r_reply = input("Do you want to scan or upload a QR Code to read? ")
    while r_reply.lower() != 'scan' or r_reply.lower() != 'upload':
        if r_reply.lower() == 'scan':
            cap = cv2.VideoCapture(0)
            while True:
                _, scan_img = cap.read()
                data, bbox, _ = det.detectAndDecode(scan_img)
                if data:
                    a = data
                    cv2.imshow("QRCODEscanner", scan_img)
                    if cv2.waitKey(1) == ord("q"):
                        break
                    b = webbrowser.open("https://{}".format(str(a)))
                    cap.release()
                    cv2.destroyAllWindows()

        elif r_reply.lower() == 'upload':    
            print("Ensure your QR Code(s) are uploaded in the present directory.")
            r_source = input("What is the QR Code you would like me to read? ")
            r_img=cv2.imread('{}'.format(r_source))
            val, pts, st_code= det.detectAndDecode(r_img)
            webbrowser.open('https://{}'.format(val))
        else:
            r_reply = input("Sorry, you didn't enter a valid input. Do you want to scan or upload QR Code? ")

#Introduction Page
print("Hello! Welcome to QR Code App.")
ans = input("Do you want to generate or read QR Code? ")
while ans.lower() != 'generate' or ans.lower() != 'read':
    if ans.lower() == 'generate':
        igenerate()
    elif ans.lower() == 'read':
        iread()    
    else: 
        ans = input("Sorry, you didn't enter a valid input. Do you want to generate or read QR Code? ")

