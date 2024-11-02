
import toml
from pathlib import Path


toml_file = Path("../pyproject.toml")
temp_toml_file = Path("../{{cookiecutter.project_name}}/pyproject.toml")
project_name_dir = Path("../{{cookiecutter.project_name}}")

with open(toml_file, "r") as f:
    project = toml.load(f)

with open(temp_toml_file, "r") as f:
    template = toml.load(f)
    project.update(template)
    
with open(toml_file, "w") as f:
    toml.dump(project, f)

# Cleanup
temp_toml_file.unlink(missing_ok=True)
project_name_dir.rmdir()
