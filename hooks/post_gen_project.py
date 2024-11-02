
import toml
from pathlib import Path


toml_file = Path("../pyproject.toml")
temp_toml_file = Path("{{cookiecutter.project_name}}/pyproject.toml")
project_name_dir = Path("{{cookiecutter.project_name}}")

with open(toml_file, "r") as f:
    project = toml.load(f)

if "dependencies" not in project.get("project", {}):
    project.setdefault("project", {})["dependencies"] = []

dependencies = project["project"]["dependencies"]
if not any(dep.startswith("pandas") for dep in dependencies):
    dependencies.append("pandas")

with open(toml_file, "w") as f:
    toml.dump(project, f)
    
temp_toml_file.unlink()
project_name_dir.rmdir()
