import time
from datetime import datetime, timezone

def take_ss(driver, name_file):
    now_utc = datetime.now(timezone.utc).strftime("%d_%m_%Y_%H_%M_%S")
    driver.save_screenshot(f'./reports/{now_utc}-{name_file}')
    