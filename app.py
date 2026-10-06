from flask import Flask, render_template, request

app = Flask(__name__)


def check_bunching(gap):
    if gap <= 3:
        return "BUNCHING RISK"
    elif gap <= 6:
        return "WARNING"
    else:
        return "NORMAL"


@app.route("/")
def dashboard():

    buses = [
        {"name": "Bus 1", "speed": 32, "gap": 8},
        {"name": "Bus 2", "speed": 28, "gap": 5},
        {"name": "Bus 3", "speed": 25, "gap": 2}
    ]

    for bus in buses:
        bus["status"] = check_bunching(bus["gap"])

    return render_template("dashboard.html", buses=buses)


@app.route("/simulate", methods=["POST"])
def simulate():

    hold_time = int(request.form["hold_time"])

    original_gap = 2
    new_gap = original_gap + hold_time

    old_status = check_bunching(original_gap)
    new_status = check_bunching(new_gap)

    return render_template(
        "dashboard.html",
        buses=[
            {"name": "Bus 1", "speed": 32, "gap": 8, "status": "NORMAL"},
            {"name": "Bus 2", "speed": 28, "gap": 5, "status": "WARNING"},
            {"name": "Bus 3", "speed": 25, "gap": new_gap,
             "status": new_status}
        ],
        simulation=True,
        hold_time=hold_time,
        original_gap=original_gap,
        new_gap=new_gap,
        old_status=old_status,
        new_status=new_status
    )


@app.route("/check", methods=["POST"])
def check():

    speed1 = int(request.form["speed1"])
    gap1 = int(request.form["gap1"])

    speed2 = int(request.form["speed2"])
    gap2 = int(request.form["gap2"])

    speed3 = int(request.form["speed3"])
    gap3 = int(request.form["gap3"])

    buses = [
        {
            "name": "Bus 1",
            "speed": speed1,
            "gap": gap1,
            "status": check_bunching(gap1)
        },
        {
            "name": "Bus 2",
            "speed": speed2,
            "gap": gap2,
            "status": check_bunching(gap2)
        },
        {
            "name": "Bus 3",
            "speed": speed3,
            "gap": gap3,
            "status": check_bunching(gap3)
        }
    ]

    return render_template(
        "dashboard.html",
        buses=buses
    )


if __name__ == "__main__":
    app.run(debug=True)