#!/usr/bin/python
from argparse import ArgumentParser

from app import routes

routes.app.config.from_pyfile('../config.cfg')

class WEBserver:
    @staticmethod
    def run(args):
        port = args.port
        routes.app.run(host='0.0.0.0', port=port)
    
    
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000,type=int, help='port to listen on,default 5000')
    parser.add_argument('-v', '--version', action='version',
                        version='Simple BlockChain DataBase Web server 1.0')
    args = parser.parse_args()
    WEBserver.run(args)
