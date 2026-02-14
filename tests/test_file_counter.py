from file_counter.file_counter import count_lines

def test_count_lines_returns_int():
    # نتأكد أن الدالة ترجع رقم صحيح
    result = count_lines("testdata/file_with_5_lines.txt")
    assert isinstance(result, int)

def test_count_lines_correct_value():
    # نتأكد أن الدالة تحسب الأسطر بشكل صحيح
    result = count_lines("testdata/file_with_5_lines.txt")
    assert result == 5
