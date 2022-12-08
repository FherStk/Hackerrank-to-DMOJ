import os

def main():
	html2md()
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
				os.system(f"unzip -u {zip} -d {problem}")

				#create the file
				output = os.path.join(problem, "init.yaml")
				os.system(f"touch {output}")
				os.system(f"echo 'archive: {file}' > {output}")
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

def appendTestCase(output, i, points):
	num = str(i).zfill(2)
	os.system(f"echo '- in: input/input{num}.txt' >> {output}")
	os.system(f"echo '  out: output/output{num}.txt' >> {output}")					
	os.system(f"echo '  points: {points}' >> {output}")

if __name__ == "__main__":
	main()
