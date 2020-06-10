import os
import requests
from twilio.rest import Client
import sqlite3
from datetime import datetime

#Get current date
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))



#Avoid putting your credentials here, use environment instead!!

account_sid = os.environ.get("ACCOUNT_SID")
#Auth Token expires, get an active one 

auth_token = os.environ.get("AUTH_TOKEN")

sender = os.environ.get("SENDER")

client = Client(account_sid, auth_token)
balanceEndPointURI = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Balance.json"


#Record sent SMS in database

def record(to, message):
    #Initialize DB
    conn = sqlite3.connect("sms_db.db")
    cursor = conn.cursor()
    date = get_timestamp()
    sql_statement = f"INSERT INTO sms_record VALUES('{to}','{message}','{date}');"
    cursor.execute(sql_statement)
    conn.commit()
    conn.close()

def retrieve():
    #Initialize DB
    conn = sqlite3.connect("sms_db.db")
    cursor = conn.cursor()
    sql_statement = "SELECT * FROM sms_record;"
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    conn.close()
    return records




#Task 1 *Check sms balance 

def checkBalance():
    response = requests.get(balanceEndPointURI, auth = (account_sid, auth_token))
    data = response.json()
    try:
        del data["account_sid"]
        return data
    except KeyError:
        return "Unable to check balance, check credentials"



#Task 2 *Send sms

def sendSms(details):
    #get details
    try:
        to = details.get("to", None)
        message = details.get("message", None)
        sms = client.messages.create(
            to = to,
                from_ = sender,
                body = message
                )
        if sms.sid:
            record(to, message)
            return f"Message sent successfully to {to} with message id {sms.sid}"
    except KeyError:
        return Response("Invalid credentials", status=403)


