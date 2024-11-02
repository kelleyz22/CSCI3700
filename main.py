from flask import Flask, render_template
import util

# Create application instance
app = Flask(__name__)

# Global variables
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# Route is used to insert row into basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    try:
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (%s, %s)", (5, 'Cherry'))
        connection.commit()
        return "Success!"
    except Exception as e:
        connection.rollback()
        return f"Error: {e}"
    finally:
        util.disconnect_from_db(connection, cursor)

# Route to display unique fruits in basket_a and basket_b
@app.route('/api/unique')
def unique_fruits():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    try:
        cursor.execute("SELECT DISTINCT fruit FROM basket_a")
        unique_a = cursor.fetchall()
        cursor.execute("SELECT DISTINCT fruit FROM basket_b")
        unique_b = cursor.fetchall()

        sql_table = unique_a + unique_b
        table_title = ["Unique Fruits in Basket A", "Unique Fruits in Basket B"]

        return render_template('index.html', sql_table=sql_table, table_title=table_title)
    except Error as e:
        return f"Error: {e}"
    finally:
        util.disconnect_from_db(connection, cursor)

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
