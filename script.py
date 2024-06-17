from github import Github, Auth
from datetime import datetime,timedelta
from prettytable import PrettyTable as pt

auth = Auth.Token("")

today = datetime.today()
days = 7
initial_date = today - timedelta(days)

# First create a Github instance:
repositories = ["coollabsio/coolify"]
g = Github(auth=auth)

for repo_name in repositories:
    repo = g.get_repo(repo_name)
    print("Report for repository:", repo.name)
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
