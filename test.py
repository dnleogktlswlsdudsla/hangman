__author__ = 'user'
import unittest
import hangman
class testCase(unittest.TestCase):
	def test_checkCorrectAnswer(self):
		corretLetters="cta"
		secretWord="cat"
		ret=hangman.checkCorrectAnswer(corretLetters,secretWord)
		self.assertTrue(ret)
	def test_checkWrongAnswer(self):
		corretLetters="tcryui"
		sectertWord="cat"
		ret=hangman.checkWrongAnswer(corretLetters,sectertWord)
		self.assertTrue(ret)
if __name__=="__main__":
unittest.main()
