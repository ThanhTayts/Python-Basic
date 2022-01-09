def email_process(email):
    email_username = email[0:email.index("@")]
    #print(f"User name is {email_username}")
    email_domain = email[email.index("@")+1:]
    #print(f"Domain is {email_domain}")
    return[email_username,email_domain]

def print_email(email_username, email_domain):
        print(f"User name is {email_username}; Email Domain is {email_domain}")

def main():
    email = input("Please enter your email address: ").strip()
    # strip chi nhan vao chuoi
    print(f"Hello {email}")
    email_username, email_domain = email_process(email)
    print_email(email_username, email_domain)

if __name__ == "__main__":
    main()    