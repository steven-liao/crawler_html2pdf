from weibo import Client
API_KEY="2127684306"
API_SECRET="0182d6ed546035479f41e28a4bb69973"
REDIRECT_URI="127.0.0.1"
c = Client(API_KEY, API_SECRET, REDIRECT_URI)
print c.authorize_url