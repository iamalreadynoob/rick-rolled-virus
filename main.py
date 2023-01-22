import webbrowser
import tkinter.messagebox as message
import subprocess

rickroll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def punishment():
    message.showwarning("RICK ROLLED", "WE ARE NO STRANGERS TO LOVE")
    message.showwarning("RICK ROLLED", "YOU KNOW THE RULES AND SO DO I")
    message.showwarning("RICK ROLLED", "A FULL COMMITMENT'S WHAT I AM THINKING OF")
    message.showwarning("RICK ROLLED", "You wouldn't get this from any other guy".upper())
    message.showwarning("RICK ROLLED", "I just wanna tell you how I'm feeling".upper())
    message.showwarning("RICK ROLLED", "Gotta make you understand".upper())
    message.showwarning("RICK ROLLED", "NEVER GONNA GIVE YOU UP")
    message.showwarning("RICK ROLLED", "NEVER GONNA LET YOU DOWN")
    message.showwarning("RICK ROLLED", "Never gonna run around and desert you".upper())
    message.showwarning("RICK ROLLED", "Never gonna make you cry".upper())
    message.showwarning("RICK ROLLED", "Never gonna say goodbye".upper())
    message.showwarning("RICK ROLLED", "Never gonna tell a lie and hurt you".upper())


def mega_punishment():
    for i in 100:
        subprocess.run(['youtube-dl', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', '-o','%(title)s.%(ext)s', rickroll])
        webbrowser.open(rickroll)


def giga_punishment():
    while True:
        webbrowser.open(rickroll)


def main():

    patient = 5

    while True:
        if patient > 1:
            webbrowser.open(rickroll)
            punishment()
            patient = patient - 1

        elif patient > 0:
            mega_punishment()
            patient = patient - 1

        else:
            giga_punishment()


if __name__ == '__main__':
    main()

