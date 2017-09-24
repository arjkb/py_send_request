# py_send_reqeust

Python script to send HTTP requests to urls.

### USAGE
For command line instructions:
```
python send_request -h
```

The program takes two arguments:
* First argument is the number of times HTTP GET requests must be sent to the server.
* Second argument is the file containing the urls to which the requests are to be sent.

For example, if 100 requests each must be sent to urls in the file `url_list.txt`, use the command:
```
python send_request 100 url_list.txt
```


#### Output
Spits out 4 numbers that may be of interest:

1. blocked <br/> Number of times `requests.exceptions.ConnectionError` was raised
2. worked<br/>Number of times an HTTP 200 was received from the server.
3. weird_1 <br /> The request succeeded, but the reply was something other than HTTP 200.
4. weird_2 <br /> An exception other than `requests.exceptions.ConnectionError` was raised.

The URL is also printed along with the corresponding information.

---
### Collaborators

1. [Ashraf Siddiquee](https://github.com/mashrafsiddiquee)
2. Humayra Tasnim, University of New Mexico
