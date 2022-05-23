# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example1.txt'
# urllib.request.urlretrieve(url, filename)

# Read the Example1.txt
example1 = "Example1.txt"
# file1 = open(example1, "r")

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)