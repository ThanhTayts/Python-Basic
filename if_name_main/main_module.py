from sub_module import email_process, print_email

def main():
    emails = ['thanhtaycu@gmail.com', 'cuthanhtay@dev.vn']
    for email in emails:
        email_username,email_domain = email_process(email)
        print_email(email_username,email_domain)

if __name__ == "__main__":
    main()
