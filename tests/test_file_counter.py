import pytest
from file_counter.file_counter import count_lines

def test_count_lines_correct():
    
    result = count_lines("testdata/file_with_5_lines.txt")
    assert result == 5