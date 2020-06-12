import requests
import connexion
from twilio.rest import Client
import sqlite3
import os
from datetime import datetime
from flask import Response
from connexion.exceptions import OAuthProblem


#Get current date
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))



#Avoid putting your credentials here, use environment instead!!

ACCOUNT_SID =  os.environ.get("ACCOUNT_SID")
AUTH_TOKEN =  os.environ.get("AUTH_TOKEN")
SENDER = os.environ.get("SENDER")
 

client = Client(ACCOUNT_SID, AUTH_TOKEN)
balanceEndPointURI = f"https://api.twilio.com/2010-04-01/Accounts/{ACCOUNT_SID}/Balance.json"


#Authentication middlewares

def authenticate(apiKey, required_scopes):
    if apiKey != AUTH_TOKEN:
        raise OAuthProblem("Invalid Token")
    else:
        return {"apiKey":apiKey}

def validateAccountSid(account_sid):
    if account_sid != ACCOUNT_SID:
        raise OAuthProblem("Invalid Account Sid")





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

#Retrieve records function

def retrieve():
    account_sid = connexion.request.headers["Account-Sid"]

    #Validate Account Sid

    validateAccountSid(account_sid)

    #Initialize DB
    conn = sqlite3.connect("sms_db.db")
    cursor = conn.cursor()
    sql_statement = "SELECT * FROM sms_record;"
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    conn.close()
    return records


#Check Balance function 

def checkBalance():
    try:
        account_sid = connexion.request.headers["Account-Sid"]
        #Validate Account Sid

        validateAccountSid(account_sid)

        #Get balance

        response = requests.get(balanceEndPointURI, auth = (ACCOUNT_SID, AUTH_TOKEN))
        data = response.json()
        try:
            del data["account_sid"]
            return data
        except KeyError:
            raise KeyError
    except KeyError:
        return Response("Unable to check balance, check credentials", status=403)



#Send SMS function

def sendSms(**kwargs):

    #get details
    try:
        body = kwargs['body']
        to = body['to']
        message = body['message']
        account_sid = connexion.request.headers["Account-Sid"]

        #Validate Account Sid
        
        validateAccountSid(account_sid)


        #Send SMS

        sms = client.messages.create(
                    to = to,
                    from_ = SENDER,
                    body = message
                    )

        #Record SMS to DB


        if sms.sid:
            record(to, message)
            return f"Message sent successfully to {to} with message id {sms.sid}"
    except KeyError:
        return Response("Invalid credentials", status=403)


#JSON Documentations handler

def docs():
    data = requests.get("http://localhost:5000/v1/openapi.json").json()
    return data

#Configure Company ID handler


def configure(**kwargs):
    try:
        body = kwargs["body"]
        company_id = body["company_id"]

        #Validate Account SID
        try:
            account_sid = connexion.request.headers["Account-Sid"]
            

            validateAccountSid(account_sid)
        except KeyError:
            return Response("Invalid Acount Sid")

    except KeyError:
        return Response("Invalid Company ID")

    conn = sqlite3.connect("sms_db.db")
    cursor = conn.cursor()
    sql_statement = f"SELECT * FROM company_record WHERE CompanyID = '{company_id}';"
    cursor.execute(sql_statement)
    data = cursor.fetchall()

    if data == []:
        sql_statement = f"INSERT INTO company_record VALUES('{company_id}');"
        cursor.execute(sql_statement)
    else:
        sql_statement = f"UPDATE company_record SET CompanyID = '{company_id}';"
        cursor.execute(sql_statement)

    conn.commit()
    conn.close()


