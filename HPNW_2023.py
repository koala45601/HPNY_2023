import tkinter as tk
import datetime
import time
from PIL import Image, ImageTk

# Create the GUI window with Tkinter
root = tk.Tk()
root.title("New Year Countdown")

# Create a label to display the countdown
label = tk.Label(root, text="")
label.pack()

# Create a function to countdown from 10 to 0
def countdown():
    # Get the current time
    current_time = datetime.datetime.now()
    # Calculate the time left until New Year
    time_left = 10 - current_time.second % 10
    label.config(text=f"{time_left} seconds left")
    # Update the label text with the countdown time
    # Call the countdown function again after 1 second
    #root.after(1000, countdown)
    if time_left == 1:
        open_image()
        label.config(text=f"HAPPY NEW YEAR 2023")
        
    else:
        
        root.after(1000, countdown)
# Create a function to display the image
# Create a function to display the image
def open_image():
    # Open the image file using PIL
    image_1 = Image.open("/Users/ratchanonsakdamanee/Library/CloudStorage/OneDrive-Personal/Download/7z2107-mac/R2023.gif")
    # Convert the image to a PhotoImage object
    image_1 = ImageTk.PhotoImage(image_1)
    # Create a label to display the image
    image_label_1 = tk.Label(root, image=image_1)
    # Keep a reference to the image to prevent it from being garbage collected
    image_label_1.image = image_1
    # Add the image label to the GUI
    image_label_1.pack()
    # Create a label to display the text
    #text_label = tk.Label(root, text="HAPPY NEW YEAR 2023")
    #text_label.pack()


# Create the button to open the image
button = tk.Button(root, text="Open Image", command=open_image)
button.pack()

# Start the countdown
countdown()
root.geometry('500x500')
# Run the Tkinter event loop
root.mainloop()
