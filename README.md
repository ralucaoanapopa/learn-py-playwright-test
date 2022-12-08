# Setup

1. Download and install [Python 3.x](https://www.python.org/downloads/windows/)
- If it is already installed, check in terminal:

```
> python --version
```

2. Make sure to have the [latest pip version](https://pip.pypa.io/en/stable/installation/) installed

```
> python.exe -m pip install --upgrade pip
```

3. Install the [pytest playwright plugin](https://pypi.org/project/pytest-playwright/)

```
> pip install pytest-playwright
```

4. Install the required browsers (chromium, firefox, webkit)

```
> playwright install
```

# Run tests

By default tests will be run on chromium, in headless mode:

```
> pytest
```

Using pytest [CLI options](https://playwright.dev/python/docs/test-runners#cli-arguments) can choose another browser and headed mode:

```
> pytest --browser webkit --headed
```

# Results


# Resources

## Tools & frameworks
- [Playwright](https://playwright.dev/python/docs/intro)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Playwright Pytest plugin](https://playwright.dev/python/docs/test-runners)


## Free websites for UI testing
- [DemoQA](https://demoqa.com/)
- [Sauce Demo](https://www.saucedemo.com/)
- [UI elements on herokuapp](https://the-internet.herokuapp.com/)
- [Test pages for automating](https://testpages.herokuapp.com/styled/index.html)