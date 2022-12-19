import os
import json

DMOJ_DIR = "/etc/dmoj"
PROBLEMS_DIR = "chs"
TEST = "FAKE"

def main():
	#fix_code()
	fix_prefix()
		
def fix_code():
	for folder in os.listdir(PROBLEMS_DIR):
		name = folder.replace("-", "")[0:20]

		oldDir = os.path.join(DMOJ_DIR, "problems", folder)
		newDir = os.path.join(DMOJ_DIR, "problems", name)

		command = f'from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge; p = Problem.objects.filter(code="{folder}")[0]; p.code = "{name}"; p.save();'
		os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo '{command}' | python3 {DMOJ_DIR}/site/manage.py shell")
		os.system(f"mv {oldDir} {newDir}")

def fix_prefix():
	problems = os.path.join(DMOJ_DIR, "problems")
	for folder in os.listdir(problems):
		problem = os.path.join(problems, folder)

		if not problem.endswith(".yml"):
			for file in os.listdir(problem):
				if file.endswith(".yml"):
					file = os.path.join(problem, file)
					with open(file, 'r') as f:
						content = f.read()

						if "output_prefix_length" not in content:
							os.system(f"echo 'output_prefix_length: 500' >> {file}")

if __name__ == "__main__":
	main()
