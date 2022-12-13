import os
import json

PROBLEMS_DIR = "chs"
PROBLEMS_TEMPLATE_ID = 1

def main():
	html2md()
	yamlFiles()
	pythonFiles()

def html2md():
	for folder in os.listdir(PROBLEMS_DIR):
		problem = os.path.join(PROBLEMS_DIR, folder)

		for file in os.listdir(problem):
			if file.endswith(".html"):
				html = os.path.join(problem, file)
				md = os.path.join(problem, "statement.md")
				os.system(f"pandoc {html} -t gfm-raw_html -o {md}")
				os.system(f"""cat <<EOT >> {md}

----------

** Autoria: **
[Gerard Falcó](https://github.com/gerardfp)
""")


def yamlFiles():
	for folder in os.listdir(PROBLEMS_DIR):
		problem = os.path.join(PROBLEMS_DIR, folder)		

		for file in os.listdir(problem):
			if file.endswith(".zip"):
				#unzip test cases
				zip = os.path.join(problem, file)
				os.system(f"unzip -u {zip} -d {problem}")

				#create the file
				output = os.path.join(problem, "init.yml")
				os.system(f"touch {output}")
				os.system(f"echo 'archive: {file}' > {output}")
				os.system(f"echo 'hints: [unicode]' >> {output}")
				os.system(f"echo 'output_prefix_length: 1000' >> {output}")
				os.system(f"echo 'test_cases:' >> {output}")

				#counting the cases
				count = 0
				for test in os.listdir(os.path.join(problem, "input")):
					count+=1

				#setup the cases
				for i in range(0, count-1):
					appendTestCase(output, i, 0)

				#the last one always scores 1
				appendTestCase(output, count-1, 1)				

def pythonFiles():
	for folder in os.listdir(PROBLEMS_DIR):
		problem = os.path.join(PROBLEMS_DIR, folder)
				
		for file in os.listdir(problem):
			if file.endswith(".json"):
				with open(os.path.join(problem, file), 'r') as f:
					data = json.load(f)

			if file.endswith(".md"):
				with open(os.path.join(problem, file), 'r') as f:
					description = f.read()
					
		#create the file
		output = os.path.join(problem, "import.py")
		os.system(f"touch {output}")
		os.system(f"echo '' > {output}")

		#TODO: missing creators and curator
		os.system(f"""cat <<EOT >> {output}
from django.utils import timezone
from django.contrib.auth.models import User
from judge.models import Problem, Judge

p = Problem.objects.get(id={PROBLEMS_TEMPLATE_ID})
p.pk = None
p.code="{data['model']['slug'][0:20]}"
p.name="{data['model']['name']}"
p.summary="{data['model']['preview']}"
p.description='''{description}'''
p.is_public=False
p.date=timezone.now()
p.save()
""")
		

def appendTestCase(output, i, points):
	num = str(i).zfill(2)
	os.system(f"echo '- in: input/input{num}.txt' >> {output}")
	os.system(f"echo '  out: output/output{num}.txt' >> {output}")					
	os.system(f"echo '  points: {points}' >> {output}")

if __name__ == "__main__":
	main()
