import subprocess
import os
import shutil

def generated_file_name(filename: str, version: str) -> str:
    filenameArr = filename.split(".")
    filenameArr.insert(-1, version)
    output = ""
    for name in filenameArr:
        output += name + "."
    return output[:-1]

def new_html_file(filename: str, result: str, static: list, version: str) -> None:
    output = result.replace("<script src=https://cdn.tailwindcss.com></script>", "")
    for file in static:
        output = output.replace(f"={file['filename']}", f"={file['path']}")
    with open(f'build/{filename}', 'w+') as html_file:
        html_file.write(output)

if __name__ == "__main__":
    static_files = []
    # Get Git Version
    result = subprocess.run(['git', 'describe', '--always'], stdout=subprocess.PIPE)
    GIT_VERSION = result.stdout.decode('utf-8').strip()

    subprocess.run(['mkdir', '-p', 'build/static'])

    for filename in os.listdir("src/"):
        if filename.endswith(".png"):
            shutil.copyfile(f"src/{filename}", f"build/static/{filename}")
            static_files.append({
                "filename": filename,
                "path": f"static/{filename}"
            })
        elif filename.endswith(".css"):
            file = open(f'build/static/{generated_file_name(filename, GIT_VERSION)}', 'w+')
            subprocess.run(['npx', 'tailwindcss', '-i', f'src/{filename}', '-o', f'build/static/{filename}'])
            subprocess.run(['npx', 'minify', f'build/static/{filename}'], stdout=file)
            file.close()
            static_files.append({
                "filename": filename,
                "path": f'static/{generated_file_name(filename, GIT_VERSION)}'
            })
            os.remove(f'build/static/{filename}')
        elif filename.endswith(".js"):
            file = open(f'build/static/{generated_file_name(filename, GIT_VERSION)}', 'w+')
            result = subprocess.run(['npx', 'minify', f'src/{filename}'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
            result = result.replace("REPLACE_ALL_GIT_VERSION", GIT_VERSION)
            file.write(result)
            file.close()
            static_files.append({
                "filename": filename,
                "path": f'static/{generated_file_name(filename, GIT_VERSION)}'
            })
        elif not filename.endswith(".html"):
            shutil.copyfile(f"src/{filename}", f"build/{filename}")
    
    for filename in os.listdir("src/"):
        if filename.endswith(".html"):
            result = subprocess.run(['npx', 'minify', f'src/{filename}'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
            new_html_file(filename, result, static_files, GIT_VERSION)
