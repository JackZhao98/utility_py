
"""
project: apitool 
version: 0.1

Author: Jack Zhao
Github: github.com/JackZhao98

"""


import requests
import json
import time

default_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
default_param = {}

class SimpleApi:
    """
    A convenient apitool. Pass in the API url, header field and parameter field,
    get json package in return.
    """
    def __init__(self, url = "", headers = default_headers, params = default_param):
        self.url = url
        self.headers = headers
        self.params = params
        self.response = {}

    """
    Public methods
    """
    def set_url(self, url):
        """
        Modifies API url
        """
        self.url = url


    def set_header(self, key, value):
        """
        Modifies header field.
        Usage: object.set_header(key, value)
        """
        self.__modifier(self.headers, key, value)


    def set_param(self, key, value):
        """
        Modifies parameter field.
        Usage: object.set_header(key, value)
        """
        self.__modifier(self.params, key, value)


    def set_param_dict(self, params):
        for each in params:
            self.__modifier(self.params, each, params[each])


    def Get(self, timeout = 6, sleep = 0.5, max_retry = 5,print_message = False):
        """
        Easy requests.get() method.
        call requests.get() with preset headers field, param.
        will automatically retry if timeout.
        """
        try:
            response = requests.get(url=self.url, params = self.params, headers = self.headers, timeout = timeout)
        except:
            if print_message: 
                print("API request timeout, retry.")
            for i in range(1, max_retry):
                try:
                    if print_message: 
                        print(f"...Retry No.{i}")
                    response = requests.get(
                        url=self.url, params = self.params, 
                        headers = self.headers, timeout = 5)
                    if print_message: 
                        print(f"...Retry No.{i}: SUCCESS")
                    break
                except:
                    if print_message: 
                        print(f"...Retry No.{i}: FAILED")
                    if i == (max_retry - 1):
                        print("...API requests failed")
                        exit(1)
                    else:
                        continue

        time.sleep(sleep)

        if response.status_code != 200:
            print(f"ERROR: {response.status_code}, exit")
            exit(1)

        self.response = response.json()

        return self.response


    """
    Private methods
    """
    def __modifier(self, field, key, value):
        try:
            field[key] = value
        except:
            print("Modify error: \"{}:{}\"".format(key, value))
            exit(1)

    """
    End of private  methods
    """
                
    """
    DEBUG
    """

    def display_request_info(self):
        print(f"API URL: {self.url}")
        print("\nHeader field:")
        print("\n".join(f"...{k}:\n......{self.headers[k]}" for k in self.headers))
        print("\nParameter field:")
        print("\n".join(f"...{k}:\n......{self.params[k]}" for k in self.params))


    def display_response(self):
        if self.response is '':
            print("no response")
        else:
            print("Response: ")
            print(json.dumps(self.response, indent=2, ensure_ascii=False))



class SimpleJson:
    """
    SimpleJ SON Dictionary parser for lazy people.
    
    """
    def __init__(self, json_data = {}):
        self.json_data = json_data


    def access(self, target, data = None):
        """
        Automatically returns the data for given target key.
        *note: Return the first matched target key value only.
        """
        if not data:
            data = self.json_data
        for v in data:
            if v == target:
                return data[v]
            if type(data[v]) == dict:
                return self.access(target, data[v])

            if type(data[v]) == list:
                if len(data[v]) > 0 and type(data[v][0]) == dict:
                    for l in range(0, len(data[v])):
                        return self.access(target, data[v][l])
        return None





