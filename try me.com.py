import tkinter as tk
from time import strftime
from tkinter import messagebox
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def show_home_content():
    can2.delete("all")  # Clear canvas
    abt_text.config(state="normal")  # Enable text widget for editing
    abt_text.delete("1.0", "end")  # Clear any previous content
    abt_text.insert("1.0", home_content)
    abt_text.config(state="disabled")  # Disable text widget for editing

def show_about_content():
    can2.delete("all")  # Clear canvas
    abt_text.config(state="normal")  # Enable text widget for editing
    abt_text.delete("1.0", "end")  # Clear any previous content
    abt_text.insert("1.0", about_content)
    abt_text.config(state="disabled")  # Disable text widget for editing


# Content for the home page
home_content = """
Welcome to TRY ME.COM - Your Ultimate Hanger Storage Solution!
\n
"Unlock Your Closet's Potential with TRY ME.COM - Hang with Confidence!"

At TRY ME.COM, we take pride in offering top-notch hanger storage services to meet all your hanging needs. Whether you're a fashionista with a collection of trendy outfits or a business professional seeking a tidy closet, we've got you covered.

Our wide range of hangers caters to all your garment types, from delicate dresses to sturdy suits. We understand the value of your clothing, and that's why we provide secure and reliable storage solutions. Say goodbye to wrinkled clothes and messy closets - with TRY ME.COM, your garments are in safe hands.
\n
Why Choose TRY ME.COM:\n\n
- Secure Storage: Our state-of-the-art facilities ensure the utmost protection for your precious garments.\n
- Easy Accessibility: Retrieve your favorite clothes at your convenience, anytime you need them.\n
- 24/7 Support: Our dedicated customer support team is here to assist you round the clock.\n
- Affordable Pricing: Enjoy our cost-effective storage plans tailored to fit your budget.\n

Don't take our word for it! Hear what our satisfied customers have to say about their experience with us. We take pride in their trust and confidence in TRY ME.COM.

So, what are you waiting for? Declutter your closet and make room for new memories. Experience the ease and convenience of TRY ME.COM - your one-stop hanger storage solution.

Browse our featured hangers, explore our services, and get ready to rediscover your wardrobe like never before. Welcome to the world of organized fashion and hassle-free storage!

Get in touch with us today to get started. Happy hanging!
"""

about_content = """
About Us - Fabric Hanger Details.

Welcome to Fabric Hanger Details, your ultimate software solution for organizing and managing fabric hanger information with ease and efficiency. Our mission is to streamline the process of storing, accessing, and updating fabric hanger data, empowering businesses and individuals in the textile industry to work smarter and more effectively.

Who We Are:
Fabric Hanger Details was founded by a team of passionate textile enthusiasts and software experts who saw a need for a better way to handle fabric hanger information. With a deep understanding of the challenges faced by textile manufacturers, retailers, and designers, we set out to create a comprehensive tool that simplifies the way fabric hanger details are recorded and managed.

Our Vision:
At Fabric Hanger Details, we envision a world where every textile professional can effortlessly access and leverage the vital information about fabric hangers. By providing an intuitive and user-friendly platform, we aim to revolutionize the way the textile industry interacts with fabric samples, enabling quicker decision-making, reduced wastage, and enhanced productivity.

What We Offer:
Our software is a feature-rich solution designed to cater specifically to the textile industry's unique needs. With Fabric Hanger Details, you can:

- Effortlessly Organize Fabric Hangers: Our platform allows you to categorize and tag fabric hangers according to material, color, pattern, and more, making it easy to find the right samples for your projects.

- Detailed Information Storage: Record essential details for each fabric hanger, including supplier information, cost, availability, and any additional notes or specifications relevant to your business.

- Real-time Updates and Collaboration: Collaborate seamlessly with your team by sharing fabric hanger details in real-time, ensuring everyone stays informed and up-to-date.

- Data Analytics and Reporting: Make data-driven decisions with our advanced analytics and reporting features, providing valuable insights into your fabric hanger inventory and usage patterns.

- Security and Privacy: We prioritize the security of your data. Fabric Hanger Details employs the latest encryption technologies to keep your information safe and confidential.

Our Commitment:
At Fabric Hanger Details, we are committed to delivering exceptional value to our users. We continually strive to enhance our software by incorporating user feedback and staying up-to-date with the latest advancements in technology and the textile industry. Your success is our success, and we take pride in being a reliable partner on your journey to excellence.

Thank you for choosing Fabric Hanger Details as your trusted software companion. We are excited to embark on this journey with you and look forward to assisting you in achieving greater efficiency and success in the world of textiles. Should you have any questions, feedback, or suggestions, please do not hesitate to reach out to our dedicated support team.

Happy fabric hanger organizing!
"""

# Create main window
root = tk.Tk()
root.title("TRY ME . COM")
root.geometry("1366x768")
root.config(highlightcolor="DarkGoldenrod4", background="gray9", highlightthickness=10)

# Top Frame to add contact details
can1 = tk.Canvas(root, highlightthickness=0, highlightbackground="DarkGoldenrod4",
                 background="gray9", width=1500, height=100)
can1.place(x=0, y=0)

# Adding the company name
Tit = tk.Label(can1, text=" TRY ME . COM ", font=(" Oregon ", 32, "bold"),
               fg="PapayaWhip", bg="gray9")
Tit.place(x=500, y=10)

# Middle Frame
can2 = tk.Canvas(root, highlightthickness=5, bg='gray9',
                 highlightbackground="DarkGoldenrod4", width=1345, height=900)
can2.place(x=0, y=100)

# Create a Text widget for the scrollbar (with wraplength)
abt_text = tk.Text(can2, wrap="word", width=160, height=38,
                   font=("Oregon", 10), state="disabled", bg='gray9', fg='white')
abt_text.place(x=10, y=10)

# Set home content by default when the main window opens
show_home_content()

# Create "About" button
about_button = tk.Button(can1, text="About", font=("Oregon", 10), bg="gray9",
                         fg="MistyRose3", activebackground="grey9",
                         activeforeground="gray9", bd=10, highlightcolor="gray9",
                         relief="flat",
                         command=show_about_content)
about_button.place(x=900, y=60)

# Home button
home_button = tk.Button(can1, text="Home", font=("Times", 10), bg="gray9", fg="MistyRose3",
                        activebackground="grey9",
                        activeforeground="gray9", bd=10, highlightcolor="gray9", relief="flat",
                        command=show_home_content)
home_button.place(x=800, y=60)

import tkinter as tk
import random
import string


def P():
    # Create the main window
    leaf = tk.Tk()
    leaf.geometry("400x400")
    leaf.resizable(0, 0)
    leaf.title("TRY ME.COM - PASSWORD GENERATOR")
    leaf.config(highlightcolor="DarkGoldenrod4", background="white",
                highlightthickness=10)

    def generate_password():
        # Get the desired password length from the Spinbox widget
        length = int(length_var.get())

        # Define the character sets for generating the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Create a list to hold characters for the password, ensuring it contains at least one of each type
        password_list = [random.choice(string.ascii_lowercase),
                         random.choice(string.ascii_uppercase),
                         random.choice(string.digits),
                         random.choice(string.punctuation)]

        # Add random characters to the list until the desired length is reached
        while len(password_list) < length:
            password_list.append(random.choice(characters))

        # Shuffle the password_list to randomize the order of characters
        random.shuffle(password_list)

        # Join the characters into a string to form the password
        password = ''.join(password_list)

        # Clear the password entry and insert the generated password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    def copy_to_clipboard():
        # Get the password from the password entry
        password = password_entry.get()

        # Check if the password is not empty
        if password:
            # Clear the clipboard and append the password to it
            leaf.clipboard_clear()
            leaf.clipboard_append(password)

            # Clear the password entry
            password_entry.delete(0, tk.END)

    # Password Entry Widget
    password_entry = tk.Entry(leaf, show='*', font=('Arial', 12))
    password_entry.pack(pady=10)

    # Length Selection using Spinbox
    length_var = tk.StringVar()
    length_var.set("8")  # Default password length is 8 characters
    length_spinbox = tk.Spinbox(leaf, from_=8, to=16,
                                textvariable=length_var, font=('Arial', 12))
    length_spinbox.pack()

    # Generate Button
    generate_button = tk.Button(leaf, text="Generate Password",
                                command=generate_password)
    generate_button.pack()

    # Copy to Clipboard Button
    copy_button = tk.Button(leaf, text="Copy to Clipboard",
                            command=copy_to_clipboard)
    copy_button.pack(pady=5)

    # Start the Tkinter main loop
    leaf.mainloop()


# Password Generator Button

password_generator = tk.Button(can1, text="Password Generator",
                               font=("Times", 10), bg="gray9",
                               fg="MistyRose3", activebackground="grey9",
                               activeforeground="gray9", bd=10,
                               highlightcolor="gray9", relief="flat", command=P)
password_generator.place(x=1200, y=60)


# Sign Up Button

def new():
    r = tk.Tk()
    r.geometry("1366x768")
    r.config(highlightthickness=7,
             background="gray9", highlightbackground="black")
    r.title("SIGN UP PAGE")
    c = tk.Canvas(r, width=500, height=400,
                  highlightbackground="black", highlightthickness=6,
                  background="white")
    c.place(x=440, y=100)
    n = tk.Label(c, text="Name", font=("Times", 18, "bold"),
                 fg="black", bg="white")
    n.place(x=20, y=40)
    ne = tk.Entry(c, highlightcolor="white",
                  highlightbackground="black", relief="solid",
                  font=("Aerial", 16))
    ne.place(x=240, y=40)
    un = tk.Label(c, text="User Name", font=("Times", 18, "bold"),
                  fg="black", bg="white")
    un.place(x=20, y=80)
    usn = tk.Entry(c, highlightcolor="white",
                   highlightbackground="black", relief="solid",
                   font=("Aerial", 14))
    usn.place(x=240, y=80)
    mi = tk.Label(c, text="Mail Id", font=("Times", 18, "bold"),
                  fg="black", bg="white")
    mi.place(x=20, y=120)
    mai = tk.Entry(c, highlightcolor="white",
                   highlightbackground="black", relief="solid",
                   font=("Aerial", 14))
    mai.place(x=240, y=120)
    p = tk.Label(c, text="Password", font=("Times", 18, "bold"),
                 fg="black", bg="white")
    p.place(x=20, y=160)
    vara = tk.IntVar()

    def sho():
        if vara.get() == 1:
            pa.config(show="")

        elif vara.get() == 0:
            pa.config(show="*")

    ch = tk.Checkbutton(c, text="Show Password",
                        font=("times", 18, "italic"),
                        variable=vara, onvalue=1, bg="white", offvalue=0, command=sho)
    ch.place(x=240, y=190)
    pa = tk.Entry(c, highlightcolor="white",
                  highlightbackground="black", relief="solid", font=("Aerial", 14), show="*")
    pa.place(x=240, y=160)
    cp = tk.Label(c, text="Confirm Password",
                  font=("Times", 18, "bold"), fg="black", bg="white")
    cp.place(x=20, y=240)
    cip = tk.Entry(c, highlightcolor="white",
                   highlightbackground="black", relief="solid", font=("Aerial", 14), show="*")
    cip.place(x=240, y=240)

    def inst():
        if pa.get() == cip.get():
            Name = ne.get()
            Uname = usn.get()
            MailID = mai.get()
            Password = pa.get()
            CPassword = cip.get()
            mys = pymysql.connect(resource_path(host="localhost", user="root",
                                  password="root", database="tryme"))
            myc = mys.cursor()
            sq = "Insert into su(Name,Uname,MailID,Password,CPassword)values(%s,%s,%s,%s,%s)"
            value = (Name, Uname, MailID, Password, CPassword)
            myc.execute(sq, value)
            mys.commit()

            mys.close()
            messagebox.showinfo("Records", f"{Uname} is Record Created!!")
            ne.delete(0, tk.END)
            usn.delete(0, tk.END)
            mai.delete(0, tk.END)
            pa.delete(0, tk.END)
            cip.delete(0, tk.END)
            ne.focus_set()
        else:
            messagebox.showerror("Register", "Password Not Matched")
            pa.delete(0, tk.END)
            cip.delete(0, tk.END)
            pa.focus_set()

    b = tk.Button(c, text="SIGN UP",
                  font=("Times", 16, "bold"), fg="black", bg="cyan", command=inst)
    b.place(x=200, y=300)


log_button = tk.Button(can1, text="sign up", font=("Times", 10), bg="gray9",
                       fg="MistyRose3", activebackground="grey9",
                       activeforeground="gray9", bd=10, highlightcolor="gray9",
                       relief="flat", command=new)
log_button.place(x=1000, y=60)


# Sign In Page Button

def login():
    base = tk.Tk()
    base.geometry("1366x768")
    base.title("TRY ME . COM - LOGIN PAGE")
    base.config(background="gray9", highlightcolor="black", highlightthickness=10)
    can = tk.Canvas(base, width=500, height=400, background="white", highlightbackground="DarkGoldenrod4",
                    highlightthickness=5)
    can.place(x=470, y=160)
    tit = tk.Label(base, text="WELCOME !!",
                   font=("Block Font", 30), fg="white", bg="gray9", width=15)
    tit.place(x=550, y=50)
    o = tk.Label(can, text="TRY ME.COM - LOGIN PAGE",
                 font=("Times New Roman", 13, "bold"), fg="Black", bg="white")
    o.place(x=120, y=50)
    n = tk.Label(can, text="USER ID :",
                 font=("Times New Roman", 20, "bold"), bg="white", fg="chocolate4")
    n.place(x=60, y=150)
    m = tk.Label(can, text="PASSWORD :",
                 font=("Times New Roman", 20, "bold"), bg="white", fg="chocolate4")
    m.place(x=60, y=250)
    nam = tk.Entry(can, font=("Times", 20, "italic"),
                   width=15, relief="groove", bg="burlywood2", fg="black")
    nam.place(x=250, y=150)
    pas = tk.Entry(can, font=("Times", 20, "italic"),
                   width=15, relief="groove", bg="burlywood2", fg="black", show="*")
    pas.place(x=250, y=250)

    def log():
        mysql = pymysql.connect(resource_path(host="localhost",
                                user="root", password="root", database="tryme"))
        mycuror = mysql.cursor()
        sql = "select Uname, Password from su where Uname=%s and Password=%s"
        val = (nam.get(), pas.get())
        mycuror.execute(sql, val)
        ans = mycuror.fetchone()

        if ans is None:
            messagebox.showerror("Login", "Login Failed.")
        else:
            messagebox.showinfo("Login", "Login Successful!!")
            hanger_rt()
            base.destroy()

        # Close the database connection
        mycuror.close()
        mysql.close()

    btn = tk.Button(can, text="Login", font=("arial", 10, "bold"),
                    width=9, relief="groove", bg="burlywood2", fg="black", command=log)
    btn.place(x=280, y=350)


login_button = tk.Button(can1, text="Sign In", font=("Times", 10), bg="gray9", fg="MistyRose3",
                         activebackground="grey9",
                         activeforeground="gray9", bd=10, highlightcolor="gray9", relief="flat",
                         command=login)
login_button.place(x=1100, y=60)

# Adding Hanger Button with DropDown Option

import tkinter as tk
from tkinter import ttk
import pymysql
import time


def hanger_rt():
    rt = tk.Tk()
    rt.title("TRY ME . COM")
    rt.geometry("1366x768")
    rt.config(highlightcolor="DarkGoldenrod4", background="gray9", highlightthickness=10)
    can1 = tk.Canvas(rt, highlightthickness=0, highlightbackground="DarkGoldenrod4",
                     background="burlywood2", width=1500, height=100, )
    can1.place(x=0, y=0)
    hp = tk.Label(can1, text=('HANGER APPLICATION'), font=('Oregon', 28, 'bold'),
                  fg="DarkGoldenrod4",
                  background="burlywood2")
    hp.place(x=300, y=10)
    try_me = tk.Label(can1, text=('TRY ME . COM'), font=('Oregon', 16, 'bold'),
                      fg="DarkGoldenrod4",
                      background="burlywood2")
    try_me.place(x=400, y=58)

    def update_clock(rt, clock_label):
        current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        clock_label.config(text=current_time)  # Update the label text
        rt.after(1000, update_clock, rt, clock_label)  # Schedule the function to run again after 1000ms (1 second)

    # Create the clock label to display the digital clock
    clock_label = tk.Label(rt, text="", font=("Oregon", 24, 'bold'), fg="black", bg="burlywood2")
    clock_label.place(x=40, y=15)  # Set the position of the clock label
    # Create a label to display the current date
    current_date_label = tk.Label(rt, text="", font=("Oregon", 12), fg="black", bg="burlywood2")
    current_date_label.place(x=65, y=60)  # Set the position of the date label

    def update_clock_and_date(rt, clock_label, current_date_label):
        current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        current_date = time.strftime("%Y-%m-%d")  # Get the current date in YYYY-MM-DD format
        clock_label.config(text=current_time)  # Update the clock label text
        current_date_label.config(text=current_date)  # Update the date label text
        rt.after(1000, update_clock_and_date, rt, clock_label,
                 current_date_label)  # Schedule the function to run again after 1000ms (1 second)

    # Call the update_clock_and_date function to start updating the clock and date
    update_clock_and_date(rt, clock_label, current_date_label)

    # Call the update_clock function to start updating the clock
    update_clock(rt, clock_label)

    def hanger():
        global is_pending_var
        import tkinter as tk
        from datetime import date
        from tkinter import messagebox, ttk
        import pymysql
        leaf = tk.Tk()
        leaf.title("TRY ME . COM - HANGER ENTRY")
        leaf.geometry("1366x768")
        leaf.config(highlightcolor="DarkGoldenrod4", background="white",
                    highlightthickness=5, width=600, height=600)

        def auto_enter_date():
            current_date = date.today()
            lnm.delete(0, tk.END)  # Clear the entry widget
            lnm.insert(0, str(current_date))  # Insert the current date into the entry widget

        # Create an entry widget to enter the date
        lnm = tk.Entry(leaf, font=("Areial", 10, "bold"),
                       fg="black", bg="burlywood2")
        lnm.place(x=300, y=100)

        # Create a button to auto-enter the date

        lf = tk.Label(leaf, text="Date :", font=("Oregon", 12, "bold"),
                      fg="chocolate4", bg="white")
        lf.place(x=100, y=100)

        lf = tk.Button(leaf, text="Enter", font=("Oregon", 9, "bold"),
                       fg="chocolate4", bg="white", command=auto_enter_date)
        lf.place(x=450, y=95)

        laf = tk.Label(leaf, text="M-sub NO :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        laf.place(x=100, y=150)
        lae = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2")
        lae.place(x=300, y=150)
        lbf = tk.Label(leaf, text="Color :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        lbf.place(x=100, y=200)
        lbg = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2")
        lbg.place(x=300, y=200)
        lff = tk.Label(leaf, text="Fabric Description :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        lff.place(x=100, y=250)
        lfn = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2")
        lfn.place(x=300, y=250)
        lmf = tk.Label(leaf, text="Achieved GSM :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        lmf.place(x=100, y=300)
        lmn = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2")
        lmn.place(x=300, y=300)
        lqf = tk.Label(leaf, text="Buyer :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        lqf.place(x=100, y=350)
        vleaf = tk.StringVar(leaf)
        values = ("BE", "ME", "BCA", "BA", "MA", "Bsc", "Msc", "others")
        qf = ttk.Combobox(leaf, font=("Oregon", 18, "bold"),
                          textvariable=vleaf, values=values)
        qf.place(x=300, y=350)
        lef = tk.Label(leaf, text="Count :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        lef.place(x=100, y=400)
        eleaf = tk.StringVar(leaf)
        value = ("0 Year", "1 Year", "2 Year", "3 Year", "4 Year", "5 Year", "More Than 5 Years")
        ef = ttk.Combobox(leaf, font=("Oregon", 18, "bold"),
                          textvariable=eleaf, values=value)
        ef.place(x=300, y=400)
        laf = tk.Label(leaf, text="Submission :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        laf.place(x=100, y=450)
        lad = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2", width=50)
        lad.place(x=300, y=450)
        lpf = tk.Label(leaf, text="TCX No :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        lpf.place(x=100, y=500)
        lpn = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2")
        lpn.place(x=300, y=500)
        ltf = tk.Label(leaf, text="Dia :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        ltf.place(x=100, y=550)
        lta = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2", width=50)
        lta.place(x=300, y=550)
        lpnf = tk.Label(leaf, text="Gage :", font=("Oregon", 12, "bold"),
                        fg="chocolate4", bg="white")
        lpnf.place(x=100, y=600)
        lpin = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lpin.place(x=300, y=600)
        lpf = tk.Label(leaf, text=" Mechine Made :", font=("Oregon", 12, "bold"),
                       fg="chocolate4", bg="white")
        lpf.place(x=100, y=650)
        lphn = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lphn.place(x=300, y=650)
        lapf = tk.Label(leaf, text="Greige GSM :", font=("Oregon", 12, "bold"),
                        fg="chocolate4", bg="white")
        lapf.place(x=700, y=100)
        lap = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2")
        lap.place(x=900, y=100)
        lemf = tk.Label(leaf, text="Required GSM :", font=("Oregon", 12, "bold"),
                        fg="chocolate4", bg="white")
        lemf.place(x=700, y=150)
        lem = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                       bg="burlywood2")
        lem.place(x=900, y=150)
        lemf1 = tk.Label(leaf, text="Loop Length :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf1.place(x=700, y=200)
        lem1 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem1.place(x=900, y=200)
        lemf2 = tk.Label(leaf, text="Comments :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf2.place(x=700, y=250)
        lem2 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem2.place(x=900, y=250)
        lemf3 = tk.Label(leaf, text="Approved By :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf3.place(x=700, y=300)
        lem3 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem3.place(x=900, y=300)
        lemf4 = tk.Label(leaf, text="Yarn From :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf4.place(x=700, y=350)
        lem4 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem4.place(x=900, y=350)
        lemf5 = tk.Label(leaf, text="Knitting By :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf5.place(x=700, y=400)
        lem5 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem5.place(x=900, y=400)
        lemf6 = tk.Label(leaf, text="Washing By :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf6.place(x=700, y=450)
        lem6 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem6.place(x=900, y=450)
        lemf7 = tk.Label(leaf, text="Dyeing By :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf7.place(x=700, y=500)
        lem7 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem7.place(x=900, y=500)
        lemf8 = tk.Label(leaf, text="Compacting By :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf8.place(x=700, y=550)
        lem8 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem8.place(x=900, y=550)
        lemf9 = tk.Label(leaf, text="Finishing By :", font=("Oregon", 12, "bold"),
                         fg="chocolate4", bg="white")
        lemf9.place(x=1070, y=100)
        lem9 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                        bg="burlywood2")
        lem9.place(x=1200, y=100)
        lb = tk.Canvas(leaf, highlightthickness=0, highlightbackground="chocolate4",
                       background="chocolate4", width=1600, height=60, )
        lb.place(x=0, y=0)
        lff1 = tk.Label(leaf, text="Fabric Composition :", font=("Oregon", 12, "bold"),
                        fg="chocolate4", bg="white")
        lff1.place(x=700, y=600)
        lfn12 = tk.Entry(leaf, font=("Areial", 10, "bold"), fg="black",
                         bg="burlywood2")
        lfn12.place(x=900, y=600)
        Title = tk.Label(leaf, text="HANGER ENTRY FIELD", font=("Oregon", 20, "bold"),
                         fg="PapayaWhip", bg="chocolate4")
        Title.place(x=550, y=15)
        is_pending_var = tk.IntVar()  # Variable to store the checkbox value (0 or 1)
        is_pending_checkbox = tk.Checkbutton(leaf, text="Is Pending", font=("Oregon", 12, "bold"),
                                             fg="chocolate4", bg="white", variable=is_pending_var)
        is_pending_checkbox.place(x=1070, y=150)
        # Get the value of the "Is Pending" checkbox (0 or 1)
        is_pending_value = is_pending_var.get()

        def insert():


            Date = lnm.get()
            M_SubNo = lae.get()
            Color = lbg.get()
            F_Des = lfn.get()
            A_GSM = lmn.get()
            Buyer = qf.get()
            Count = ef.get()
            Subm = lad.get()
            TCX_No = lta.get()
            Dia = lphn.get()
            Gage = lem.get()
            M_Made = lpin.get()
            G_GSM = lap.get()
            R_GSM = lem.get()
            L_Length = lem1.get()
            Comments = lem2.get()
            Approved_By = lem3.get()
            Yarn_From = lem4.get()
            Knitting_By = lem5.get()
            W_By = lem6.get()
            Dyeing_By = lem7.get()
            Compacting_By = lem8.get()
            Finishing_By = lem9.get()
            F_Composition = lfn12.get()

            mys = pymysql.connect(resource_path(host="localhost",
                                  user="root", password="root", database="tryme"))
            myc = mys.cursor()
            is_pending = 1 if is_pending_var.get() == 1 else 0

            sq = "INSERT INTO hanger_entry (Date, M_SubNo, Color, F_Des, " \
                 "A_GSM, Buyer, Count, Subm, TCX_No, Dia, Gage, M_Made, " \
                 "G_GSM, R_GSM, L_Length, Comments, Approved_By, Yarn_From," \
                 " Knitting_By, W_By, Dyeing_By, Compacting_By, " \
                 "Finishing_By, F_Composition, is_pending) " \
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" \
                 ",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            values1 = (Date, M_SubNo, Color, F_Des, A_GSM, Buyer, Count,
                       Subm, TCX_No, Dia, Gage, M_Made, G_GSM, R_GSM,
                       L_Length, Comments, Approved_By, Yarn_From, Knitting_By,
                       W_By, Dyeing_By, Compacting_By,
                       Finishing_By, F_Composition, is_pending_var.get())

            myc.execute(sq, values1)
            mys.commit()
            mys.close()

            messagebox.showinfo("Records", f"Record of {Buyer} with {M_SubNo} is  Created!!")
            lnm.delete(0, tk.END)
            lae.delete(0, tk.END)
            lbg.delete(0, tk.END)
            lfn.delete(0, tk.END)
            lmn.delete(0, tk.END)
            qf.delete(0, tk.END)
            ef.delete(0, tk.END)
            lad.delete(0, tk.END)
            lta.delete(0, tk.END)
            lphn.delete(0, tk.END)
            lem.delete(0, tk.END)
            lpin.delete(0, tk.END)
            lap.delete(0, tk.END)
            lem.delete(0, tk.END)
            lem1.delete(0, tk.END)
            lem2.delete(0, tk.END)
            lem3.delete(0, tk.END)
            lem4.delete(0, tk.END)
            lem5.delete(0, tk.END)
            lem6.delete(0, tk.END)
            lem7.delete(0, tk.END)
            lem8.delete(0, tk.END)
            lem9.delete(0, tk.END)
            lfn12.delete(0, tk.END)

            lnm.focus_set()

        lbtn = tk.Button(leaf, text="CREATE", font=("Oregon", 15), fg=("black"),
                         bg="chocolate2", command=insert, borderwidth=10)
        lbtn.place(x=1150, y=500)

    hanger_button = tk.Button(can1, text="Hanger Entry", font=("Oregon", 10, 'bold'),
                              bg="DarkGoldenrod4",
                              fg="black",
                              activebackground="burlywood2",
                              activeforeground="gray9", bd=10, highlightcolor="gray9",
                              relief="flat",
                              command=hanger)
    hanger_button.place(x=800, y=60)

    def hanger_details():


        import pymysql
        import tkinter as tk
        from tkinter import ttk, messagebox

        hd = tk.Tk()
        hd.title("Hanger Details Updation")
        hd.geometry("1300x700")
        con = pymysql.connect(resource_path(host="localhost", user="root", password="root", database="tryme"))
        conn = con.cursor()
        conn.execute("select * from hanger_entry")
        lb = tk.Canvas(hd, highlightthickness=0, highlightbackground="chocolate4",
                       background="chocolate4", width=1300, height=60)
        lb.pack(fill="x", side="top")
        Title = tk.Label(hd, text="TRY ME . COM", font=("Oregon", 20, "bold"),
                         foreground="PapayaWhip", background="chocolate4")
        Title.place(x=500, y=10)
        Title1 = tk.Label(hd, text="HANGER DETAILS", font=("Oregon", 10, "bold"),
                          foreground="PapayaWhip", background="chocolate4")
        Title1.place(x=700, y=20)
        Title2 = tk.Label(hd, text="WELCOME TO", font=("Oregon", 10, "bold"),
                          foreground="PapayaWhip", background="chocolate4")
        Title2.place(x=400, y=20)
        # Create an instance of ttk.Treeview
        tree = ttk.Treeview(hd)
        tree['show'] = 'headings'
        s = ttk.Style(hd)
        s.theme_use("clam")
        s.configure("Treeview.Heading", font=(" Oregon ", 10, "bold"), background="PapayaWhip")
        tree["columns"] = ("SI_no", "Date", "M_SubNo", "Color", "F_Des",
                           "A_GSM", "Buyer", "Count", "Subm", "TCX_No", "Dia", "Gage", "M_Made",
                           "G_GSM", "R_GSM", "L_Length", "Comments", "Approved_By", "Yarn_From",
                           "Knitting_By", "W_By", "Dyeing_By", "Compacting_By", "Finishing_By",
                           "F_Composition", "is_pending")

        tree.column("SI_no", width=30, minwidth=100, anchor=tk.CENTER)
        tree.column("Date", width=50, minwidth=100, anchor=tk.CENTER)
        tree.column("M_SubNo", width=70, minwidth=70, anchor=tk.CENTER)
        tree.column("Color", width=70, minwidth=100, anchor=tk.CENTER)
        tree.column("F_Des", width=70, minwidth=100, anchor=tk.CENTER)
        tree.column("A_GSM", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Buyer", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Count", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Subm", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("TCX_No", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Dia", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Gage", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("M_Made", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("G_GSM", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("R_GSM", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("L_Length", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Comments", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Approved_By", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Yarn_From", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Knitting_By", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("W_By", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Dyeing_By", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Compacting_By", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("Finishing_By", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("F_Composition", width=70, anchor=tk.CENTER, minwidth=100)
        tree.column("is_pending", width=70, anchor=tk.CENTER, minwidth=100)
        # Create headings for the columns
        tree.heading("SI_no", text='SI.No', anchor=tk.CENTER)
        tree.heading("Date", text='Date', anchor=tk.CENTER)
        tree.heading("M_SubNo", text='M-Sub No', anchor=tk.CENTER)
        tree.heading("Color", text='Color', anchor=tk.CENTER)
        tree.heading("F_Des", text='Fabric Description', anchor=tk.CENTER)
        tree.heading("A_GSM", text='Achieved GSM', anchor=tk.CENTER)
        tree.heading("Buyer", text='Buyer', anchor=tk.CENTER)
        tree.heading("Count", text='Count', anchor=tk.CENTER)
        tree.heading("Subm", text='Submission', anchor=tk.CENTER)
        tree.heading("TCX_No", text='TCX No', anchor=tk.CENTER)
        tree.heading("Dia", text='Dia', anchor=tk.CENTER)
        tree.heading("Gage", text='Gage', anchor=tk.CENTER)
        tree.heading("M_Made", text='Mechine Make', anchor=tk.CENTER)
        tree.heading("G_GSM", text='Griege GSM', anchor=tk.CENTER)
        tree.heading("R_GSM", text='Required GSM', anchor=tk.CENTER)
        tree.heading("L_Length", text='Loop Length', anchor=tk.CENTER)
        tree.heading("Comments", text='Comments', anchor=tk.CENTER)
        tree.heading("Approved_By", text='Approved By', anchor=tk.CENTER)
        tree.heading("Yarn_From", text='Yarn From', anchor=tk.CENTER)
        tree.heading("Knitting_By", text='Knitting By', anchor=tk.CENTER)
        tree.heading("W_By", text='Washing By', anchor=tk.CENTER)
        tree.heading("Dyeing_By", text='Dyeing By', anchor=tk.CENTER)
        tree.heading("Compacting_By", text='Compacting By', anchor=tk.CENTER)
        tree.heading("Finishing_By", text='Finishing By', anchor=tk.CENTER)
        tree.heading("F_Composition", text='Fabric Composition', anchor=tk.CENTER)
        tree.heading("is_pending", text='Pending Status', anchor=tk.CENTER)
        l = 0
        for l, row in enumerate(conn):
            tree.insert('', l, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5],
                                                row[6], row[7], row[8], row[9], row[10], row[11],
                                                row[12], row[13], row[14], row[15], row[16], row[17],
                                                row[18], row[19], row[20], row[21], row[22], row[23],
                                                row[24], row[25]))
        scroll_bar = ttk.Scrollbar(hd, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scroll_bar.set)
        scroll_bar.pack(fill="x", side="bottom")

        vsb = ttk.Scrollbar(hd, orient="vertical", command=tree.yview)
        tree.configure(xscrollcommand=vsb.set)
        vsb.pack(fill="y", side="right")

        # Function to delete selected item
        def delete_selected():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select an item to delete.")
                return

            confirmed = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected item?")
            if confirmed:
                for item in selected_item:
                    values = tree.item(item, "values")
                    row_id = values[0]

                    try:
                        conn.execute(f"DELETE FROM hanger_entry WHERE SI_no={row_id}")
                        con.commit()
                        tree.delete(item)
                        messagebox.showinfo("Success", f"Item with SI.No {row_id} deleted successfully.")
                    except Exception as e:
                        messagebox.showerror("Error", f"Error deleting item: {str(e)}")

        # Create Delete button
        delete_button = tk.Button(hd, text="Delete", font=("Oregon", 10, 'bold'), bg="DarkGoldenrod4",
                                  fg="black",
                                  activebackground="burlywood2",
                                  activeforeground="gray9", bd=10,
                                  highlightcolor="gray9", relief="flat",
                                  command=delete_selected)
        delete_button.place(x=180, y=10)

        def read_selected():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select an item to read.")
                return

            for item in selected_item:
                values = tree.item(item, "values")
                # Display the selected item's values in a dialog box
                message = "\n".join([f"{column}: {value}" for column, value in zip(tree["columns"], values)])
                messagebox.showinfo("Read Item", message)

        # Function to refresh the treeview
        def refresh_tree():
            tree.delete(*tree.get_children())  # Clear the treeview
            conn.execute("select * from hanger_entry")
            for row in conn:
                tree.insert("", "end", values=row)

        # Create Read button
        read_button = tk.Button(hd, text="Read", font=("Oregon", 10, 'bold'), bg="DarkGoldenrod4",
                                fg="black",
                                activebackground="burlywood2",
                                activeforeground="gray9", bd=10,
                                highlightcolor="gray9", relief="flat",
                                command=read_selected)
        read_button.place(x=120, y=10)

        # Create Refresh button
        refresh_button = tk.Button(hd, text="Refresh", font=("Oregon", 10, 'bold'), bg="DarkGoldenrod4",
                                   fg="black",
                                   activebackground="burlywood2",
                                   activeforeground="gray9", bd=10,
                                   highlightcolor="gray9", relief="flat",
                                   command=refresh_tree)
        refresh_button.place(x=240, y=10)

        # Function to open the edit window and populate the fields with selected data
        def open_edit_window():

            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select an item to edit.")
                return

            # Get the selected item's values
            values = tree.item(selected_item, "values")
            si_no = values[0]
            date = values[1]
            m_sub_no = values[2]
            color = values[3]
            F_Des = values[4]
            A_GSM = values[5]
            Buyer = values[6]
            Count = values[7]
            Subm = values[8]
            TCX_No = values[9]
            Dia = values[10]
            Gage = values[11]
            M_Made = values[12]
            G_GSM = values[13]
            R_GSM = values[14]
            L_Length = values[15]
            Comments = values[16]
            Approved_By = values[17]
            Yarn_From = values[18]
            Knitting_By = values[19]
            W_By = values[20]
            Dyeing_By = values[21]
            Compacting_By = values[22]
            Finishing_By = values[23]
            F_Composition = values[24]
            is_pending = values[25]
            edit_window = tk.Toplevel(hd)
            edit_window.title("Edit Hanger Details")
            edit_window.geometry("1300x700")

            # SI No
            lft = tk.Label(edit_window, text="SI No :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lft.place(x=100, y=70)
            lft1 = tk.Entry(edit_window, font=("Areial", 10, "bold"),
                            foreground="black", background="burlywood2")
            lft1.place(x=300, y=70)
            lft1.insert(0, si_no)

            # Date
            lf = tk.Label(edit_window, text="Date :", font=("Oregon", 12, "bold"),
                          foreground="chocolate4", background="white")
            lf.place(x=100, y=100)
            lnm = tk.Entry(edit_window, font=("Areial", 10, "bold"),
                           foreground="black", background="burlywood2")
            lnm.place(x=300, y=100)
            lnm.insert(0, date)

            # M-sub NO
            laf = tk.Label(edit_window, text="M-sub NO :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            laf.place(x=100, y=150)
            lae = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2")
            lae.place(x=300, y=150)
            lae.insert(0, m_sub_no)

            # Color
            lbf = tk.Label(edit_window, text="Color :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lbf.place(x=100, y=200)
            lbackground = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                                   background="burlywood2")
            lbackground.place(x=300, y=200)
            lbackground.insert(0, color)

            lff = tk.Label(edit_window, text="Fabric Description :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lff.place(x=100, y=250)
            lfn = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2")
            lfn.place(x=300, y=250)
            lfn.insert(0, F_Des)

            lmf = tk.Label(edit_window, text="Achieved GSM :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lmf.place(x=100, y=300)
            lmn = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2")
            lmn.place(x=300, y=300)
            lmn.insert(0, A_GSM)

            lqf = tk.Label(edit_window, text="Buyer :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lqf.place(x=100, y=350)
            # Create a Combobox for "Buyer"
            vleaf = tk.StringVar(edit_window)
            values = (
            "Norlanka", "John Lewis", "George", "Emjay", "Senvin", "Tharaka", "TrendyWear", "Matalan")  # Set the values
            qf = ttk.Combobox(edit_window, font=("Oregon", 18, "bold"), textvariable=vleaf, values=values)
            qf.place(x=300, y=350)
            # Set the default placeholder text for the Combobox
            qf.insert(0, Buyer)

            lef = tk.Label(edit_window, text="Count :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lef.place(x=100, y=400)
            ef = ttk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2", width=50)
            ef.place(x=300, y=400)
            ef.insert(0, Count)

            laf = tk.Label(edit_window, text="Submission :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            laf.place(x=100, y=450)
            lad = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2", width=50)
            lad.place(x=300, y=450)
            lad.insert(0, Subm)

            lpf = tk.Label(edit_window, text="TCX No :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lpf.place(x=100, y=500)
            lpn = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2")
            lpn.place(x=300, y=500)
            lpn.insert(0, TCX_No)

            ltf = tk.Label(edit_window, text="Dia :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            ltf.place(x=100, y=550)
            lta = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2", width=50)
            lta.place(x=300, y=550)
            lta.insert(0, Dia)

            lpnf = tk.Label(edit_window, text="Gage :", font=("Oregon", 12, "bold"),
                            foreground="chocolate4", background="white")
            lpnf.place(x=100, y=600)
            lpin = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lpin.place(x=300, y=600)
            lpin.insert(0, Gage)

            lpf = tk.Label(edit_window, text=" Mechine Made :", font=("Oregon", 12, "bold"),
                           foreground="chocolate4", background="white")
            lpf.place(x=100, y=650)
            lphn = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lphn.place(x=300, y=650)
            lphn.insert(0, M_Made)

            lapf = tk.Label(edit_window, text="Greige GSM :", font=("Oregon", 12, "bold"),
                            foreground="chocolate4", background="white")
            lapf.place(x=700, y=100)
            lap = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2")
            lap.place(x=900, y=100)
            lap.insert(0, G_GSM)

            lemf = tk.Label(edit_window, text="Required GSM :", font=("Oregon", 12, "bold"),
                            foreground="chocolate4", background="white")
            lemf.place(x=700, y=150)
            lem = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                           background="burlywood2")
            lem.place(x=900, y=150)
            lem.insert(0, R_GSM)

            lemf1 = tk.Label(edit_window, text="Loop Length :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf1.place(x=700, y=200)
            lem1 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem1.place(x=900, y=200)
            lem1.insert(0, L_Length)

            lemf2 = tk.Label(edit_window, text="Comments :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf2.place(x=700, y=250)
            lem2 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem2.place(x=900, y=250)
            lem2.insert(0, Comments)

            lemf3 = tk.Label(edit_window, text="Approved By :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf3.place(x=700, y=300)
            lem3 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem3.insert(0, Approved_By)

            lem3.place(x=900, y=300)
            lemf4 = tk.Label(edit_window, text="Yarn From :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf4.place(x=700, y=350)
            lem4 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem4.place(x=900, y=350)
            lem4.insert(0, Yarn_From)

            lemf5 = tk.Label(edit_window, text="Knitting By :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf5.place(x=700, y=400)
            lem5 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem5.place(x=900, y=400)
            lem5.insert(0, Knitting_By)

            lemf6 = tk.Label(edit_window, text="Washing By :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf6.place(x=700, y=450)
            lem6 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem6.place(x=900, y=450)
            lem6.insert(0, W_By)

            lemf7 = tk.Label(edit_window, text="Dyeing By :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf7.place(x=700, y=500)
            lem7 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem7.place(x=900, y=500)
            lem7.insert(0, Dyeing_By)

            lemf8 = tk.Label(edit_window, text="Compacting By :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf8.place(x=700, y=550)
            lem8 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem8.place(x=900, y=550)
            lem8.insert(0, Compacting_By)

            lemf9 = tk.Label(edit_window, text="Finishing By :", font=("Oregon", 12, "bold"),
                             foreground="chocolate4", background="white")
            lemf9.place(x=1070, y=100)
            lem9 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                            background="burlywood2")
            lem9.place(x=1200, y=100)
            lem9.insert(0, Finishing_By)

            lb = tk.Canvas(edit_window, highlightthickness=0, highlightbackground="chocolate4",
                           background="chocolate4", width=1600, height=60, )
            lb.place(x=0, y=0)

            lff1 = tk.Label(edit_window, text="Fabric Composition :", font=("Oregon", 12, "bold"),
                            foreground="chocolate4", background="white")
            lff1.place(x=700, y=600)
            lfn12 = tk.Entry(edit_window, font=("Areial", 10, "bold"), foreground="black",
                             background="burlywood2")
            lfn12.place(x=900, y=600)
            lfn12.insert(0, F_Composition)

            is_pending_var = tk.IntVar()  # Variable to store the checkbox value (0 or 1)
            is_pending_checkbox = tk.Checkbutton(edit_window, text="Is Pending", font=("Oregon", 12, "bold"),
                                                 foreground="chocolate4", background="white", variable=is_pending_var)
            is_pending_checkbox.place(x=1070, y=150)
            is_pending_var.get()
            is_pending_var.get()

            # Create the Update button for the edit window
            def update_data():
                new_si_no = lft1.get()
                new_date = lnm.get()
                new_m_sub_no = lae.get()
                new_color = lbackground.get()
                new_achieved_gsm = lmn.get()  # Corrected variable name
                new_buyer = vleaf.get()  # Corrected variable name
                new_count = ef.get()  # Corrected variable name
                new_subm = lad.get()
                new_tcx_no = lpn.get()
                new_dia = lta.get()
                new_gage = lpin.get()
                new_m_made = lphn.get()
                new_g_gsm = lap.get()
                new_r_gsm = lem.get()
                new_l_length = lem1.get()
                new_comments = lem2.get()
                new_approved_by = lem3.get()
                new_yarn_from = lem4.get()
                new_knitting_by = lem5.get()
                new_washing_by = lem6.get()
                new_dyeing_by = lem7.get()
                new_compacting_by = lem8.get()
                new_finishing_by = lem9.get()
                new_f_composition = lfn12.get()
                new_is_pending = is_pending_var.get()

                try:
                    conn.execute(
                        f"UPDATE hanger_entry SET SI_no='{new_si_no}', Date='{new_date}',"
                        f" M_SubNo='{new_m_sub_no}', Color='{new_color}', A_GSM='{new_achieved_gsm}',"
                        f" Buyer='{new_buyer}', Count='{new_count}', Subm='{new_subm}',"
                        f" TCX_No='{new_tcx_no}', Dia='{new_dia}', Gage='{new_gage}',"
                        f" M_Made='{new_m_made}', G_GSM='{new_g_gsm}', R_GSM='{new_r_gsm}',"
                        f" L_Length='{new_l_length}', Comments='{new_comments}',"
                        f" Approved_By='{new_approved_by}', Yarn_From='{new_yarn_from}',"
                        f" Knitting_By='{new_knitting_by}', W_By='{new_washing_by}',"
                        f" Dyeing_By='{new_dyeing_by}', Compacting_By='{new_compacting_by}',"
                        f" Finishing_By='{new_finishing_by}', F_Composition='{new_f_composition}',"
                        f" is_pending='{new_is_pending}' WHERE SI_no='{si_no}'")
                    con.commit()
                    messagebox.showinfo("Success", "Data updated successfully.")
                    edit_window.destroy()  # Close the edit window after update
                except Exception as e:
                    messagebox.showerror("Error", f"Error updating data: {str(e)}")

            update_button = tk.Button(edit_window, text="Update", font=("Oregon", 10, 'bold'), bg="DarkGoldenrod4",
                                      fg="black",
                                      activebackground="burlywood2",
                                      activeforeground="gray9", bd=10,
                                      highlightcolor="gray9", relief="flat",
                                      command=update_data)
            update_button.place(x=300, y=20)

        # Create Edit button
        edit_button = tk.Button(hd, text="Edit", font=("Oregon", 10, 'bold'), bg="DarkGoldenrod4",
                                fg="black",
                                activebackground="burlywood2",
                                activeforeground="gray9", bd=10,
                                highlightcolor="gray9", relief="flat",
                                command=open_edit_window)
        edit_button.place(x=70, y=10)

        tree.pack()


    def hanger_pending():
        def refresh_pending_data():
            Tree.delete(*Tree.get_children())
            my_conn.execute("SELECT * FROM hanger_entry WHERE is_pending = 1")
            i = 0
            for ro in my_conn.fetchall():
                Tree.insert('', i, text='', values=ro)
                i += 1

        ht = tk.Tk()
        ht.title("TRY ME.COM - Pending Hanger Entries")
        ht.geometry("1200x600")

        my = pymysql.connect(resource_path(host="localhost", user="root", password="root", database="tryme"))
        my_conn = my.cursor()

        columns = ["SI.NO", "Date", "M_SubNo", "Color", "F_Des", "A_GSM", "Buyer",
                   "Count", "Subm", "TCX_No", "Dia",
                   "Gage", "M_Made", "G_GSM", "R_GSM", "L_Length", "Comments",
                   "Approved_By", "Yarn_From",
                   "Knitting_By", "W_By", "Dyeing_By", "Compacting_By",
                   "Finishing_By", "F_Composition", "is_pending"]

        Tree = ttk.Treeview(ht)
        Tree['show'] = 'headings'
        Tree['columns'] = columns

        for col in columns:
            Tree.column(col, width=100, minwidth=50, anchor=tk.CENTER)
            Tree.heading(col, text=col, anchor=tk.CENTER)

        # Create a Refresh button and place it at the top
        refresh_button = ttk.Button(ht, text="Refresh", command=refresh_pending_data)
        refresh_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        refresh_pending_data()

        Tree.pack(fill='both', expand=True)

        def edit_pending_status():
            selected_item = Tree.selection()
            if selected_item:
                entry_id = Tree.item(selected_item, 'values')[0]  # Assuming the first column is the entry ID
                new_status = 0 if Tree.item(selected_item, 'values')[1] == 1 else 1  # Toggle is_pending status
                my_conn.execute("UPDATE hanger_entry SET is_pending = %s WHERE entry_id = %s", (new_status, entry_id))
                my.commit()

                refresh_pending_data()

        for col in columns + ['Edit']:
            Tree.column(col, width=100, minwidth=50, anchor=tk.CENTER)
            Tree.heading(col, text=col, anchor=tk.CENTER)

        # Create an Edit button and place it below the Refresh button
        edit_button = ttk.Button(ht, text="Edit", command=edit_pending_status)
        edit_button.place(x=40, y=100)

        ht.mainloop()

    hanger_button = tk.Button(can1, text="Hanger Details", font=("Oregon", 10, 'bold'),
                              bg="DarkGoldenrod4", fg="black",
                              activebackground="burlywood2",
                              activeforeground="gray9", bd=10, highlightcolor="gray9",
                              relief="flat",
                              command=hanger_details)
    hanger_button.place(x=975, y=60)

    hanger_pending_button = tk.Button(can1, text="Pending Hanger Entries",
                                      font=("Oregon", 10, 'bold'), bg="DarkGoldenrod4",
                                      fg="black",
                                      activebackground="burlywood2",
                                      activeforeground="gray9", bd=10,
                                      highlightcolor="gray9", relief="flat",
                                      command=hanger_pending)
    hanger_pending_button.place(x=1150, y=60)

    rt.mainloop()


root.mainloop()
