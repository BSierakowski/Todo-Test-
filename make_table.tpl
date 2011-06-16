%#Template to generate a HTML table from a list of tuples (or a list of lists, or tuples of tuples...)
<p>The open items are as follows:</p>
<table border="1">
%for r in rows:
<p><b>ID:</b>{{r[0]}}, <b>Task:</b>{{r[1]}}, <a href="/edit/{{r[0]}}">Edit Item</a></p>
%end
</table>

<p><a href="new">Post a new item</a></p>
