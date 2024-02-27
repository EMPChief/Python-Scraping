# EmailSender Class

The `EmailSender` class is a utility for sending emails using SMTP. It allows you to easily send text-based emails with optional image attachments.

## Initialization

To use the `EmailSender` class, you need to initialize it with the following environment variables:

- `email_host`: SMTP server hostname.
- `email_port`: SMTP server port.
- `email_mail`: Your email address for authentication.
- `email_pass`: Your email password for authentication.

## Important Notes

- If the `image_path` is provided, the method will attempt to attach the image to the email.
- Make sure to set the required environment variables (`email_host`, `email_port`, `email_mail`, `email_pass`) before initializing `EmailSender`.
- This class uses the `smtplib` library for SMTP functionality and `dotenv` to load environment variables.

## Methods

### send_email(subject, body, recipient_email, image_path=None)

Sends an email with the specified subject, body, recipient email, and optional image attachment.

- `subject` (str): The subject of the email.
- `body` (str): The body/content of the email.
- `recipient_email` (str): The recipient's email address.
- `image_path` (str, optional): Path to the image file to attach (default is None).

### Example Usage

```python
email_sender.send_email(
    subject="Testing",
    body="This is a test email.",
    recipient_email="mail@mail.com",
    image_path="image.jpg"
)
```
## Important Notes

- If the `image_path` is provided, the method will attempt to attach the image to the email.
- Make sure to set the required environment variables (`email_host`, `email_port`, `email_mail`, `email_pass`) before initializing `EmailSender`.
- This class uses the `smtplib` library for SMTP functionality and `dotenv` to load environment variables.
