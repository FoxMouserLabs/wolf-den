def save_name(name):
	with open("memory.txt", "w") as file:
		file.write(name)

def load_name():
	try:
		with open("memory.txt", "r") as file:
			return file.read().strip()


	except FileNotFoundError:
		return None



def respond(message):
	message = message.strip()
	command = message.lower()

	if command.startswith("my name is "):
		name = message[len("my name is "):]
		save_name(name)
		return f"I'll remember that, {name}."

	elif command == "who am i":
			name = load_name()

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
	print(" Wolf v0.2 - Remember Me")
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
