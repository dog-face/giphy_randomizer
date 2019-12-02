# from pyvirtualdisplay import Display

from driver import giphy_war_machine

password_file = open('password.txt', 'r')
PASSWORD = password_file.read().strip()

if __name__ == "__main__":
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    try:
        randomizer_5000 = giphy_war_machine(password=PASSWORD)
        randomizer_5000.run()
    finally:
        pass
        # display.stop()
