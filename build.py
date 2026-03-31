import os
import shutil

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

CSS_PATH = os.getenv("CSS_PATH", default="css")

env = Environment(loader=FileSystemLoader("src"))
os.makedirs("./build", exist_ok=True)
shutil.copytree("src/css", "build/css", dirs_exist_ok=True)
shutil.copytree("src/base", "build", dirs_exist_ok=True)

index_template = env.get_template("index.html")
index_html = index_template.render(title="Amy", css_path=CSS_PATH)
index_soup = BeautifulSoup(index_html, "html.parser")
with open("build/index.html", "w") as f:
    f.write(str(index_soup))

deprecated_template = env.get_template("deprecated.html")
deprecated_html = deprecated_template.render(
    title="Deprecated - Amy", css_path=CSS_PATH
)
deprecated_soup = BeautifulSoup(deprecated_html, "html.parser")
with open("build/deprecated.html", "w") as f:
    f.write(str(deprecated_soup))

four04_template = env.get_template("404.html")
four04_html = four04_template.render(title="404 - Amy", css_path=CSS_PATH)
four04_soup = BeautifulSoup(four04_html, "html.parser")
with open("build/404.html", "w") as f:
    f.write(str(four04_soup))

five00_template = env.get_template("50x.html")
five00_html = five00_template.render(title="50x - Amy", css_path=CSS_PATH)
five00_soup = BeautifulSoup(five00_html, "html.parser")
with open("build/50x.html", "w") as f:
    f.write(str(five00_soup))
