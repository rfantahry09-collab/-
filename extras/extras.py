# PLUGINS
def plugin_example():
    return "Hello from plugin_example!"

def ai_enhancer():
    return "AI enhancement active!"

PLUGINS = {
    "plugin_example": plugin_example,
    "ai_enhancer": ai_enhancer
}

# TESTS
def test_wallet():
    assert True

def test_pay():
    assert True

def test_ai():
    assert True

TESTS = {
    "test_wallet": test_wallet,
    "test_pay": test_pay,
    "test_ai": test_ai
}

# DOCS
USAGE_GUIDE = """
Taherion Super App Usage Guide
/auth/register → ثبت نام کاربر
/auth/login → ورود
/wallet/add → افزودن موجودی
/wallet/pay → پرداخت قبض
/chat/send → ارسال پیام
/chat/inbox → مشاهده پیام‌ها
/ai → سوال به AI
"""

# ASSETS
ASSETS = {
    "logo": "logo.png",
    "banner": "banner.jpg"
}

# BASIC AI
def basic_ai(question: str):
    return f"AI Response: {question}"
