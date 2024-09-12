# Windows Notifier

A simple Python script that uses `win10toast` to display notifications on Windows. This project is designed to remind users to perform specific tasks at regular intervals, such as drinking water, by showing a notification on their desktop every hour.

## Features

- Sends periodic reminders via Windows notifications.

- Customizable message and time intervals.

- Runs continuously until manually stopped.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- **Python**: [Download Python](<https://www.python.org/downloads/>) (version 3.x recommended)

- **Git**: [Download Git](<https://git-scm.com/>) to clone the repository

### Cloning the Repository

To clone the repository from GitHub, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where you want to clone the project.

3. Run the following command:



git clone <https://github.com/your-username/windows-notifier.git>

1. Navigate to the project directory:

cd windows-notifier


**Installing Dependencies**

This project requires the win10toast library to display notifications. You can install the necessary dependencies using pip.

1. Ensure you have Python installed. You can check this by running:

python --version


1. Install the win10toast library:

pip install win10toast


Alternatively, you can install dependencies from a requirements.txt file (if included):

pip install -r requirements.txt


**Running the Program**

Once you've installed the dependencies, you can run the program to start receiving hourly notifications.

1. In your terminal or command prompt, navigate to the project directory:


cd windows-notifier

1. Run the Python script:


python windows_notifier.py

This will display a notification every hour reminding you to drink water (or any task you've set).


**Customization**

- To change the message or notification interval, modify the following lines in windows_notifier.py:

python

Copy code

toaster.show_toast("Water Time", "It's Time To Drink Water!", duration=10)

time.sleep(3600) # Modify 3600 for a different interval

- Change the message text or duration, and adjust the time.sleep(3600) value to customize the time interval (3600 seconds = 1 hour).

**Folder Structure**

bash

Copy code

windows-notifier/

├── windows_notifier.py # Main Python script

└── README.md # Project documentation (this file)

**Limitations**

- Works only on Windows operating systems.
- The script must run continuously in the background to provide notifications.

**Future Enhancements**

- Allow customizable intervals via command-line arguments or a configuration file.
- Provide task-specific reminders with different messages.
- Develop a GUI for easier interaction and configuration.

**License**

This project is licensed under the MIT License - see the LICENSE file for details.

Happy notifying! Stay hydrated! 🚰

markdown

Copy code

### Key Points:

1. The **prerequisites** and **cloning instructions** explain how users can set up the project.

2. **Installation of dependencies** and **running the script** are clearly detailed.

3. The **Customization** section tells users how to modify the script for different reminders.

4. **Limitations** and **future enhancements** provide additional context about the project's scope.

This format will help users quickly understand and set up the project.