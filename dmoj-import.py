#TODO:
#from django.utils import timezone
#from django.contrib.auth.models import User
#from judge.models import Problem, Judge
import os

def main():
	copyTest()	

def copyTest():
	testsDir = "chs"
	promblemsDir = "/etc/dmoj/problems"

	for problem in os.listdir(testsDir):
		problemSource = os.path.join(testsDir, problem)
		problemDest = os.path.join(promblemsDir, problem)

		#creating the dmoj problem folder
		os.system(f"mkdir -p {problemDest}")

		for file in os.listdir(problemSource):
			if file.endswith(".zip") or file.endswith(".yaml"):
				os.system(f"cp {os.path.join(problemSource, file)} {os.path.join(problemDest, file)}")			

if __name__ == "__main__":
	main()
