import pytest
import softest
from pages.element import ElementPage
from ddt import ddt, file_data, data, unpack
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestElements(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.elements = ElementPage(self.driver)
        self.ut = Utils()

    @file_data("../test_data/test_account.yml")
    def test_textbox(self, fullname, email, current_address, permanent_address):
        self.elements.text_box(fullname, email, current_address, permanent_address)

    def test_checkbox(self):
        self.elements.check_box()

    def test_radiobutton(self):
        self.elements.radio_button()