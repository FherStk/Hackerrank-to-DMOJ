import os

DMOJ_DIR = "/etc/dmoj"
PROBLEMS_DIR = "chs"

def main():
	copyTest()	

def copyTest():
	for problem in os.listdir(PROBLEMS_DIR):
		problemSource = os.path.join(PROBLEMS_DIR, problem)
		problemDest = os.path.join(DMOJ_DIR, "problems", problem)

		#creating the dmoj problem folder
		os.system(f"mkdir -p {problemDest}")

		for file in os.listdir(problemSource):
			if file.endswith(".zip") or file.endswith(".yaml"):
				os.system(f"cp {os.path.join(problemSource, file)} {os.path.join(problemDest, file)}")

			if file.endswith(".py"):
				os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && python3 {DMOJ_DIR}/site/manage.py shell < {os.path.join(problemSource, file)}")				

if __name__ == "__main__":
	main()