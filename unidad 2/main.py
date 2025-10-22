from tkinter import tk
from login_view import LoginApp

def main():
    root = tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()