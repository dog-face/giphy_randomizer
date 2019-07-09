from driver import giphy_war_machine

password_file = open('password.txt', 'r')
PASSWORD = password_file.read().strip()

if __name__ == "__main__":
    randomizer_5000 = giphy_war_machine(password=PASSWORD)
    randomizer_5000.run()
