# This function is built to extract date and time.
# DEFINE getDate
def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())
