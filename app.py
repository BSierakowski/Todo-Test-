import sqlite3
from bottle import route, run, debug, template

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output
    
# debug(True)
# run(reloader=True)        
run()



# if __name__ == '__main__':
#    import bottle
#    app = bottle.app()
#    bottle.debug(True)
#    bottle.run(app=app,host='localhost', port=8080,reloader=True)
