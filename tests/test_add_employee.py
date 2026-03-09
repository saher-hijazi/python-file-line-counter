from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from playwright.sync_api import expect

def test_add_employee(page):
    # 1. الذهاب للموقع
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # 2. إنشاء الكائنات
    login_pg = LoginPage(page)
    pim_pg = PIMPage(page)
    
    # 3. تنفيذ خطوات الاختبار
    login_pg.login("Admin", "admin123")
    pim_pg.add_employee("Saher", "Hijazi")
    
    # 4. التأكيد (الناتج النهائي)
    expect(page.get_by_text("Personal Details")).to_be_visible()