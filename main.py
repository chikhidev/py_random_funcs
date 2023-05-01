import requests
import os
import shutil
import zipfile
import time
import random

# The GitHub repository URL
repo_url = "https://github.com/topics/python-functions"

# The directory where you want to extract the functions
output_dir = "/path/to/output/directory"

# Download the repository archive
r = requests.get(repo_url + "/archive/refs/heads/main.zip")

# Save the archive to a file
with open("repo.zip", "wb") as f:
    f.write(r.content)

# Wait for a random time between 10 to 30 seconds before extracting the archive
time.sleep(random.randint(10, 30))

# Extract the archive to the output directory
with zipfile.ZipFile("repo.zip", "r") as zip_ref:
    zip_ref.extractall(output_dir)

# Delete the archive file
os.remove("repo.zip")

# List all the Python files in the output directory
files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".py")]

# Loop through the files and print their contents
for f in files:
    with open(f, "r") as file:
        print(file.read())
    
    # Wait for a random time between 10 to 30 seconds before adding, committing, and pushing the changes
    time.sleep(random.randint(10, 30))
    
    # Add, commit, and push the changes to the GitHub repository
    os.chdir(output_dir)
    os.system("git add .;git commit -m added;git push origin master")
