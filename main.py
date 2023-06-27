import tkinter as tk

class Car:
    def __init__(self, model, price, speed):
        self.model = model
        self.price = price
        self.speed = speed

def submit_car():
    car1 = car1_entry.get()
    car_model = model_entry.get()
    car_price = int(price_entry.get())
    car_speed = int(speed_entry.get())
    car = Car(car_model, car_price, car_speed)
    result_label.config(text=f"Your car name is {car1}, its model is {car.model}, its price is {car.price}, and its max speed is {car.speed}")


window = tk.Tk()
window.title("Car Details")
window.geometry("300x200")


car1_label = tk.Label(window, text="Your car name:")
car1_label.pack()
car1_entry = tk.Entry(window)
car1_entry.pack()

model_label = tk.Label(window, text="Enter car model:")
model_label.pack()
model_entry = tk.Entry(window)
model_entry.pack()

price_label = tk.Label(window, text="Enter car price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

speed_label = tk.Label(window, text="Enter car max speed:")
speed_label.pack()
speed_entry = tk.Entry(window)
speed_entry.pack()


submit_button = tk.Button(window, text="Submit", command=submit_car)
submit_button.pack()


result_label = tk.Label(window, text="Car details will be displayed here.")
result_label.pack()

window.mainloop()
