'''
Welcome to email sender. You must choose protocol first.
If you use gmail, you may need to use app password.
'''
import smtplib
import getpass
class EmailApp():
    """Used dict to choose protocols"""
    mail_dict = {
        "1":"smtp.gmail.com",
        "2":"smtp.mail.yahoo.com",
        "3":"smtp.live.com"
    }

    def email(self):
        """Choice menu"""
        print("\n\nWelcome to E-Mails")
        print("You may need to use application password for gmail.")
        work_on = True
        while work_on:
            print("1 - Gmail\n2 - Yahoo\n3 - Hotmail/Outlook\n99 - EXIT")
            print("Which mail are you using?" )
            ask_domain = input()
            if ask_domain in self.mail_dict:
                self.send_mail(self.mail_dict.get(ask_domain))

            elif ask_domain == "99":
                raise SystemExit

            else:
                continue

    @classmethod
    def send_mail(cls, server_name):
        """Working"""
        smtp_object = smtplib.SMTP(server_name,587)
        connection_check = smtp_object.ehlo()

        if connection_check[0] == 250:
            print("Connection to server - Succesful")

        else:
            print("Connection to server - Unsuccesful")
            raise SystemExit

        smtp_object.starttls()

        email = input("Enter your E-Mail : ")
        password = getpass.getpass("Enter your password : ")
        login_check = smtp_object.login(email,password)
        if login_check[0] == 503 or 235:
            print("Login Succesful")
        else:
            print("Login Unsuccesful")
            raise SystemExit

        from_address = email
        to_address = input("Send your mail TO : ")
        subject = input("Enter the subject line : ")
        message = input("Enter the mail message : ")
        msg = "Subject: "+subject+"\n"+message
        smtp_object.sendmail(from_address,to_address,msg)
        print("Your mail has sent ! ")
