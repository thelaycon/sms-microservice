# HNGi7-SMS-Task
A simple microservice implementing Twilio API

It's a simple microservice that does just three tasks..


**1. Send SMS**


**2. Check balance**


**3. Check records of sent SMS.**



To use the UI, [Click here](https://sms-microservice.herokuapp.com/api/v1/sms/ui/)


To check balance, one should send a **GET** request to the endpoint:

```
https://sms-microservice.herokuapp.com/api/v1/sms/balance

```

To Send SMS, one should make a POST request to the following endpoint with a JSON object containing two parameters **message** and **to** which signifies the "SMS body" and recipient phone number respectively.


```

https://sms-microservice.herokuapp.com/api/v1/sms/send

```

An example of a simple request using **curl** client. Fetch, Axios, Postman can be used, any client would work as long as you send a valid JSON object.


```

curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
   "message": "Hey bro",
   "to": "+2349053001561"
 }' 'https://sms-microservice.herokuapp.com/api/v1/sms/send'

```


It should return a 201 if successful.

To get record of all SMS sent, one should make a **GET** request to the following endpoint.


```

https://sms-microservice.herokuapp.com/api/v1/sms/records

```

This returns a JSON of SMS sent and their respective dates...



**DEPLOYMENT:**

Make sure you get an authorization token from http://twilio.com, an account Sid and a phone number.
Set the environment variables first.


```

export ACCOUNT_SID=XXXXXXXXXXXXXXXXXXX
export AUTH_TOKEN=XXXXXXXXXXXXXXXXXXXXX
export SENDER=+XXXXXXXXXXXXXXXXXXX

```


