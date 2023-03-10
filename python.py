websites = [
    "naver.com",
    "app.modeal.net",
    "https://auto-sales.co.kr",
    "crm.modeal.net"

]

for website in websites:
    if not website.startswith(("https://")):
        website = f"https://{website}"
    print(website)