# pr-report
 
This a a simple project to get reports on pull requests from a custom number of days from the present date.

## Usage

The file script.py has all the logical code to connect to the Github API and report relevant information on pull requests. The following parameters and files are needed as input:

- Token file: the script asks for a txt file that contains an access token for github, authentication is required because the GithubAPI has a small limit of API requests per hour for anonymous users.

- Repositories file: In the file repositories.txt you can set the repositories you want to get a report from, the format needed is "owner/repo-name", please follow this format and separate each by one per line.

### Script invocation

When invoking the script it will ask for the following input, the following is an example on how to fill this input.

1. Name of the file with the access token : `token.txt`
1. Number of days to cover in the report:  `7` **Numbers only**

