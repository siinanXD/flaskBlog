Design der "Update" Form
Formularfelder mit Werten vorbelegen
Wenn du ein HTML-Formular gestaltest, kannst du mit dem Attribut value einen Standardwert für ein Eingabefeld festlegen. Dieses Attribut bestimmt den Anfangswert des Feldes beim Laden der Seite.
Ein einfaches Beispiel:

<input type="text" name="name" value="John Doe">
In diesem Fall ist „John Doe“ der Standardwert für das Texteingabefeld. Wenn der Benutzer das Formular öffnet, ist das Feld bereits mit „John Doe“ ausgefüllt.
Wenn du dynamische Werte nutzen willst – besonders in Verbindung mit Template-Sprachen wie Jinja2 in Flask – kannst du Werte von der Serverseite übergeben und damit das value-Attribut dynamisch befüllen. Zum Beispiel:

<input type="text" id="author" name="author" value="{{ post.author }}">
Hier ist post.author eine Variable, die von der Flask-Anwendung an das Template übergeben wurde. Die Syntax {{ ... }} wird in Jinja2 verwendet, um den Wert eines Ausdrucks auszugeben. Wenn post.author zum Beispiel „John Doe“ ist, sieht das gerenderte HTML so aus:

<input type="text" id="author" name="author" value="John Doe">
So kannst du Formularfelder dynamisch mit Werten befüllen, wenn du Flask mit Jinja2 verwendest.
Erstelle das Update-Formular
Zum Schluss erstellen wir ein neues Template, update.html, um das Bearbeitungsformular anzuzeigen. Dieses Template wird dem bestehenden add.html sehr ähnlich sein, mit ein paar Unterschieden:
Das action-Attribut des Formulars enthält die ID des Blogeintrags, der bearbeitet werden soll.
Jedes Eingabefeld enthält ein value-Attribut, das die aktuellen Daten des Blogeintrags anzeigt.
Hier ein Beispiel, wie update.html aussehen könnte:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Blog Post</title>
</head>
<body>
    <h1>Update Blog Post</h1>

    <form action="{{ url_for('update', post_id=post['id']) }}" method="POST">
        <label for="author">Author:</label><br>
        <input type="text" id="author" name="author" value="{{ post['author'] }}"><br>
        ...
        <input type="submit" value="Update">
    </form>
</body>
</html>
Deine Flask-Blog-Anwendung unterstützt jetzt das Bearbeiten bestehender Blogeinträge – zusätzlich zum Anzeigen, Hinzufügen und Löschen. Großartig gemacht! 🎉
