from SmartApi.smartWebSocketV2 import SmartWebSocketV2
import ast
# from marketdata.views import connect, subscription

class WSData(object):
    def __init__(self):
        self.data = ''
        self.sws = ''
    def startWS(self, connect, subscription):
        connect = ast.literal_eval(connect)
        subscription = ast.literal_eval(subscription)
        self.sws = SmartWebSocketV2(connect["AUTH_TOKEN"], connect["API_KEY"], connect["CLIENT_CODE"], connect["FEED_TOKEN"])

        def on_data(wsapp, message):
            if message != b'\x00':
                try:
                    # data = str(message).replace("'", '"')
                    # subprocess.Popen(['python3', 'manage.py', 'collectstatic', '--no-input'])
                    self.data = str(message).replace("'", '"')
                except Exception as e:
                    print(e)
            # print(message)
            # close_connection()

        def on_open(wsapp):
            # logger.info("on open")
            self.sws.subscribe(subscription["correlation_id"], subscription["mode"], subscription["token_list"])
            # sws.unsubscribe(correlation_id, mode, token_list1)


        def on_error(wsapp, message):
            # logger.error(error)
            print(message)

        def on_close(wsapp):
            # logger.info("Close")
            # stream.close()
            pass

        def close_connection():
            self.sws.close_connection()

        # Assign the callbacks.
        self.sws.on_open = on_open
        self.sws.on_data = on_data
        self.sws.on_error = on_error
        self.sws.on_close = on_close

        self.sws.connect()

    def getData(self):
        return self.data