# HNGi7-SMS-Task
A simple API implementing Twilio API

A Microservice that does only the following task:

**1. Send SMS**

**2. Check SMS Balance**

It's basically a layer on the default API provider by Twilio; A company that provides API to access phone numbers and make actions with them.
To send an SMS to a given number with a given message, a POST request should be made to the following endpoint containing the destination phone number in the parameter **"to"** and the given message in the parameter **"message"**.

```
http://localhost:5000/api/v1/sms/send

```

An example using the httpie client library, others like Postman, fetch, or axios could be used.

```
http -f POST http://localhost:5000/api/v1/sms/send to=+23409011221122 message="Hello World"

```

A wrong parameter would return a 403.


To check the available sms balance is also simple, simply make a GET request to the following endpoint.

```
http://localhost:5000/api/v1/sms/balance

**Example**

http http://localhost:5000/api/v1/sms/balance

```


It returns a JSON object containing the available balance and the currency.
Attempts to make a POST, DELETE, or PUT request would generate an error.


.


