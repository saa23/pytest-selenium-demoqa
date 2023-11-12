import pandas as pd
from commons import *
from page_selenium_only import elements


if __name__ == '__main__':
    elements.text_box(ELEMENTS_TEXTBOX_URL)
    elements.check_box(ELEMENTS_CHECKBOX_URL)
    elements.radio_button(ELEMENTS_RADIO_URL)

