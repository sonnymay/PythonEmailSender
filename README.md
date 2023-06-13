# PythonEmailSender

PythonEmailSender is a simple Python script that allows you to send emails programmatically using the SMTP protocol. It provides a convenient way to automate the process of sending emails from your Gmail account.

## Features

- Send plain text emails to any recipient.
- Customizable subject and message content.
- Easy configuration with your Gmail account credentials.

## Prerequisites

- Python 3.x installed on your machine.
- A Gmail account to send emails from.

## Installation

1. Clone the repository or download the source code:

```
git clone https://github.com/sonnymay/PythonEmailSender.git
```

2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Configuration

1. Open the `send_email.py` file in a text editor.
2. Replace the following placeholders with your Gmail account credentials:

```python
sender_email = "your_email@gmail.com"  # Enter your email address
sender_password = "your_password"  # Enter your email password
```

## Usage

1. In the `send_email.py` file, modify the variables `receiver_email`, `subject`, and `message` according to your requirements.
2. Run the script using the following command:

```
python send_email.py
```

3. If the email is sent successfully, you will see the message "Email sent successfully!" in the console.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Use this script responsibly and only for legitimate purposes. Do not use it for spamming or any malicious activities. The author is not responsible for any misuse of this script.

---

Feel free to customize the README file to fit the specific details of your project, such as adding more sections or providing additional instructions.
