%#Template to generate a HTML table from a list of tuples (or a list of lists, or tuples of tuples...)
<p>The open items are as follows:</p>
<table border="1">
%for r in rows:
<p>ID:{{r}}, task:{{r}}, <a href="/edit/{{r}}">Edit Item</a></p>
%end
</table>

<p><a href="new">Post a new item</a></p>
