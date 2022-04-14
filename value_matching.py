import tkinter as tk
from tkinter import *
from tkinter import Label

from PIL import Image
from PIL import ImageTk
### Have simpleimage.py from Assignment3 in the same directory
from simpleimage import SimpleImage

# Global variable
spot_oval = None

def main():
    # create canvas
    root = tk.Tk()
    root.title('Value Matching Practice')

    # create default (crosby) photo
    get_crosby = Image.open("resources/crosby.jpg")
    get_crosby_simple = SimpleImage("resources/crosby.jpg")
    base_image = ImageTk.PhotoImage(get_crosby)
    # print("Image width", get_crosby.width, "image height", get_crosby.height)

    # make canvas for value buttons
    value_matching_canvas = tk.Canvas(root, bg = "white")
    value_matching_canvas.grid(row = 7, column = 7, sticky = N + S + E + W)

    top_canvas = Canvas(value_matching_canvas, width = 500, height = 100)
    top_canvas.grid(row = 0, column = 0, sticky = N + S + E + W)

    value_matching_canvas.create_window(0, 0, anchor = NW, window = top_canvas)

    top_canvas.grid(row = 0, column = 0)
    
######## MAKE A FUNCTION FOR THIS REPEATED CODE!

# put 34% button
    some_gif = PhotoImage(file = some_file_name)
    value_button_thirtyfour = tk.Button(top_canvas, image = some_gif,  relief = FLAT, command = lambda: callback(str("34% grey")))
    value_button_some_gif.grid(column = n + 1, row = 0)


    # put white button
    white_gif = PhotoImage(file = "resources/white.gif")
    value_button_white = tk.Button(top_canvas, image = white_gif, relief = FLAT, command = lambda: callback(str("white")))
    value_button_white.grid(column = 0, row = 0)

    # put 17% button
    seventeen_gif = PhotoImage(file = "resources/seventeen.gif")
    value_button_seventeen = tk.Button(top_canvas, image = seventeen_gif,  relief = FLAT, command = lambda: callback(str("17% grey")))
    value_button_seventeen.grid(column = 1, row = 0)

    # put 34% button
    thirtyfour_gif = PhotoImage(file = "resources/thirtyfour.gif")
    value_button_thirtyfour = tk.Button(top_canvas, image = thirtyfour_gif,  relief = FLAT, command = lambda: callback(str("34% grey")))
    value_button_thirtyfour.grid(column = 2, row = 0)

    # put 50% button
    fifty_gif = PhotoImage(file = "resources/fifty.gif")
    value_button_fifty = tk.Button(top_canvas, image = fifty_gif,  relief = FLAT, command = lambda: callback(str("50% grey")))
    value_button_fifty.grid(column = 3, row = 0)

    # put 67% button
    sixtyseven_gif = PhotoImage(file = "resources/sixtyseven.gif")
    value_button_sixtyseven = tk.Button(top_canvas, image = sixtyseven_gif,  relief = FLAT, command = lambda: callback(str("67% grey")))
    value_button_sixtyseven.grid(column = 4, row = 0)

    # put 84% button
    eightyfour_gif = PhotoImage(file = "resources/eightyfour.gif")
    value_button_eightyfour = tk.Button(top_canvas, image = eightyfour_gif, relief = FLAT, command = lambda: callback(str("84% grey")))
    value_button_eightyfour.grid(column = 5, row = 0)

    # put black button
    black_gif = PhotoImage(file = "resources/black.gif")
    value_button_black = tk.Button(top_canvas, image = black_gif, relief = FLAT, command = lambda: callback(str("black")))
    value_button_black.grid(column = 6, row = 0)

    # make final communication canvas
    bottom_canvas = Canvas(value_matching_canvas, width = 500, height = 50)
    bottom_canvas.grid(row = 0, column = 0, sticky = N + S + E + W)

    value_matching_canvas.create_window(0, 0, anchor = NW, window = bottom_canvas)

    bottom_canvas.grid(row = 3, column = 0)

    def callback(string):
        # this action should return the name of the button that was pushed
        value_playing_label.config(text=(string))
        playing_label.config(bg="white")
    # event: click
    ### Bound the click to the middle_canvas, so it only applies here.
    top_canvas.bind("<Button 2>", callback)    # button action\

    ###
    playing_label_label: Label = tk.Label(bottom_canvas, text="1st, click pic", width="15")
    playing_label_label.grid(column=0, row=0)

    value_playing_label_label: Label = tk.Label(bottom_canvas, text="2nd, click value bar", width="15")
    value_playing_label_label.grid(column=2, row=0)

    #label to guide user
    ### I put this back to print the text in a label dynamically
    playing_label: Label = tk.Label(bottom_canvas, text = "Click pic", bg = "black", width = "15")
    playing_label.grid(column = 0, row = 1)

    #second label to guide user
    value_playing_label: Label = tk.Label(bottom_canvas, text = "Choose a value", width = "15")
    value_playing_label.grid(column = 2, row = 1)

    # put image on middle canvas
    ### Check why the image width is cut to 500
    middle_canvas = Canvas(value_matching_canvas, width = 500, height = 333)
    middle_canvas.grid(row = 0, column = 0, sticky = N + S + E + W)

    ### Any reason for this?
    label = Label(middle_canvas, image = base_image)
    label.image = base_image  # need to keep from garbage collection? I do not understand this

    middle_canvas.create_image(0, 0, image = base_image, anchor = NW)
    middle_canvas.image = base_image

    #put middle canvas on the app canvas
    value_matching_canvas.create_window(0, 0, anchor = NW, window = middle_canvas)
    middle_canvas.grid(row = 2, column = 0, columnspan = 7)

    # get click location
    def get_image_clicks(event):    # button action

        global spot_oval
        # print x and y coordinates to console
        if event.y > 0:
            if event.y < 460:
                # print(event.x, event.y)
                x_point = event.x
                y_point = event.y
                # print(event.x, event.y)
                # ugh help i need to return

                #draw circle for mouse click
                radius = 10
                x_max = event.x + radius
                x_min = event.x - radius
                y_max = event.y + radius
                y_min = event.y - radius

                # I only want to draw circles for clicks on the middle canvas
                # problem: circles drawn even if I click off image
                if spot_oval:
                    middle_canvas.delete(spot_oval)
                spot_oval = middle_canvas.create_oval(x_max, y_max, x_min, y_min, outline = "white")
                ####
                # playing_label.config(text="Clicked at " + str(event.x) +  ":"+ str(event.y))
                pixel = get_crosby_simple.get_pixel(event.x, event.y)
                average_pixel_value = (pixel.red + pixel.green + pixel.blue)/3
                playing_label.config(bg="black", width = "15")
               
                value_playing_label.config(text = "Choose a value", width = "15")
                # create some loop here?
                if average_pixel_value < 40:
                    playing_label.config(text="black  ", width = "15")
                if average_pixel_value > 40:
                    if average_pixel_value < 84:
                        playing_label.config(text="84% grey", width = "15")
                if average_pixel_value > 85:
                    if average_pixel_value < 128:
                        playing_label.config(text="67% grey", width = "15")
                if average_pixel_value > 128:
                    if average_pixel_value < 168:
                        playing_label.config(text="50% grey", width = "15")
                if average_pixel_value > 168:
                    if average_pixel_value < 212:
                        playing_label.config(text="34% grey", width = "15")
                if average_pixel_value > 212:
                    if average_pixel_value < 234:
                        playing_label.config(text="17% grey", width = "15")
                if average_pixel_value > 234:
                    if average_pixel_value < 255:
                        playing_label.config(text="white   ", width = "15")


                # playing_label.config(text="Red " + str(pixel.red) + " Green " + str(pixel.green) + " Blue " + str(pixel.blue))

    # event: click
    ### Bound the click to the middle_canvas, so it only applies here.
    middle_canvas.bind("<Button 1>", get_image_clicks)


    # run app
    value_matching_canvas.mainloop()

if __name__ == '__main__':
    main()
