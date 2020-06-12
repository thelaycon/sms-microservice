"""import pytest
import requests


def test_sendsms():
    #Use localhost:5000

    response = requests.post("http://localhost:5000/api/v1/sms/send", json={"message":"Hey bro", "to":"+2349053001561"})
    assert response.status_code == 200

def test_checkbalance():

    #Use localhost:5000

    response = requests.get("http://localhost:5000/api/v1/sms/balance")
    assert response.status_code == 200



def test_getrecords():

    #Use localhost:5000

    response = requests.get("http://localhost:5000/api/v1/sms/records")
    assert response.status_code == 200



"""

#Commented
