import unittest
from text_tetris import *

class TestTetrisMethods(unittest.TestCase):
    # Simple tests for most important functions

    def test_mix_field_and_current_piece(self):
        temp_field = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        piece = [[0,1],[0,1]]
        current_piece_object = {'piece':piece, 'x':1, 'y':1}
        expected = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(mix_field_and_current_piece(current_piece_object, temp_field), expected)

    def test_is_occupied(self):
        temp_field = [[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,1,0]]
        piece = [[0,1],[0,1]]
        current_piece_object = {'piece':piece, 'x':0, 'y':0}
        
        self.assertTrue(is_occupied(piece, 0, 0, temp_field, dx=1))
        self.assertFalse(is_occupied(piece, 0, 0, temp_field, dx=-1))

if __name__ == '__main__':
    unittest.main()
