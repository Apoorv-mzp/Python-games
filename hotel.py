from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# ==========================
# DATA STORAGE (in memory)
# ==========================
rooms = {
    "single": 5,
    "double": 3,
    "deluxe": 2
}

bookings = {}

# ==========================
# HOME PAGE
# ==========================
@app.route("/")
def home():
    return """
    <h1>🏨 Hotel Booking System</h1>
    <a href='/rooms'>View Rooms</a><br>
    <a href='/book'>Book Room</a><br>
    <a href='/bookings'>View Bookings</a><br>
    <a href='/cancel'>Cancel Booking</a><br>
    """

# ==========================
# SHOW ROOMS
# ==========================
@app.route("/rooms")
def show_rooms():
    return f"""
    <h2>🏨 Available Rooms</h2>
    <p>Single Rooms: {rooms['single']}</p>
    <p>Double Rooms: {rooms['double']}</p>
    <p>Deluxe Rooms: {rooms['deluxe']}</p>
    <a href='/'>Back</a>
    """

# ==========================
# BOOK ROOM (GET + POST)
# ==========================
@app.route("/book", methods=["GET", "POST"])
def book_room():
    if request.method == "POST":
        name = request.form["name"]
        room_type = request.form["room"]
        nights = int(request.form["nights"])

        prices = {
            "single": 1000,
            "double": 2000,
            "deluxe": 3500
        }

        if room_type in rooms and rooms[room_type] > 0:
            total = prices[room_type] * nights

            rooms[room_type] -= 1

            bookings[name] = {
                "room": room_type,
                "nights": nights,
                "bill": total
            }

            return f"""
            <h2>✅ Booking Successful!</h2>
            <p>Name: {name}</p>
            <p>Room: {room_type}</p>
            <p>Nights: {nights}</p>
            <p>Total Bill: ₹{total}</p>
            <a href='/'>Back Home</a>
            """
        else:
            return "<h2>❌ Room not available</h2><a href='/'>Back</a>"

    return """
    <h2>🏨 Book a Room</h2>
    <form method='post'>
        Name: <input type='text' name='name' required><br><br>

        Room Type:
        <select name='room'>
            <option value='single'>Single (₹1000)</option>
            <option value='double'>Double (₹2000)</option>
            <option value='deluxe'>Deluxe (₹3500)</option>
        </select><br><br>

        Nights: <input type='number' name='nights' required><br><br>

        <button type='submit'>Book Now</button>
    </form>
    <br><a href='/'>Back</a>
    """

# ==========================
# VIEW BOOKINGS
# ==========================
@app.route("/bookings")
def view_bookings():
    if not bookings:
        return "<h2>📭 No bookings found</h2><a href='/'>Back</a>"

    output = "<h2>📋 All Bookings</h2>"

    for name, data in bookings.items():
        output += f"""
        <p>
        <b>Name:</b> {name}<br>
        <b>Room:</b> {data['room']}<br>
        <b>Nights:</b> {data['nights']}<br>
        <b>Bill:</b> ₹{data['bill']}
        </p>
        <hr>
        """

    output += "<a href='/'>Back</a>"
    return output

# ==========================
# CANCEL BOOKING
# ==========================
@app.route("/cancel", methods=["GET", "POST"])
def cancel():
    if request.method == "POST":
        name = request.form["name"]

        if name in bookings:
            room_type = bookings[name]["room"]
            rooms[room_type] += 1
            del bookings[name]
            return "<h2>✅ Booking Cancelled</h2><a href='/'>Back</a>"
        else:
            return "<h2>❌ Booking not found</h2><a href='/'>Back</a>"

    return """
    <h2>❌ Cancel Booking</h2>
    <form method='post'>
        Enter Name: <input type='text' name='name'><br><br>
        <button type='submit'>Cancel</button>
    </form>
    <br><a href='/'>Back</a>
    """

# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)