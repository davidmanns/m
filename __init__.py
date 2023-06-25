from py4web import action, URL, redirect

@action("index")
def index():
    redirect(URL("oxcam", scheme=True).replace('/m/', '/'))

@action("about")
def index():
    redirect(URL("oxcam", "about", scheme=True).replace('/m/', '/'))

@action("history")
def index():
    redirect(URL("oxcam", "history", scheme=True).replace('/m/', '/'))

@action("directory")
def index():
    redirect(URL("oxcam", "directory", scheme=True).replace('/m/', '/'))

@action("mail_list")
def index():
    redirect(URL("oxcam", "registration", vars=dict(mail_lists='Y'), scheme=True).replace('/m/', '/'))
