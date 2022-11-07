import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
from library.config import Config


@pytest.fixture(params=["Chrome"])
def init_driver(request):

    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Config.chrome_path)

    # else:
    #     firefox_path = r"C:\Users\Admin\PycharmProjects\pythonProject\HTD_project\drivers\geckodriver.exe"
    #     driver = webdriver.Firefox(executable_path=Config.firefox_path)

        driver.get(Config.URL)
        driver.maximize_window()
        driver.implicitly_wait(20)
        yield driver
        driver.close()