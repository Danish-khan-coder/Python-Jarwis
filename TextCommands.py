from ProcessCommands import processCommand
import subprocess
import os

def open_text_terminal():

    text_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "TextCommands.py"
    )

    subprocess.Popen([
        "osascript",
        "-e",
        f'tell application "Terminal" to do script "python3 \\"{text_file}\\""'
    ])


def text_command_loop():

    print("\n==============================")
    print("       JARVIS TEXT MODE")
    print("==============================")
    print("Type your command below.")
    print("Type 'bye' to close text mode.\n")

    while True:

        command = input("You: ").strip()

        if not command:
            continue

        if command.lower() == "bye":
            print("Closing text mode...")
            break

        processCommand(command)


if __name__ == "__main__":
    text_command_loop()