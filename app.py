from wsgiref import simple_server
from config import application as app   
import logging


logging.basicConfig(
    level = logging.INFO,
    format = '[%(asctime)s] - [%(levelname)s] - %(message)s'
)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)

    logging.info(f"App server running on {httpd.server_name}:{httpd.server_port}")
    httpd.serve_forever()