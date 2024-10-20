from flask import Flask, render_template , request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print("This is a print statement here")
    return render_template('Cal.html')

@app.route('/post', methods=['POST'])
def post():
    return "received: {}" .format(request.form)

if __name__ == "__main__":
    app.run(debug=True)


def electricity_bill():
    option_0 = "None"
    option_1 = "18750"
    option_2 = "26325"
    option_3 = "33825"

    user_elecBill = input("What is your average electricity bill?\n")

    if user_elecBill == "N/A":
        return option_0
    elif user_elecBill == "$100 - $150":
        return option_1
    elif user_elecBill == "$151 - $200":
        return option_2
    elif user_elecBill == "$201 - $250":
        return option_3


def gas_bill():
    option_0 = "None"
    option_1 = "5250"
    option_2 = "7403"
    option_3 = "9503"

    user_gasBill = input("What is your average gas bill?\n")

    if user_gasBill == "N/A":
        return option_0
    elif user_gasBill == "$40 - $60":
        return option_1
    elif user_gasBill == "$61 - $80":
        return option_2
    elif user_gasBill == "$81 - $100":
        return option_3

def car_miles():
    option_0 = "None"
    option_1 = "208"
    option_2 = "291"

    user_miles = input("What are your average car mileage?\n")

    if user_miles == "N/A":
        return option_0
    elif user_miles == "213mi - 313mi":
        return option_1
    elif user_miles == "313mi - 426mi":
        return option_2


def recycle_paper():
    response_paper = input("Do you recycle paper?\n")
    return response_paper == "Yes"


def recycle_alum_tin():
    response_alumtin = input("Do you recycle aluminum or tin?\n")
    return response_alumtin == "Yes"


def sum_carbonUse():
    total_carbonUse = 0
    total_carbonUse += int(electricity_bill())
    total_carbonUse += int(gas_bill())
    total_carbonUse += int(car_miles())

    if not recycle_alum_tin():
        total_carbonUse += 184

    if not recycle_paper():
        total_carbonUse += 166

    return total_carbonUse


if __name__ == "__main__":
    total_carbonUse = sum_carbonUse()
    print(f"Total carbon use is: {total_carbonUse}")







