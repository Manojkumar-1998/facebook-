import datetime
import pytest
from library.config import Config
from library.exel_lib import ReadExcel
from POM.facebook_profile import Facebookprofile


class Testfacebookprofile:
    read_xl = ReadExcel()
    data = read_xl.read_testdata()

    def test_datas(self):
        print(self.data)

    @pytest.mark.parametrize('username,pwd,status,note,home', data)
    def test_registration(self, init_driver, username, pwd, status, note, home):
        driver = init_driver
        try:

            fb = Facebookprofile(driver)
            fb.user_name(username)
            fb.pass_word(pwd)
            fb.login()
            fb.profile_icon()
            fb.Add_to_Story()
            fb.create_text_story()
            fb.start_typing(status)
            fb.discard()
            fb.confirm_discard()
            fb.back_button()
            fb.edit_profile()
            fb.add_bio()
            fb.discribe(note)
            fb.save()
            fb.back_to_profile()
            fb.about()
            fb.contact_and_basic()
            fb.address()
            fb.add_address(home)
            fb.save_address()

        except AssertionError as msg:
            td = datetime.datetime.now()
            name = f'screenshot_{td.hour}{td.minute}{td.second}.png'
            driver.save_screenshot(Config.SCREENSHOT_PATH + name)
            raise msg
