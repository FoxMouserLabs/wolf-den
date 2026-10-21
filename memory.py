import json

MEMORY_FILE = "memory.json"


def save_memory(memory):
	with open(MEMORY_FILE, "w") as file:
		json.dump(memory, file, indent=4)


def load_memory():
	try:
		with open(MEMORY_FILE, "r") as file:
			return json.load(file)

	except FileNotFoundError:
		return {}
