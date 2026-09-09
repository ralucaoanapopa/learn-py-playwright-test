# Setup

1. Download and install [Python 3.x](https://www.python.org/downloads/windows/)
- If it is already installed, check in terminal:

```
python --version
```

2. Make sure to have the [latest pip version](https://pip.pypa.io/en/stable/installation/) installed

```
python.exe -m pip install --upgrade pip
```

3. Create a virtual environment (use gitbash terminal)

```
python.exe -m venv .venv
source .venv/Scripts/activate
```

4. Install all dependencies
- the [pytest playwright plugin](https://pypi.org/project/pytest-playwright/)

```
pip install -r requirements.txt
```

5. Install the required web drivers (chromium, firefox, webkit)

```
playwright install
```

# [Run tests](https://playwright.dev/python/docs/running-tests)

### Pre-requisites

Credentials used in tests need to be set as [environment variables](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set_1).

Easy setup for secrets using shell file which can be executed in git bash in order to set environment variables.
Create a `credentials.sh` with:
```
export USERNAME_QA=<add_username>
export PASSWORD_QA=<add_pwd>
export USER_SAUCE=<add_user>
export PASSWORD_SAUCE=<add_pwd>
```
Execute in git bash
```
source ./credentials.sh
```

In order to see the list of tests:
```
pytest --collect-only
```

By default tests will be run on chromium, in headless mode:

```
pytest
```

Using pytest [CLI options](https://playwright.dev/python/docs/test-runners#cli-arguments) can choose another browser and headed mode:

```
pytest --browser webkit --headed
```

Run only one test suite

```
pytest <test_file>.py --headed
```

Run all tests from root
```
python -m pytest
```

Run tests for one website
```
pytest POM_saucedemo/* --headed
```

# Results

## All tests
![POM demoqa tests](/results/pom_demoqa.png "POM demoqa tests")
![POM sauce demo tests](/results/pom_saucedemo.png "POM sauce demo tests")
![Basic tests](/results/basic_tests.png)

# Resources

## Tools & frameworks
- [Playwright](https://playwright.dev/python/docs/intro)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Playwright Pytest plugin](https://playwright.dev/python/docs/test-runners)


## Free websites for UI testing
- [DemoQA](https://demoqa.com/)
- [Letcode](https://letcode.in/)
- [Sauce Demo](https://www.saucedemo.com/)
- [UI elements on herokuapp](https://the-internet.herokuapp.com/)
- [Test pages for automating](https://testpages.herokuapp.com/styled/index.html)