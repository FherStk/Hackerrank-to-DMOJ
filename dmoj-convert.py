#from django.utils import timezone
#from django.contrib.auth.models import User
#from judge.models import Problem, Judge
import os

def main():
	#html2md()
	yamlFiles()

def html2md():
	directory = "chs"

	for folder in os.listdir(directory):
		problem = os.path.join(directory, folder)

		for file in os.listdir(problem):
			if file.endswith(".html"):
				html = os.path.join(problem, file)
				md = os.path.join(problem, "statement.md")
				os.system(f"pandoc {html} -t gfm-raw_html -o {md}")

def yamlFiles():
	directory = "chs"

	for folder in os.listdir(directory):
		problem = os.path.join(directory, folder)		

		for file in os.listdir(problem):
			if file.endswith(".zip"):
				#unzip test cases
				zip = os.path.join(problem, file)
				os.system(f"unzip -f {zip} -d {problem}")

				#create the file
				output = "init.yaml"
				os.system(f"touch {output}")
				os.system(f"echo 'archive: {zip}' > {output}")
				os.system(f"echo 'test_cases:' >> {output}")

				#setup the cases
				first = True
				for test in os.listdir(os.path.join(problem, "input")):
					#only the last test scores
					if not first:
						os.system(f"echo '  points: 0' >> {output}")
						first = False

					#in
					os.system(f"echo '- in: {test}' >> {output}")

					#out
					test = test.replace("input", "output")
					os.system(f"echo '  out: {test}' >> {output}")

				#the last one always scores 1
				os.system(f"echo '  points: 1' >> {output}")

if __name__ == "__main__":
	main()
