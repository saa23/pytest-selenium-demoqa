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

## 3. How to run the script?
pytest --browser [choose browser] --url [url retailer website] --html=[path/to/file/report.html]

for example:<br>
pytest --browser chrome --url https://demoqa.com/ --html=reports/report.html

After that, the script will run the test cases one by one.

The final report directory is defined from `--html=[path/to/file/report.html]


## Learn More
Thanks to Manish Verma for the very helpful video **Selenium Python Tutorial** in **Software Testing Mentor** Youtube Channel: https://www.youtube.com/watch?v=fH4AWp9hzZM&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz
