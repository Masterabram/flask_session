import requests

url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

payload = "{\n  \"BusinessShortCode\": \"174379\"," \
          "\n  \"Password\": \"MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMDkzNTUx\"," \
          "\n  \"Timestamp\": \"20180702093551\"," \
          "\n  \"TransactionType\": \"CustomerPayBillOnline\"," \
          "\n  \"Amount\": \"1\"," \
          "\n  \"PartyA\": \"254703129077\"," \
          "\n  \"PartyB\": \"174379\"," \
          "\n  \"PhoneNumber\": \"254703129077\"," \
          "\n  \"CallBackURL\": \"http://mpesa-requestbin.herokuapp.com/15kzjtu1\"," \
          "\n  \"AccountReference\": \"test\"," \
          "\n  \"TransactionDesc\": \"test\"\t\n}"

headers = {
    'Authorization': "Bearer Try6KPZSimgnmAooWEKvlPQ5hGVY",
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "6dfde7ff-8f9c-484d-b72a-f842e0b8458b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
