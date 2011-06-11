%#Template to generate a HTML table from a list of tuples (or a list of lists, or tuples of tuples...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
    <tr>
    %for r in rows:
        <td>{{r}}</td>
    %end
    </tr>
%end
</table>

<p><a href="new">Post a new item</a></p>
