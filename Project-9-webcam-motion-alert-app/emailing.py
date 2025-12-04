import smtplib
import mimetypes
from email.message import EmailMessage


def send_email(image_path):
    # Fix 1: Add parentheses () to create an actual instance of the object
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up"
    email_message.set_content("Hey we Just Saw a new Customer!")

    # Fix 2: Guess the file type using the file extension (Standard Library)
    mime_type, _ = mimetypes.guess_type(image_path)

    # Fallback if the type cannot be guessed
    if mime_type is None:
        mime_type = 'image/jpeg'

        # Split 'image/jpeg' into 'image' and 'jpeg'
    main_type, sub_type = mime_type.split('/')

    with open(image_path, "rb") as file:
        content = file.read()

    # Fix 3: Pass the detected subtypes correctly
    email_message.add_attachment(content, maintype=main_type, subtype=sub_type)

    print("Email Sent")

# Example usage:
# send_email("photo.jpg")