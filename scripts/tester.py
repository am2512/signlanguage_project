import subprocess
import time
import sys


def main():


	

	time.sleep(1)

	subprocess.call("python -m  scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=tf_files/sign_photos/test.jpg", shell=True)
	
	

if __name__ == '__main__':
	main()




