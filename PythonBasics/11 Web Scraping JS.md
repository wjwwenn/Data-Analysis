# Web Scraping on Javascript-Driven HTML

## To get the HTML for the whole page:
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://stackoverflow.com")
html = driver.page_source

```

### To get the outer HTML (tag included):

**HTML from `<html>`**
```python
html = driver.execute_script("return document.documentElement.outerHTML;")
```

**HTML from `<body>`**
```python
html = driver.execute_script("return document.body.outerHTML;")
```

**HTML from element with some JavaScript**
```python
element = driver.find_element_by_css_selector("#hireme")
html = driver.execute_script("return arguments[0].outerHTML;", element)
```

**HTML from element with `get_attribute`**
```python
element = driver.find_element_by_css_selector("#hireme")
html = element.get_attribute('outerHTML')
```

### To get the inner HTML (tag included):

**HTML from `<html>`**
```python
html = driver.execute_script("return document.documentElement.innerHTML;")
```

**HTML from `<body>`**
```python
html = driver.execute_script("return document.body.innerHTML;")
```

**HTML from element with some JavaScript**
```python
element = driver.find_element_by_css_selector("#hireme")
html = driver.execute_script("return arguments[0].innerHTML;", element)
```

**HTML from element with `get_attribute`**
```python
element = driver.find_element_by_css_selector("#hireme")
html = element.get_attribute('innerHTML')
```