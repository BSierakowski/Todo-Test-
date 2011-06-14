import sqlite3
from bottle import route, run, debug, template, request, validate, error

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
        
@route('/edit/:no', method='GET')
@validate(no=int)
def edit_item(no):

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip() 

        if status == 'open':
            status = 1
        else:
            status = 0
            
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()
        
        return '<p>The item number %s was successfully updated</p><p><a href="../todo">Back to the list</a>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()
        
        return template('edit_task', old=cur_data, no=no)
        
@route('/item:item#[1-9]+#')
def show_item(item):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item))
    result = c.fetchall()
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' %result[0]
        
@route('/json:json#[1-9]+#')
def show_json(json):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task':'This item number does not exist!'}
    else:
        return {'Task': result[0]}
        
@error(404)
@error(403)
def mistake(code):
    return 'There is something wrong!' 
        
        
#debug(True)
#run(reloader=True)


#if __name__ == '__main__':
#    import bottle
#    app = bottle.app()
#    bottle.debug(True)
#    bottle.run(app=app,host='localhost', port=8080,reloader=True)