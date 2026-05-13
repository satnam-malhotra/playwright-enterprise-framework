from playwright.async_api import Page

def test_login_page(page:Page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()
