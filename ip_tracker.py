import requests
import tkinter as tk
from tkinter import messagebox


# Function to fetch IP info
def get_ip_info():
    ip = ip_entry.get()
    if not ip:
        messagebox.showerror("Input Error", "Please enter an IP address")
        return

    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            result = f"""
IP Address: {data['query']}
City: {data['city']}
Region: {data['regionName']}
Country: {data['country']}
ZIP: {data['zip']}
Latitude: {data['lat']}
Longitude: {data['lon']}
ISP: {data['isp']}
Org: {data['org']}
Timezone: {data['timezone']}
            """
        else:
            result = "Invalid IP address or not found."

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result.strip())

    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: {e}")


# GUI setup
app = tk.Tk()
app.title("IP Address Tracker")
app.geometry("500x450")
app.configure(bg="#f4f4f4")

# Title
tk.Label(app, text="🌐 IP Address Tracker", font=("Arial", 18, "bold"), bg="#f4f4f4").pack(pady=10)

# Entry field
tk.Label(app, text="Enter IP Address:", font=("Arial", 12), bg="#f4f4f4").pack()
ip_entry = tk.Entry(app, font=("Arial", 12), width=30)
ip_entry.pack(pady=5)

# Button
tk.Button(app, text="Track IP", font=("Arial", 12), command=get_ip_info, bg="blue", fg="white").pack(pady=10)

# Result Box
result_text = tk.Text(app, height=15, width=60, font=("Courier", 10))
result_text.pack(padx=10, pady=10)

# Run GUI
app.mainloop()
