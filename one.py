import json
import urllib3

http = urllib3.PoolManager()
data = {"text": "Test from local"}

response = http.request(
    "POST",
    "https://hooks.slack.com/services/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",
    body=json.dumps(data),
    headers={"Content-Type": "application/json"}
)

print("Status:", response.status)
print("Response:", response.data.decode("utf-8"))
