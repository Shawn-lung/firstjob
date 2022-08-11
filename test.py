import datetime

print((datetime.datetime.now() - datetime.timedelta(60)).date().year.__str__())