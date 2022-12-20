import os
import json

DMOJ_DIR = "/etc/dmoj"
PROBLEMS_DIR = "chs"

def main():
	fix_code()
	fix_prefix()
	fix_language()
	fix_author()
	fix_curators
		
def fix_code():
	#fix the BBDD
	command = "from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge; for s in Problem.objects.all():exec('s.code=s.code.replace(\"-\", \"\")[0:20]; s.save()')"
	os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo '{command}' | python3 {DMOJ_DIR}/site/manage.py shell")

	#fix the problems folder
	for folder in os.listdir(PROBLEMS_DIR):
		name = folder.replace("-", "")[0:20]

		oldDir = os.path.join(DMOJ_DIR, "problems", folder)
		newDir = os.path.join(DMOJ_DIR, "problems", name)
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

def fix_language():
	command = "from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge; l = Language.objects.get(id=9); for s in Problem.objects.all():exec('s.allowed_languages.add(l); s.save()')"
	os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo '{command}' | python3 {DMOJ_DIR}/site/manage.py shell")

def fix_author():
	command = "from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge, Profile; u = Profile.objects.get(id=1); for s in Problem.objects.all():exec('s.authors.add(u); s.save()')"
	os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo '{command}' | python3 {DMOJ_DIR}/site/manage.py shell")

def fix_curators():
	command = "from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge, Profile; u = Profile.objects.get(id=1); for s in Problem.objects.all():exec('s.authors.add(u); s.save()')"
	os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo '{command}' | python3 {DMOJ_DIR}/site/manage.py shell")

if __name__ == "__main__":
	main()
