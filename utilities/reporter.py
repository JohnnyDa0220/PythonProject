import pytest
import allure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            try:
                png = driver.get_screenshot_as_png()
                allure.attach(png, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Could not capture screenshot: {e}")