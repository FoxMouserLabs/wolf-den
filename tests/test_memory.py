import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

import memory

class TestMemory(unittest.TestCase):

	def setUp(self):
		self.temp_dir = tempfile.TemporaryDirectory()
		self.test_file = (
			Path(self.temp_dir.name) / "test_memory.json"
		)

		self.patcher = patch.object(
			memory, "MEMORY_FILE", str(self.test_file)
		)
		self.patcher.start()

	def tearDown(self):
		self.patcher.stop()
		self.temp_dir.cleanup()

	def test_save_and_load(self):
		data = {"name": "test Wolf"}

		memory.save_memory(data)

		self.assertEqual(
			memory.load_memory(), data

		)

	def test_missing_file(self):
		self.assertEqual(memory.load_memory(), {})

	def test_update_memory(self):
		memory.save_memory({"game": "Terraria"})

		data = memory.load_memory()
		data["game"] = "Stardew Valley"
		memory.save_memory(data)

		self.assertEqual(
			memory.load_memory()["game"],
			"Stardew Valley"
		)

	def test_corrupted_json(self):
		self.test_file.write_text(
			'{"name": "Broken"',
			encoding="utf-8"
		)

		with self.assertRaises(ValueError):
			memory.load_memory()

		self.assertEqual(
			self.test_file.read_text(encoding="utf-8"),
			'{"name": "Broken"'
		)


if __name__ == "__main__":
	unittest.main()
