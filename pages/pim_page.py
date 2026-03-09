class PIMPage:
    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.add_emp_link = page.get_by_role("link", name="Add Employee")
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")
        self.save_btn = page.get_by_role("button", name="Save")

def add_employee(self, first, last):
        # بدلاً من الضغط فقط، انتظر حدوث التنقل
        #expect_navigation(): تخبر Playwright "انتظر حتى يكتمل تحميل الصفحة الجديدة قبل أن تنتقل للسطر التالي". هذا يحل مشكلة الـ T
        with self.page.expect_navigation():
            self.pim_menu.click()
            
        self.add_emp_link.click()
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.save_btn.click()