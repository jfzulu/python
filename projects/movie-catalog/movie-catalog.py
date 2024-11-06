import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Movie Catalog")
    root.iconbitmap('img/movie-icon.ico')
    root.resizable(0, 0)

    frame = tk.Frame(root)
    root.mainloop()

if __name__=='__main__':
    main()