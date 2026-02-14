import pytest
import os
from file_counter.file_counter import count_lines

# دالة مساعدة للحصول على المسار الصحيح للملفات في مجلد testdata
def get_file_path(filename):
    return os.path.join("testdata", filename)

# 1. اختبار الملف الأساسي (المفروض يحتوي على 5 أسطر صالحة)
def test_count_lines_standard():
    path = get_file_path("file_with_5_lines.txt")
    # الدالة تعد السطور التي طولها (بعد الحذف) أكبر من 1
    assert count_lines(path) == 5

# 2. اختبار ملف فارغ 
def test_count_lines_empty():
    path = get_file_path("empty.txt")
    # يجب أن تكون النتيجة 0 لأن الملف لا يحتوي على أسطر
    assert count_lines(path) == 0

# 3. اختبار ملف يحتوي على سطر واحد فقط طوله حرف واحد 
def test_count_lines_single_char():
    path = get_file_path("one_char.txt")
    # النتيجة 0 لأن الدالة تشترط أن يكون طول السطر > 1
    assert count_lines(path) == 0

# 4. اختبار ملف كبير 
def test_count_lines_large_file():
    # هذا الاختبار يفترض وجود ملف اسمه big.txt في مجلد testdata
    path = get_file_path("big.txt")
    if os.path.exists(path):
        result = count_lines(path)
        assert result > 0
    else:
        # إذا لم يتوفر الملف الكبير، نمرر الاختبار كرسالة تنبيه
        pytest.skip("big.txt not found in testdata")

# 5. اختبار في حال كان الملف غير موجود أصلاً 
def test_file_not_found():
    path = get_file_path("non_existent_file.txt")
    with pytest.raises(FileNotFoundError):
        count_lines(path)