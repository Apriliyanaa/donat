#!/usr/bin/env python3

import cgi
import cgitb

# Enable debugging
cgitb.enable()

# Function to calculate the surface area of a prism
def calculate_persegi_area(length, width):
    return length * width

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Initialize variables
length = width = 0
area = None

# Get values from the form if submitted
if "submit" in form:
    length = float(form.getvalue('Sisi1', 0))
    width = float(form.getvalue('Sisi2', 0))
    area = calculate_persegi_area(length, width)

# Print the HTTP header
print("Content-Type: text/html\n")
print("<!DOCTYPE html>\n")

# Print the HTML content
print(f"""
<html>
<head>
    <title>Bangun Geometri</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1 {{
            font-size: 24px;
            font-weight: bold;
        }}
        p {{
            font-size: 16px;
            margin: 5px 0;
        }}
        form {{
            margin-top: 20px;
        }}
        input {{
            margin: 5px 0;
        }}
    </style>
</head>
<body>
    <h1>Bangun Geometri</h1>
    <p>Nama bangun: Persegi</p>
    <p>Dimensi (2D/3D): 2D</p>
    <p>Rumus luas : Sisi x Sisi</p>
    
    <form method="post" action="">
        <label for="length">Sisi 1:</label>
        <input type="number" name="Sisi1" step="any" required><br>
        <label for="width">Sisi 2:</label>
        <input type="number" name="Sisi2" step="any" required><br>
        <input type="submit" name="submit" value="Hitung Luas">
    </form>
    
    {f'<p>Sisi 1: {length}</p>' if area is not None else ''}
    {f'<p>Sisi 2: {width}</p>' if area is not None else ''}
    {f'<p>Luas: {area}</p>' if area is not None else ''}
</body>
</html>
""")