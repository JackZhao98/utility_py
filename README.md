# Python Utility
A utility package containing handy tools for python developers. Happy coding. 🍺

## apitool
```python
from utility import apitool
```
The **apitool** module contains two Class objects: `SimpleApi()` and `SimpleJson()`. They could be used to `requests.get()` content from an API url and retrieve json data in a simpler way. Function calls only. Error handling are taken care of.

### SimpleApi

Initialize with api url:

```python	
api_url = "api.test.com"
sp = apitool.SimpleApi(api_url)
```

Or call instance `set_url` any time.

```python
sp.set_url(api_url)
```

Add header field:

```python
sample_headers = {
	"user-agent":"UA", 
	"sample":"sample"}
sp.set_headers_dict(sample_headers)
sp.set_headers(key = "header_field", value = "value")
```

Set parameters in the same way:

```python
sample_params = {
	"sample":"sample"}
sp.set_params_dict(sample_headers)
sp.set_params(key = "sample_param", value = "value")
```

Finally, use `Get()` instance to call `requests.get()`,
a `dict` will be returned

```python
response = sp.Get(timeout = 6, sleep = 0.5, max_retry = 5, print_message = False)
```

Note that the `Get()` instance will call the arguments in the sample above with those default values. Change these values are optional.

### SimpleJson
Initialize the `SimpleJson` object with a `dict` type argument value:

```python
# response is a `dict`
js = apitool.SimpleJson(response)
```

Access any key value you want with `access(key)`, the corresponding value will be returned.
```python
ret = js.access("target")
```
	
### To be continued
