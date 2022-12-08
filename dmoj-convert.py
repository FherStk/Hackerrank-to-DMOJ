#from django.utils import timezone
#from django.contrib.auth.models import User
#from judge.models import Problem, Judge
import os

def main():
	html2md()

def html2md():
	directory = "chs"

	for folder in os.listdir(directory):
		problem = os.path.join(directory, folder)

		for file in os.listdir(problem):
			if file.endswith(".html"):
				html = os.path.join(problem, file)
				md = os.path.join(problem, "statement.md")
				os.system(f"pandoc {html} -t gfm-raw_html -o {md}")

if __name__ == "__main__":
	main()
