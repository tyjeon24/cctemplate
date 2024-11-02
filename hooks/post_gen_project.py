import toml

toml_file = "../pyproject.toml"

with open(toml_file, "r") as f:
    project = toml.load(f)

if "dependencies" not in project.get("project", {}):
    project.setdefault("project", {})["dependencies"] = []

dependencies = project["project"]["dependencies"]
if not any(dep.startswith("pandas") for dep in dependencies):
    dependencies.append("pandas")

with open(toml_file, "w") as f:
    toml.dump(project, f)