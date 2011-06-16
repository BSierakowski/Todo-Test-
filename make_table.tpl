%#Template to generate a HTML table from a list of tuples (or a list of lists, or tuples of tuples...)
<p>Open items todo:</p>
<table border="1">
%for r in rows:
<p><b>{{r[0]}}:</b> {{r[1].rstrip(',')}} | Mark as Complete | <a href="/edit/{{r[0]}}">Edit Item</a></p>
%end
</table>

<p>Completed items:</p>
<table border="1">
%for c in comp:
<p><b>{{c[0]}}:</b> {{c[1].rstrip(',')}} | Mark as New | <a href="/edit/{{c[0]}}">Edit Item</a></p>
%end
</table>

<p><a href="new">Post a new item</a></p>
