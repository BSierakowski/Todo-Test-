import sqlite3
from bottle import route, run, debug, template, request

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    return template('make_table', rows=result)
  
@route('/new', method='GET')
def new_item():

    if request.GET.get('save','').strip():

        new = request.GET.get('task', '').strip()
        
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid
        
        conn.commit()
        c.close()
        
        return '<p>The new task was inserted into the database with the ID %s</p><p><a href="todo">Return to the list</a></p>' % new_id
    else:
        return template('new_task.tpl')

# debug(True)
# run(reloader=True)
run()

#if __name__ == '__main__':
#    import bottle
#    app = bottle.app()
#    bottle.debug(True)
#    bottle.run(app=app,host='localhost', port=8080,reloader=True)
