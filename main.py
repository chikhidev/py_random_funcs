import requests
import os
import shutil
import zipfile
import time
import random

while True:
    try:
        # The GitHub repository URL
        repo_url = input('Enter github repo url: ')

        if repo_url == '':
            break

        print('cloning from "' + repo_url + '"')

        # The directory where you want to extract the functions
        output_dir = "./"

        # Download the repository archive
        r = requests.get(repo_url + "/archive/refs/heads/main.zip")

        if r.status_code == 200:
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
                if shutil.which("git"):
                    os.system("git add .;git commit -m added;git push origin master")
                    time.sleep(5)  # Wait for the push to finish
                    os.chdir(output_dir)

        else:
            print(f"Failed to download repository {repo_url} with status code {r.status_code}")

    except Exception as e:
        print(f"Error: {e}")
