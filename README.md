# pytest-selenium-demoqa
## 1. About the project
Here we are building an automation testing of website https://demoqa.com/ by using selenium and pytest.

The idea is combining the unit testing (pytest) and web automation (selenium).

Then the final report will be provided in form of html page with list test case and the status (**pass, failed, skipped,or error**).

## 2. Dependencies Required
Some python dependencies needed, check in the `requirements.txt`,  those are:
- selenium
- webdriver-manager
- python-dotenv
- openpyxl
- pandas
- pytest
- pytest-html
- softest
- ddt
- PyYAML

Install the dependencies by command:
```
pip install -r requirements.txt
```

## 3. Project Directory Structure
```
|-- README.md
|-- requirements.txt
|-- app.py
|-- assets/
    |-- [only if needed]
|-- base/
    |-- __init__.py
    |-- base_driver.py
|-- commons/
    |-- __init__.py
    |-- logger.py
    |-- take_screenshot.py
    |-- webdriver_selenium.py
|-- page_selenium_only/
    |-- __init__.py
    |-- elements.py
    |-- forms.py   [on progress]
    |-- alerts_window.py   [on progress]
    |-- widgets.py   [on progress]
    |-- interactions.py   [on progress]
    |-- book_store_app.py   [on progress]
|-- pages/
    |-- __init__.py
    |-- [on progress]
|-- reports/
    |-- screenshots/
        |-- [all screenshot files will be here]
    |-- report.html
|-- test_cases/
    |-- __init__.py
    |-- conftest.py
    |-- test_elements.py
    |-- [on progress]
|-- test_data/
    |-- test_acccount.yaml
|-- utilities/
    |-- __init__.py
    |-- chromedriver.exe
    |-- utils.py
```

requirements.txt &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; all python packages needed to run the scripts <br/>
assets/ &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; all asset files regarding specific test case <br/>
base/ &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; base driver use as the prototype inherited <br/>
reports/ &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; all kind reports as output results from running automation testing  <br/>
test_data/ &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; all account for execute data-driven testing <br/>
pages/ &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; define all locators (web element) and actions per page <br/>
test_cases/ &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; test case combining action defined in _pages/_ folder <br/>
test_cases/conftest.py &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; configuration of setup, parameters, and report format during run test case <br/>
utilities/ &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; contains all reusable commons functions or methods <br/>
page_selenium_only &nbsp;&nbsp;&nbsp;&nbsp; &#8594; &nbsp;&nbsp;&nbsp;&nbsp; automation testing if only using selenium webdriver <br/>

## 4. How to run the script
There are two ways to run the scripts:
1. Run selenium webdriver only
2. Run automation testing report using pytest supported selenium webdriver (*<u>still on progress</u>*)

### 4.1.Run selenium webdriver only
the core scripts are in directory *page_selenium_only* and executed centrally through file *app py* using this command:
```
python app.py
```

### 4.2.Run automation testing report using pytest supported selenium webdriver (*<u>still on progress</u>*)
```
pytest --browser [choose browser] --url [url retailer website] --html=[path/to/file/report.html]  --self-contained-html
```

for example:<br>
```
pytest --browser chrome --url https://demoqa.com/ --html=reports/report.html  --self-contained-html
```

After that, the script will run the test cases one by one.

The final report directory is defined from `--html=[path/to/file/report.html]`


## Learn More
Thanks to Manish Verma for the very helpful video **Selenium Python Tutorial** in **Software Testing Mentor** Youtube Channel: https://www.youtube.com/watch?v=fH4AWp9hzZM&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz
