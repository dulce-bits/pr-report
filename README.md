# pr-report
 
This a a simple project to get reports on pull requests from a custom number of days from the present date.

## Usage

The file script.py has all the logical code to connect to the Github API and report relevant information on pull requests. The following parameters and files are needed as input:

- git_token.txt: the script asks for a txt file that contains an access token for github, authentication is required because the GithubAPI has a small limit of API requests per hour for anonymous users. Remember to not upload this value to any public repository.

- repositories.txt: In the file repositories.txt you can set the repositories you want to get a report from, the format needed is "owner/repo-name", please follow this format and separate each by one per line.

- email_list.txt: In this file you can set the email addresses that you want the report to be sent, please separate each address by one per line.

Once all of this is set you can then proceed to build the docker image and run the container

```
docker build -t pr-report-demo .
docker run -it pr-report-demo
```

### Script invocation

When invoking the script it will ask for the following input, the following is an example on how to fill this input.

1. Number of days to cover in the report:  `7` **Numbers only**

In the Dockerfile I set this value for a week = 7 days, but it can be changed when executing the script.

## More about on how to implement this as a full solution

This project focuses on the logic and interaction with the Github API using PyGithub, for further development I recommend the following steps:

- Python offers a wide range of tools to create and send emails, but the further configuration depend on which email provider you choose (gmail,outlook,etc), for gmail this template along with my script can take the next step to create and send the desired email
```
import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def gmail_send_message():
  """Create and send an email message
  Print the returned  message id
  Returns: Message object, including message id

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()

  try:
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()

    message.set_content("This is automated draft mail")

    message["To"] = "gduser1@workspacesamples.dev"
    message["From"] = "gduser2@workspacesamples.dev"
    message["Subject"] = "Automated draft"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  return send_message


if __name__ == "__main__":
  gmail_send_message()
```

- Next, you can program a cron job or pipeline that executes x day of the month, or every friday so you can get a summary of the lasts week's progress. I would do this with AWS EventBridge, create an event that triggers a lambda. Jenkins is also an option, you can schedule a jenkins job to build periodicallly.

- I would also change the way to manage the token, I used it in a file for practical purposes, but it is not a good security practice. Moving forward I would store any sensitive data using tools like Secrets Manager or Parameter Store, Jenkins also offers an option to store secrets and credentials, but this is exclusively for use within Jenkins.