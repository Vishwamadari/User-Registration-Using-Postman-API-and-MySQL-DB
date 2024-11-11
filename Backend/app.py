from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

# Configure database connection
def create_connection():
    return mysql.connector.connect(
        host='localhost',  # Database host
        user='root',       # Database user
        password='Vishwa@123',  # Replace with your database password
        database='registration_db'   # Replace with your database name
    )

# CREATE operation
@app.route('/register', methods=['POST'])
def create_registration():
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s)",
            (data['name'], data['email'], data['date_of_birth'], data.get('phone_number'), data.get('address'))
        )
        connection.commit()
        return jsonify({"message": "Registration created successfully!"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        connection.close()

# READ all registrations
@app.route('/register', methods=['GET'])
def get_all_registrations():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Registration")
    registrations = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(registrations), 200

# READ a specific registration by ID
@app.route('/register/<int:id>', methods=['GET'])
def get_registration(id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Registration WHERE ID = %s", (id,))
    registration = cursor.fetchone()
    cursor.close()
    connection.close()
    if registration:
        return jsonify(registration), 200
    else:
        return jsonify({"error": "Registration not found"}), 404

# UPDATE operation
@app.route('/register/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.get_json()
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE Registration SET Name = %s, Email = %s, DateOfBirth = %s, PhoneNumber = %s, Address = %s WHERE ID = %s",
            (data['name'], data['email'], data['date_of_birth'], data.get('phone_number'), data.get('address'), id)
        )
        connection.commit()
        return jsonify({"message": "Registration updated successfully!"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        connection.close()

# DELETE operation
@app.route('/register/<int:id>', methods=['DELETE'])
def delete_registration(id):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Registration WHERE ID = %s", (id,))
        connection.commit()
        return jsonify({"message": "Registration deleted successfully!"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
