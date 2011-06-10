from bottle import route, run

@route('/hello')
@route('/todo')
def hello():
    return "Hello World!"

if __name__ == '__main__':
  import bottle
  app = bottle.app()
  bottle.debug(True)
  bottle.run(app=app,host='localhost', port=8080,reloader=True)
