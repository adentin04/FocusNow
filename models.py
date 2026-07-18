from dataclasses import dataclass


@dataclass
class Task:
	title: str
	completed: bool
	line_index: int
