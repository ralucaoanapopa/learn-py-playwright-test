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

3. Install the [pytest playwright plugin](https://pypi.org/project/pytest-playwright/)

```
pip install pytest-playwright
```

4. Install the required browsers (chromium, firefox, webkit)

```
playwright install
```

# [Run tests](https://playwright.dev/python/docs/running-tests)

### Pre-requisites

Credentials used in tests need to be set as [environment variables](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set_1).

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

# Results


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