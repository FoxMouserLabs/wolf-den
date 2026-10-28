import json
import os
import tempfile
from pathlib import Path

MEMORY_FILE = "memory.json"


def save_memory(memory):
	destination = Path(MEMORY_FILE)
	temp_path = None

	try:
		with tempfile.NamedTemporaryFile(
			mode="w",
			encoding="utf-8",
			dir=destination.parent,
			prefix=".wolf_",
			suffix=".tmp",
			delete=False
		) as file:
			temp_path = file.name
			json.dump(memory, file, indent=4)
			file.flush()
			os.fsync(file.fileno())

		os.replace(temp_path, destination)

	finally:
		if temp_path and os.path.exists(temp_path):
			os.unlink(temp_path)


def load_memory():
	try:
		with open(MEMORY_FILE, "r") as file:
			data = json.load(file)

		if not isinstance(data, dict):
			raise ValueError(
				"Memory file must contain a dictonary."

			)

		return data

	except FileNotFoundError:
		return {}

	except (json.JSONDecodeError, ValueError) as error:
		raise ValueError(
			f"Memory file is invalid: {error}"
		) from error
