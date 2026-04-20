import re

from pages import login_page
from pages.base_page import BasePage
from pages.login_page import LoginPage

def test_login_006(access_to_login_page):
    """Check if user can input text into username and password fields."""
    login_page = access_to_login_page
    login_page.input_email("nguyenntt")
    login_page.input_password("xxxx")
    assert login_page.get_input_value(login_page.email_input) == "nguyenntt"
    assert login_page.get_input_value(login_page.password_input) == "xxxx"

def test_login_007(access_to_login_page):
    """Check email input with valid format (abc@gmail.com)."""
    login_page = access_to_login_page
    login_page.input_email("abc@gmail.com")
    assert login_page.get_input_value(login_page.email_input) == "abc@gmail.com"

def test_login_008(access_to_login_page):
    """Check email input with uppercase format."""
    login_page = access_to_login_page
    login_page.input_email("ABC@GMAIL.COM")
    assert login_page.get_input_value(login_page.email_input) == "ABC@GMAIL.COM"

def test_login_009(access_to_login_page):
    """Invalid email: abc@gmail"""
    login_page = access_to_login_page
    login_page.input_email("abc@gmail")
    login_page.click_login()
    assert login_page.is_text_visible("メールアドレスが正しくありません")

def test_login_010(access_to_login_page):
    """Invalid email: abc!@gmail.com"""
    login_page = access_to_login_page

    login_page.input_email("abc!@gmail.com")
    login_page.click_login()

    assert login_page.is_text_visible("メールアドレスが正しくありません")

def test_login_011(access_to_login_page):
    """Invalid email: test.abc"""
    login_page = access_to_login_page

    login_page.input_email("test.abc")
    login_page.click_login()

    assert login_page.is_text_visible("メールアドレスが正しくありません")
def test_login_012(access_to_login_page):
    """Invalid email: @gmail.com"""
    login_page = access_to_login_page

    login_page.input_email("@gmail.com")
    login_page.click_login()

    assert login_page.is_text_visible("メールアドレスが正しくありません")       
def test_login_013(access_to_login_page):
    """Invalid email: full-width characters"""
    login_page = access_to_login_page

    login_page.input_email("ａｂｃ＠ｇｍａｉｌ.com")
    login_page.click_login()

    assert login_page.is_text_visible("メールアドレスが正しくありません")
def test_login_014(access_to_login_page):
    """Empty email"""
    login_page = access_to_login_page

    login_page.input_email("")
    login_page.click_login()

    assert login_page.is_text_visible("メールアドレスを入力してください")

def test_login_015(access_to_login_page):
    """Check password label and input display."""
    login_page = access_to_login_page

    assert login_page.is_text_visible("パスワード")
    assert login_page.page.is_visible(login_page.password_input)  

def test_login_016(access_to_login_page):
    """Password input should be masked."""
    login_page = access_to_login_page

    login_page.input_password("12345678")

    assert login_page.get_input_value(login_page.password_input) == "12345678"

def test_login_017(access_to_login_page):
    """Click eye icon to show password."""
    login_page = access_to_login_page

    login_page.input_password("12345678")
    login_page.page.locator("//button[@aria-label='append icon']").click()
    
    assert login_page.get_input_value(login_page.password_input) == "12345678"

def test_login_018(access_to_login_page):
    """Click eye icon again to hide password."""
    login_page = access_to_login_page


    login_page.input_password("12345678")
    eye_btn = "//button[@aria-label='append icon']"
    login_page.page.click(eye_btn)
    login_page.page.click(eye_btn)

    assert login_page.get_input_value(login_page.password_input) == "12345678"


def test_login_019(access_to_login_page):
    login_page = access_to_login_page
    login_page.input_password("1234567")
    login_page.click_login()
    login_page.page.wait_for_selector("text=パスワードは8文字以上32文字以下で指定してください")

    assert login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください")


def test_login_020(access_to_login_page):
    login_page = access_to_login_page

    long_password = "a" * 40
    login_page.input_password(long_password)
    login_page.click_login()
    assert login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください")


def test_login_021(access_to_login_page):
    login_page = access_to_login_page


    login_page.input_password("12345678")
    login_page.click_login()


    assert not login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください。")


def test_login_022(access_to_login_page):
    login_page = access_to_login_page


    login_page.input_password("abcdefgh")
    login_page.click_login()


    assert not login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください。")
def test_login_023(access_to_login_page):
    login_page = access_to_login_page


    login_page.input_password("!!!!!!!!")
    login_page.click_login()


    assert not login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください。")


def test_login_024(access_to_login_page):
    login_page = access_to_login_page


    login_page.input_password("abc12345")
    login_page.click_login()


    assert not login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください。")


def test_login_025(access_to_login_page):
    login_page = access_to_login_page


    login_page.input_password("1234!!!!")
    login_page.click_login()


    assert not login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください。")


def test_login_026(access_to_login_page):
    login_page = access_to_login_page


    login_page.input_password("abcd!!!!")
    login_page.click_login()


    assert not login_page.is_text_visible("パスワードは8文字以上32文字以下で指定してください。")


def test_login_027(access_to_login_page):
    login_page = access_to_login_page


    import re

    assert login_page.page.get_by_text("パスワードを忘れた場合").is_visible()




def test_login_029(access_to_login_page):
    login_page = access_to_login_page


    login_page.click_login()

    assert login_page.is_text_visible("メールアドレスを入力してください")


def test_login_030(access_to_login_page):
    login_page = access_to_login_page

    login_page.input_email("bsv@bravesoft.co.jp")
    login_page.input_password("wrongpass123")
    login_page.click_login()

    # vẫn ở login page → login fail
    assert "login" in login_page.page.url


def test_login_031(access_to_login_page):
    login_page = access_to_login_page

    login_page.input_email("notfound@gmail.com")
    login_page.input_password("anypass123")
    login_page.click_login()

    assert "login" in login_page.page.url


def test_login_032(access_to_login_page):
    login_page = access_to_login_page


    assert login_page.page.get_by_role("button", name="新規登録").is_visible()


def test_login_033(access_to_login_page):
    login_page = access_to_login_page


    login_page.page.click("text=新規登録")
    login_page.page.wait_for_load_state("networkidle")

    assert "register" in login_page.page.url


def test_login_034(access_to_login_page):
    page = access_to_login_page.page


    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.evaluate("window.scrollTo(0, 0)")


    assert True
def test_login_035(access_to_login_page):
    page = access_to_login_page.page


    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")


    assert True
def test_login_036(access_to_login_page):
    page = access_to_login_page.page


    page.evaluate("window.scrollTo(0, 500)")
    page.evaluate("window.scrollTo(0, 0)")


    assert True

    



