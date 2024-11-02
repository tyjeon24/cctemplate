
import toml
from pathlib import Path


toml_file = Path("../pyproject.toml")
temp_toml_file = Path("../{{cookiecutter.project_name}}/pyproject.toml")
project_name_dir = Path("../{{cookiecutter.project_name}}")


contents = """
[tool.pdm.dev-dependencies]
dev = [
    "pytest",
    "ipykernel",
    "ruff",
]

[[tool.pdm.source]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu118"
verify_ssl = true

# 120자 기준 줄바꿈
[tool.ruff]
line-length = 120

# 아래 링크 참조.
# <https://docs.astral.sh/ruff/rules/>
# ruff는 기본적으로 "F"(Flake8), "E"(pycodestyle)의 일부를 사용합니다.
# 아래처럼 추가가 가능합니다.
[tool.ruff.lint]
extend-select = [
  "RUF",  # ruff : ruff 검사기
  "I",    # isort : import 정렬 기능
  "W",    # pycodestyle
  "UP",   # pyupgrade # 포맷 변경기능
  "D",   # pydocstyle

  "NPY", # numpy 관련
  "FAST", # FastAPI 관련
  "PD", # pandas 관련
]

[tool.ruff.lint.pydocstyle]
convention = "google"
"""

with open(toml_file, "r") as f:
    project = f.read() + contents

with open(toml_file, "w") as f:
    toml.dump(project, f)

temp_toml_file.unlink(missing_ok=True)
project_name_dir.rmdir()
