from memory import save_memory, load_memory
def respond(message):
	message = message.strip()
	command = message.lower()

	if command.startswith("remember "):
		fact = message[9:]

		if "=" not in fact:
			return "Try: remember favorite food = Sushi"

		key, value = fact.split("=", 1)
		key = key.strip().lower().replace(" ", "_")
		value = value.strip()

		if not key or not value:
			return "I need both a memory name and a value."

		memory = load_memory()
		memory[key] = value
		save_memory(memory)

		return f"Got it! I'll remember {key}."

	elif command.startswith("recall "):
		key = command[7:].strip().replace(" ", "_")
		memory = load_memory()

		if key in memory:
			return memory[key]
		else:
			return "I dont remember that yet."

	elif command.startswith("forget "):
		key = command[7:].strip().replace(" ","_")
		memory = load_memory()

		if key in memory:
			del memory[key]
			save_memory(memory)
			return f"Okay. I've forgotten {key}."

		else:
			return "I don't remmeber that."

	elif command.startswith("update "):
		fact = message[7:]

		if "=" not in fact:
			return "Try: update favorite game = Stardew Valley"

		key, value = fact.split("=", 1)
		key = key.strip().lower().replace(" ","_")
		value = value.strip()

		if not key or not value:
			return "I need both a memory name and a value"

		memory = load_memory()

		if key in memory:
			memory[key] = value
			save_memory(memory)
			return f"Updated {key}!"

		else:
			return f"I don't have a memory called {key}."

	elif command == "memories":
		memory = load_memory()

		if not memory:
			return "My brain is empty. Rude."

		response = "Here's what i remember:\n"

		for key, value in memory.items():
			response += f"-{key}: {value}\n"

		return response


	elif command.startswith("my name is "):
		name = message[len("my name is "):].strip()

		if not name:
			return "You forgot to tell me your name!"

		memory = load_memory()
		memory["name"] = name
		save_memory(memory)

		return f"I'll remember that, {name}."

	elif command == "who am i":
		memory = load_memory()
		name = memory.get("name")

		if name:
			return f"You're {name}!"

		else:
			return "I dont know your name yet."

	elif command == "hello":
		return "Oh. You're here. Hi!:"

	elif command == "status":
		return "All systems operational. Tail functioning."

	elif command == "sleep":
		return "Fine. Five more minutes..."

	elif command == "name":
		return "Wolf."

	else:
		return "I don't know  how to answer that yet."


def main():
	print(" Wolf v0.3.2 - Memory Management")
	print("Type 'exit' to close the program. \n")

	while True:
		message = input("You:  ")

		if message.lower().strip() == "exit":
			print("Wolf: Going back to my crate.")
			break

		reply = respond(message)
		print(f"Wolf: {reply}")


if __name__ == "__main__":
	main()
