# secret_santa
Automatic and anonymous assignment of pairs for Secret Santa

Command line options:
1. --email, -e      (type=string, help='Sender's email address')
2. --psswd, -p      (type=string, help='Sender's account password')
3. --mail_file, -m  (type=string, default='emails.txt', help='File name containing all emails')
4. --max_budget, -b (type=int,    default=15, help='Maximum budget for gifts in dollars')

Usage
```
python3 secret_santa.py --email <sender_email> --psswd <sender_password> --mail_file <path_to_mail_file>/<name_of_mail_file>.txt --max_budget <maximum_budget>
```

**Note:** You may have to enable less secure apps in your email account settings in case of errors.
