import os

DMOJ_DIR = "/etc/dmoj"

def main():	
	set_language(9) #Java8	
	set_language(21) #Java (latest installed)	
	set_language(20) #C# 6 (Mono)

def set_language(id):
	command = "from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge; l = Language.objects.get(id={id}); for s in Problem.objects.all():exec('s.allowed_languages.add(l); s.save()')"
	os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo '{command}' | python3 {DMOJ_DIR}/site/manage.py shell")

if __name__ == "__main__":
	main()
