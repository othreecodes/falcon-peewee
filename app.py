from wsgiref import simple_server
from config import application as app   
import logging

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)

    logging.log(logging.DEBUG, f"App server running on {httpd.server_name}:{httpd.server_port}")
    httpd.serve_forever()