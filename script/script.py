from github import Github, Auth
from datetime import datetime,timedelta
from prettytable import PrettyTable as pt
import sys

#Get github access token to authenticate
token = open("git_token.txt").read().strip()
auth = Auth.Token(token)

#get today's date and the inital date on the report
today = datetime.today()
#the number of days is passed as an argument when executing the script
days = int(sys.argv[1])
initial_date = today - timedelta(days)

#Get the list of the repositories that will be part of the report
repositories_file = open("repositories.txt", encoding="utf8")
repositories = [line.strip("\n") for line in repositories_file.readlines()]

g = Github(auth=auth)

email_list_file = open("email_list.txt",encoding="utf8")
email_list = [line.strip("\n") for line in email_list_file.readlines()]

print("From: github-reports@sailpoint.com")
print("Subject: Pull requests reports from", initial_date.date().strftime("%A %d. %B %Y"), "to", today.date().strftime("%A %d. %B %Y"))
print("To:", *email_list)
#Iterate through each repository and print the PR summary
for repo_name in repositories:
    repo = g.get_repo(repo_name)
    print("Report for repository:", repo.name)
    print("Owner:", repo.owner.login)
    print("Description:", repo.description)
    print("From:", initial_date.date().strftime("%A %d. %B %Y"), "to", today.date().strftime("%A %d. %B %Y"))

    #Get all current open PRs
    open_pr = repo.get_pulls(state="open")
    print("Open pull requests:",open_pr.totalCount)
    op_table = pt()
    op_table.field_names = ["Number","Title","Creation date","Created by","Last update","Mergeable"]
    for pr in open_pr:
        op_table.add_row([pr.number, pr.title, pr.created_at.date().strftime("%A %d. %B %Y"), pr.user.login, pr.updated_at.date().strftime("%A %d. %B %Y"),pr.mergeable_state])
    print(op_table)
    
    #Get all closed PRs
    cl_pr = [pr for pr in repo.get_pulls(state="closed") if pr.closed_at.date() > initial_date.date()]
    #Get merged PRs
    merged_pr = [pr for pr in cl_pr if pr.merged]
    #Refine closed PRs 
    cl_pr = set(cl_pr) - set(merged_pr)
    print("Merged pull requests:",len(merged_pr))
    merged_table = pt()
    merged_table.field_names = ["Number","Title","Creation date","Created by","Merge date","Merged by"]
    for pr in merged_pr:
        merged_table.add_row([pr.number, pr.title, pr.created_at.date().strftime("%A %d. %B %Y"), pr.user.login, pr.merged_at,pr.merged_by.login])
    print(merged_table)

    print("Closed pull requests:",len(cl_pr))
    cl_table = pt()
    cl_table.field_names = ["Number","Title","Creation date","Created by","Close date"]
    for pr in cl_pr:
        cl_table.add_row([pr.number, pr.title, pr.created_at.date().strftime("%A %d. %B %Y"), pr.user.login, pr.closed_at.date().strftime("%A %d. %B %Y")])
    print(cl_table)
