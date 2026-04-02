# 📝 Flask Blog App

Eine moderne Blog-Anwendung mit Python und Flask, die grundlegende Web-Development-Konzepte demonstriert – inklusive CRUD-Funktionalität, Kategorien, Likes, Kommentaren und Suchfunktion.

---

## 🚀 Features

- 📄 Beiträge anzeigen (Homepage)
- ➕ Neue Beiträge erstellen
- ✏️ Beiträge bearbeiten
- ❌ Beiträge löschen
- 🏷️ Kategorien für Beiträge
- ❤️ Like-Funktion pro Beitrag
- 💬 Kommentare hinzufügen
- 🔍 Suche & Filter nach Kategorie
- 🎨 Modernes UI mit CSS (Card-Layout)

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML (Jinja2 Templates)
- CSS (Custom Styling)

---

## 📁 Projektstruktur

```
flaskBlog/
│
├── app.py
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── add.html
    └── update.html
```

---

## ⚙️ Installation & Setup

### 1. Repository klonen

```bash
git clone https://github.com/DEIN_USERNAME/flask-blog.git
cd flask-blog
```

### 2. Virtuelle Umgebung erstellen (optional)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Abhängigkeiten installieren

```bash
pip install flask
```

### 4. Anwendung starten

```bash
python app.py
```

---

## 🌐 Anwendung öffnen

```
http://127.0.0.1:5000/
```

---

## 🧠 Funktionsweise

- `/` → alle Beiträge anzeigen  
- `/add` → neuen Beitrag erstellen  
- `/update/<id>` → Beitrag bearbeiten  
- `/delete/<id>` → Beitrag löschen  

---

## ⚠️ Hinweis

Die Daten werden aktuell **nur im Speicher gespeichert**.

👉 Nach einem Neustart der App gehen alle neuen Beiträge verloren.

---

## 🔮 Zukünftige Features

- 💾 Speicherung in JSON oder Datenbank (SQLite)
- 🔐 Benutzer-Login & Authentifizierung
- 📅 Zeitstempel für Beiträge
- 🌙 Dark Mode
- 🖼️ Bilder-Upload
- ⭐ Favoriten-System

---

## 📸 Screenshot

(Optional hinzufügen)

```
![App Screenshot](static/screenshot.png)
```

---

## 👨‍💻 Autor

Sinan Kahraman

---

## 📄 Lizenz

Dieses Projekt dient zu Lernzwecken.
