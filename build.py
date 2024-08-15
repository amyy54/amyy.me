from dataclasses import dataclass
from pathlib import Path
import subprocess
import os
import shutil
import sys

STATIC_DEPLOYED = "/static/mini.amyy.me/"
STATIC_TESTING = "/static/"

@dataclass
class StaticFile:
    filename: str
    path: str

def generated_file_name(filename: str, version: str) -> str:
    filenameArr = filename.split(".")
    filenameArr.insert(-1, version)
    output = ""
    for name in filenameArr:
        output += name + "."
    return output[:-1]

def new_html_file(filename: str, result: str, static: list[StaticFile], version: str) -> None:
    output = result.replace("<script src=https://cdn.tailwindcss.com></script>", "")
    for file in static:
        output = output.replace(f"={file.filename}", f"={file.path}")
    output = output.replace("REPLACE_ALL_GIT_VERSION", version)
    with open(f'build/{filename}', 'w+') as html_file:
        html_file.write(output)

if __name__ == "__main__":
    STATIC_LOCATION = STATIC_TESTING if "-d" in sys.argv else STATIC_DEPLOYED

    static_files: list[StaticFile] = []
    # Get Git Version
    result = subprocess.run(['git', 'describe', '--always'], stdout=subprocess.PIPE)
    GIT_VERSION = result.stdout.decode('utf-8').strip()

    shutil.rmtree("build/", ignore_errors=True)

    subprocess.run(['mkdir', '-p', 'build/static/fonts'])

    for filename in os.listdir("src/fonts/"):
        shutil.copyfile(f"src/fonts/{filename}", f"build/static/fonts/{filename}")
        if filename.endswith(".ttf"):
            static_files.append(StaticFile(
                filename=filename,
                path=f'{STATIC_LOCATION}fonts/{filename}'
            ))

    for filename in os.listdir("src/favicon/"):
        shutil.copyfile(f"src/favicon/{filename}", f"build/{filename}")

    for filename in os.listdir("src/"):
        if filename.endswith(".png"):
            shutil.copyfile(f"src/{filename}", f"build/static/{filename}")
            static_files.append(StaticFile(
                filename=filename,
                path=f'{STATIC_LOCATION}{filename}'
            ))
        elif filename.endswith(".css"):
            file = open(f'build/static/{generated_file_name(filename, GIT_VERSION)}', 'w+')
            subprocess.run(['npx', 'tailwindcss', '-i', f'src/{filename}', '-o', f'build/static/{filename}'])
            subprocess.run(['npx', 'minify', f'build/static/{filename}'], stdout=file)
            file.close()
            static_files.append(StaticFile(
                filename=filename,
                path=f'{STATIC_LOCATION}{generated_file_name(filename, GIT_VERSION)}'
            ))
            os.remove(f'build/static/{filename}')
        elif filename.endswith(".js"):
            file = open(f'build/static/{generated_file_name(filename, GIT_VERSION)}', 'w+')
            result = subprocess.run(['npx', 'minify', f'src/{filename}'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
            result = result.replace("REPLACE_ALL_GIT_VERSION", GIT_VERSION)
            file.write(result)
            file.close()
            static_files.append(StaticFile(
                filename=filename,
                path=f'{STATIC_LOCATION}{generated_file_name(filename, GIT_VERSION)}'
            ))
        # elif not filename.endswith(".html"):
        #     shutil.copyfile(f"src/{filename}", f"build/{filename}")

    open(Path.home().joinpath(".ttreerc"), "a").close()
    subprocess.run(["ttree", "-s", "src/", "-d", "build/ttree/"])
    for filename in os.listdir("build/ttree/"):
        if filename.endswith(".html"):
            result = subprocess.run(['npx', 'minify', f'build/ttree/{filename}'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
            new_html_file(filename, result, static_files, GIT_VERSION)
    shutil.rmtree("build/ttree/") 
