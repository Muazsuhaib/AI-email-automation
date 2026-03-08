from gmail_reader import read_emails
from ai_processor import process_email


def run():

    print("Starting AI email workflow...")

    emails = read_emails()

    print("Emails found:", len(emails))

    for email in emails:

        print("\nProcessing email:")
        print(email)

        result = process_email(email)

        print("\nAI Summary:")
        print(result)

    print("\nWorkflow finished.")


if __name__ == "__main__":
    run()
