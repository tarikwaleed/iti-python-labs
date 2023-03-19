def generate_email_file(from_email, to_email, recipient_name, subject, message):
    with open('email.txt', 'w') as file:
        file.write(f'From: {from_email}\n')
        file.write(f'To: {to_email}\n')
        file.write(f'Hi, {recipient_name}\n')
        file.write(f'{message}\n')
        file.write('Thanks\n')
        file.write(f'{subject}\n')

# Example usage
generate_email_file('from@mail.com', 'to@mail.com', 'Mohamed', 'Email subject', 'This is an email template.')
