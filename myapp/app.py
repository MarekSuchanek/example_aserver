import argparse

from aiohttp import web

parser = argparse.ArgumentParser(description="aiohttp server example")
parser.add_argument('--path')
parser.add_argument('--port', type=int)


def index(request):
    return web.Response(text="Welcome home!")


def start():
    app = web.Application()
    app.router.add_get('/', index)

    args = parser.parse_args()
    web.run_app(app, path=args.path, port=args.port)
