# HNGi7-SMS-Task
A simple microservice implementing Twilio API

It's a simple microservice that does just three tasks..


**1. Send SMS**


**2. Check balance**


**3. Check records of sent SMS.**



**DEPLOYMENT:**

Make sure you get an authorization token from http://twilio.com, an account Sid and a phone number.
Set the environment variables first.


```

export ACCOUNT_SID=XXXXXXXXXXXXXXXXXXX
export AUTH_TOKEN=XXXXXXXXXXXXXXXXXXXXX
export SENDER=+XXXXXXXXXXXXXXXXXXX

```

**Note:** All requests to the endpoints should include the Account Sid as **Account-Sid** and authentication token as **Auth-Token** in the headers for authentication.

For access to Swagger UI and Docs, visit

```

http://localhost:5000/

```


To check balance, one should send a **GET** request to the endpoint:

```
https://localhost:5000/v1/balance

```

To Send SMS, one should make a POST request to the following endpoint with a JSON object containing two parameters **message** and **to** which signifies the "SMS body" and recipient phone number respectively.


```

https://localhost:5000/v1/send

```

An example of a simple request using **curl** client. Fetch, Axios, Postman can be used, any client would work as long as you send a valid JSON object.


```

curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'Account-Sid: xxxxxxxxxxxxxxxxx' --header 'Auth-Token: xxxxxxxxxxxxxxxx' -d '{
   "message": "Hey bro",
   "to": "+2349053001561"
 }' 'https://localhost:5000/v1/send'

```


It should return a 201 if successful.

To get record of all SMS sent, one should make a **GET** request to the following endpoint.


```

https://localhost:5000/v1/records

```

This returns a JSON of SMS sent and their respective dates...


To configure the API with the Company ID, a **POST** request should be sent to the endpoint:

```
http://localhost:5000/v1/configure

```
with a JSON object in this format:

```
{
	'company_id': 'HNGi7'
}
```

To get the documentation in JSON, a **GET** request to:

```
http://localhost:5000/v1/documentation
```

However, this does not require authencation.



