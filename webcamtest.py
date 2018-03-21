import cv2
import time
import sys
import subprocess

def main():
	cam = cv2.VideoCapture(0)
    
	frame = cam.read()[1]
	time.sleep(1)
	
	cv2.imwrite(filename='/home/ahalyamandana/tensorflow-for-poets-2/tf_files/sign_photos/img3.jpg', img=frame)

	response = input("Please enter the letter: ")

	if (response == "o"):


		time.sleep(1)

		subprocess.call("python -m  scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=tf_files/sign_photos/img3.jpg", shell=True)
	
	
	
	

if __name__ == '__main__':
	main()



