# README

This guide provides a brief overview of how to use Python for networking tasks.

## Fetching Internet Resources with urllib

The `urllib` package in Python is used to fetch resources (or data) from the Internet. Here's a basic example:

```python
from urllib import request

url = "http://example.com"
response = request.urlopen(url)
data = response.read()
```

## Decoding urllib Body Response

The data read from a urllib response is in bytes. To convert it into a string, you can decode it:

```python
data_decoded = data.decode('utf-8')
```

## Using the Python Package requests

The `requests` package is a simple and more user-friendly alternative to urllib for making HTTP requests:

```python
import requests

response = requests.get("http://example.com")
```

## Making HTTP GET Request

A GET request can be made using both urllib and requests:

```python
# Using urllib
from urllib import request
response = request.urlopen("http://example.com")

# Using requests
import requests
response = requests.get("http://example.com")
```

## Making HTTP POST/PUT/etc. Request

Other types of HTTP requests can also be made with requests:

```python
# POST request
response = requests.post("http://example.com/post", data={'key':'value'})

# PUT request
response = requests.put("http://example.com/put", data={'key':'value'})
```

## Fetching JSON Resources

JSON data can be fetched and parsed into a Python dictionary using the `json` method of a response object:

```python
response = requests.get("http://example.com/json")
data = response.json()
```

## Manipulating Data from an External Service

Once data is fetched from an external service, it can be manipulated like any other data in Python:

```python
data = requests.get("http://example.com/json").json()
for item in data['items']:
    print(item['name'])
```