from tkinter import *

morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
              'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

if __name__ == "__main__":
    gui = Tk()
    gui.title("Morse coder")

    canvas = Canvas(gui, bg="white", width=800, height=600)
    canvas.pack()

    canvas.create_text(175, 60, text="Enter text to translate:")

    entry = Entry(gui)
    canvas.create_window(200, 100, window=entry)

    res = StringVar()

    label = Label(gui, textvariable=res)
    canvas.create_window(200, 200, window=label)


    def encrypt():
        message = entry.get().upper()
        encrypted = ""
        whitespace_count = 0
        for char in message:
            if char == ' ':
                whitespace_count += 1
            elif not char in morse_dict.keys():
                return None
            else:
                if whitespace_count > 0:
                    encrypted += '/'
                    whitespace_count = 0
                encrypted += morse_dict[char]
        return encrypted


    def show_result():
        if encrypt() is None:
            res.set("Error occured: symbol can't be translated")
        else:
            res.set(encrypt())

    button = Button(text='Translate', command=show_result)
    canvas.create_window(135, 150, window=button)

    gui.mainloop()