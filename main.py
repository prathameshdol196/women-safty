
from tkinter import *
from tkinter import messagebox
import json
import smtplib
import time
import requests

sender_email = "YOUR MAIL ID"
password = "YOUR PASSWORD"

def user_profile(user):

    def emergency():

        ip = requests.get("https://get.geojs.io/v1/ip.json").json()["ip"]
        print(ip)
        location = requests.get(f"https://get.geojs.io/v1/ip/geo/{ip}.json").json()
        print(location)
        accuracy = location["accuracy"]
        timezone = location["timezone"]
        country_code = location["country_code"]
        country_code3 = location["country_code3"]
        country = location["country"]
        region = location["region"]
        latitude = location["latitude"]
        # longitude = str(latitude["longitude"])

        time.sleep(5)
        recievers_mails = []
        with open(f"{user}.json", "r") as data_file:
            data = json.load(data_file)
            for value in data.values():
                email = value["Email"]
                recievers_mails.append(email)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)

            for reciever_email in recievers_mails:

                connection.sendmail(from_addr=sender_email,
                                    to_addrs=reciever_email,
                                    msg=f"Subject:HELP! Please help I'm {user}, \n\nAnd my Current Location is : \n\nTimezone: {timezone}\nCountry Code: {country_code} \nCountry Code 3: {country_code3} \nCountry: {country} \nRegion: {region} \nLatitude: {latitude} \nLongitude: longitude")
                time.sleep(5)

            print("msg has been sent")

    def save_emergency_contact():

        name = emergency_name_entry.get()
        email = emergency_email_entry.get()
        number = emergency_number_entry.get()
        your_name = your_name_entry.get()

        new_data = {
            name: {
                "Email": email,
                "Number": number
            }
        }

        if len(name) == 0 or len(email) == 0 or len(number) == 0:
            messagebox.showwarning(title="ERROR", message="Please make sure you haven't left any field empty.")

        else:
            conform = messagebox.showinfo(title=name,
                                          message=f"These are the details entered : \nEmail: {email} \n Number: {number} \nis it ok to save")

            if conform:
                try:
                    with open(f"{your_name}.json", "r") as data_file:
                        # reading file data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open(f"{your_name}.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    # updating data with new data
                    data.update(new_data)

                    with open(f"{your_name}.json", "w") as data_file:
                        # writing data to json file
                        json.dump(data, data_file, indent=4)
                finally:
                    emergency_name_entry.delete(0, END)
                    emergency_email_entry.delete(0, END)
                    emergency_number_entry.delete(0, END)

    window.destroy()

    profile = Tk()
    profile.title("User Profile")
    profile.config(padx=50, pady=50, bg="black", height=300, width=300)

    profile_lable_1 = Label(profile, text=f"Hello {user}", bg="black", fg="white", font=20)
    profile_lable_1.grid(column=0, row=0)

    emergency_butten = Button(profile, text="EMERGENCY", bg="red", command=emergency)
    emergency_butten.grid(column=0, row=1)

    add_emergency_contact = Label(profile, text="Add EMERGENCY Contact", bg="black", fg="white", font=("Arial", 10))
    add_emergency_contact.grid(column=1, row=3, pady=50, padx=50)

    your_name = Label(profile, text="Your Name: ", bg="black", fg="white", font=("Arial", 10))
    your_name.grid(column=1, row=4)

    your_name_entry = Entry(profile)
    your_name_entry.grid(column=2, row=4)

    emergency_name = Label(profile, text="Emergency Contact Name: ", bg="black", fg="white", font=("Arial", 10))
    emergency_name.grid(column=1, row=5)

    emergency_name_entry = Entry(profile)
    emergency_name_entry.grid(column=2, row=5)

    emergency_email = Label(profile, text="Emergency Contact Email: ", bg="black", fg="white", font=("Arial", 10))
    emergency_email.grid(column=1, row=6)

    emergency_email_entry = Entry(profile)
    emergency_email_entry.grid(column=2, row=6)

    emergency_number_label = Label(profile, text="Emergency Contact Number: ", bg="black", fg="white", font=("Arial", 10))
    emergency_number_label.grid(column=1, row=7)

    emergency_number_entry = Entry(profile)
    emergency_number_entry.grid(column=2, row=7)

    add_contact_butten = Button(profile, text="ADD", command=save_emergency_contact)
    add_contact_butten.grid(column=2, row=8)


def sign_up():
    def register_user():
        name = name_entry.get()
        email = email_entry.get()
        passs = pass_entry.get()
        repasss = re_pass_entry.get()
        phone = phone_number_entry.get()

        new_data = {
            name: {
                "Email": email,
                "Password": passs,
                "Number": phone
            }
        }

        if len(name) == 0 or len(email) == 0 or len(passs) == 0 or len(repasss) == 0 or len(phone) == 0:
            messagebox.showwarning(title="ERROR", message="Please amke sure no field is left empty.")

        elif passs == repasss:
            conform = messagebox.showinfo(title=name,
                                          message=f"These are the details entered : \nEmail: {email} \n Number: {phone}\n Password: {passs} \nis it ok to save")

            if conform:
                try:
                    with open("users.json", "r") as data_file:
                        # reading file data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open(f"users.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    # updating data with new data
                    data.update(new_data)

                    with open("users.json", "w") as data_file:
                        # writing data to json file
                        json.dump(data, data_file, indent=4)
                finally:
                    sign.destroy()

        else:
            messagebox.showerror(title="ERROR", message="Wrong password. Both passwords should match")


    window.destroy()

    sign = Tk()
    sign.title("SignUp")
    sign.config(padx=50, pady=50, bg="black", height=300, width=300)

    label_1 = Label(sign, text="Please Enter Your Details: ", bg="black", fg="white", font=("Arial", 10), pady=20, padx=20)
    label_1.grid(column=0, row=0)

    name_label = Label(sign, text="Name: ", bg="black", fg="white", font=("Arial", 10))
    name_label.grid(column=1, row=1)

    name_entry = Entry(sign)
    name_entry.grid(column=2, row=1)

    email_label = Label(sign, text="Email: ", bg="black", fg="white", font=("Arial", 10))
    email_label.grid(column=1, row=2)

    email_entry = Entry(sign)
    email_entry.grid(column=2, row=2)

    pass_label = Label(sign, text="Password: ", bg="black", fg="white", font=("Arial", 10))
    pass_label.grid(column=1, row=3)

    pass_entry = Entry(sign)
    pass_entry.grid(column=2, row=3)

    re_pass_label = Label(sign, text="Retype Password: ", bg="black", fg="white", font=("Arial", 10))
    re_pass_label.grid(column=1, row=4)

    re_pass_entry = Entry(sign)
    re_pass_entry.grid(column=2, row=4)

    phone_number_label = Label(sign, text="Phone: ", bg="black", fg="white", font=("Arial", 10))
    phone_number_label.grid(column=1, row=5)

    phone_number_entry = Entry(sign)
    phone_number_entry.grid(column=2, row=5)

    register_btn = Button(sign, text="Register", command=register_user)
    register_btn.grid(column=2, row=6)


def login():
    # user = login_username_entry.get()
    passs = login_password_entry.get()
    if len(login_username_entry.get()) == 0:
        messagebox.showwarning(title="ERROR", message="Please enter a correct username and password.")
    else:
        try:
            with open("users.json", "r") as data_file:
                # load the json data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found.")
        else:
            if login_username_entry.get() in data and data[login_username_entry.get()]["Password"] == passs:
                user_profile(login_username_entry.get())
                # messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
            else:
                messagebox.showwarning(title="Error", message=f"No details for {login_username_entry.get()} found.")


window = Tk()
window.title("Women Safety")
window.geometry("300x200")
window.config(background="black", pady=10)

lable_1 = Label(window, text="Login Form", bg="black", fg="white", font=20)
lable_1.place(x=110, y=5)

login_username = Label(window, text="Username - ", bg="black", fg="white").place(x=10, y=40)
login_username_entry = Entry(window)
login_username_entry.place(x=110, y=40)

login_password = Label(window, text="Password - ", bg="black", fg="white").place(x=10, y=80)
login_password_entry = Entry(window)
login_password_entry.place(x=110, y=80)

login_btn = Button(window, text="Login", command=login)
login_btn.place(x=110, y=120)

sign_up_btn = Button(window,text="SignUp", command=sign_up)
sign_up_btn.place(x=170, y=120)

window.mainloop()
