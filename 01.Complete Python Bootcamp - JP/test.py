import unittest
import Cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = Cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multiplewords(self):
		text = 'monty python'
		result = Cap.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
	unittest.main()