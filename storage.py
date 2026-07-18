import os
import re

from models import Task

OBSIDIAN_TASKS_FILE_ENV = "OBSIDIAN_TASKS_FILE"
TASK_PATTERN = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s+(.*)$")


def get_obsidian_file_path():
	path = os.getenv(OBSIDIAN_TASKS_FILE_ENV, "").strip()
	if not path:
		raise RuntimeError(
			"Variable d'environnement OBSIDIAN_TASKS_FILE manquante. "
			"Exemple: OBSIDIAN_TASKS_FILE=/chemin/vers/Tasks.md"
		)

	file_path = os.path.expanduser(path)
	if not os.path.exists(file_path):
		raise FileNotFoundError(f"Fichier introuvable: {file_path}")

	return file_path


def _read_lines(file_path):
	with open(file_path, "r", encoding="utf-8") as file:
		return file.readlines()


def _write_lines(file_path, lines):
	with open(file_path, "w", encoding="utf-8") as file:
		file.writelines(lines)


def load_tasks_from_markdown(include_completed=False):
	file_path = get_obsidian_file_path()
	lines = _read_lines(file_path)

	tasks = []
	for line_index, line in enumerate(lines):
		match = TASK_PATTERN.match(line)
		if not match:
			continue

		completed = match.group(1).lower() == "x"
		if completed and not include_completed:
			continue

		tasks.append(
			Task(
				title=match.group(2).strip(),
				completed=completed,
				line_index=line_index,
			)
		)

	return tasks


def append_task_to_markdown(title):
	file_path = get_obsidian_file_path()
	lines = _read_lines(file_path)

	if lines and not lines[-1].endswith("\n"):
		lines[-1] = lines[-1] + "\n"

	lines.append(f"- [ ] {title}\n")
	_write_lines(file_path, lines)


def remove_task_by_index(task_index, include_completed=False):
	tasks = load_tasks_from_markdown(include_completed=include_completed)
	if not 0 <= task_index < len(tasks):
		return False

	file_path = get_obsidian_file_path()
	lines = _read_lines(file_path)
	lines.pop(tasks[task_index].line_index)
	_write_lines(file_path, lines)
	return True
