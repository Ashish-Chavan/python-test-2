import time

from twisted.web.resource import Resource


class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return (b"" + time.ctime().encode('utf-8'))
resource = ClockPage()
