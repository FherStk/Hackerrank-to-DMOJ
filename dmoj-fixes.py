import os
import json

DMOJ_DIR = "/etc/dmoj"
PROBLEMS_DIR = "chs"

def main():
	fix_code()
		
def fix_code():
	for folder in os.listdir(PROBLEMS_DIR):
		name = folder.replace("-", "")[0:20]

		oldDir = os.path.join(PROBLEMS_DIR, folder)
		newDir = os.path.join(PROBLEMS_DIR, name)

		command = f'from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge; p = Problem.objects.filter(code="{folder}")[0]; p.code = "{name}"; p.save();'
		os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo '{command}' | python3 {DMOJ_DIR}/site/manage.py shell")
		os.system(f"mv {oldDir} {newDir}")

if __name__ == "__main__":
	main()
