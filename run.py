import click

from app import app


@click.command()
@click.option('--debug', is_flag=True)
@click.option('--threaded', is_flag=True)
@click.argument('HOST', default='0.0.0.0')
@click.argument('PORT', default=8111, type=int)
def run(debug, threaded, host, port):
    HOST, PORT = host, port
    print 'running on %s:%d' % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


if __name__ == '__main__':
    run()
