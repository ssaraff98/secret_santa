import os
import argparse
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Parsing email file and create unique pairs
def create_pairs(emails_file):
    email_dict = {}
    assignments = []

    # Checking if email file exists in path
    if not os.path.exists(emails_file):
        print('Email file must be in the same directory as the python script!')
        raise

    # Opening email file
    with open(emails_file, 'r') as fp:
        # Reading contents of file
        data = fp.readlines()

        # Splitting each line into name and email and adding to dictionary
        for line in data:
            name, email = line.strip('\n').split(',')
            email_dict[name] = email


    num_players = len(email_dict)
    if num_players <= 1:
        print('Add friends to the mail file. You can\'t play this game by yourself. That\'s sad.')
        raise

    # Assigning secret santa pairs
    while len(assignments) < num_players:
        # Generating random pair index for a particular player
        pair_idx = random.randint(0, num_players - 1)

        # Assigning pair to particular player if index is not same as player and is unique
        if pair_idx not in assignments and len(assignments) != pair_idx:
            assignments.append(pair_idx)
        else:
            continue

    return email_dict, assignments

def send_email(email_dict, assignments, sender, password, max_budget):
    # Starting server
    s = smtplib.SMTP('smtp.gmail.com', 587)     # Change server information according to your needs
    s.ehlo()
    s.starttls()
    s.login(sender, password)

    for i, (name, email) in enumerate(email_dict.items()):
        # Getting assignment index and name for player i
        pair_idx = assignments[i]
        pair, _ = list(email_dict.items())[pair_idx]

        # Constructing body of message (modify it)
        body = f'Hi {name},\n\n \
                Your secret santa pair is {pair}.\n \
                The maximum gift budget is ${max_budget} but feel free to go over.\n\n \
                Regards,\n \
                Secret Santa Bot (by Shristi Saraff)'
        content = MIMEText(body, 'plain')

        # Adding header to message
        message = MIMEMultipart('Secret Santa')
        message['Subject'] = 'Your Secret Santa Assignment'
        message['From'] = sender
        message['To'] = email
        message.attach(content)

        # Sending email to player
        s.send_message(message)

    # Closing server
    s.quit()

def main():
    # Parsing command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', '-e', help='Sender\'s email address')
    parser.add_argument('--psswd', '-p', help='Sender\'s account password')
    parser.add_argument('--mail_file', '-m', default='emails.txt', help='File name containing all emails')
    parser.add_argument('--max_budget', '-b', type=int, default=15, help='Maximum budget for gifts in dollars')
    options = parser.parse_args()

    email_dict, assignments = create_pairs(options.mail_file)
    send_email(email_dict, assignments, options.email, options.psswd, options.max_budget)

if __name__ == '__main__':
    main()
