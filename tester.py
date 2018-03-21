import subprocess
import time
import sys

def main():


	response = input("Please enter the letter: ")

	if (response == "o"):


		time.sleep(1)

		subprocess.call("python -m  scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=tf_files/sign_photos/Opic2.jpg", shell=True)
	
	

if __name__ == '__main__':
	main()




