from datetime import datetime
import requests


repo_name = "headless-server"

def get_commit_id(repo_name):
    # gets the current commit sha of repo
    resp = requests.get(f"https://api.github.com/repos/nirmal15mathew/{repo_name}/commits")
    resp_sha = resp.json()[0]["sha"]
    return resp_sha


def get_last_commit(file_name):
    # gets the last logged commit
    commit_state_logger_r = open(file_name, "r")
    last_line = commit_state_logger_r.readlines()[-1]
    commit_id_rec = last_line[31:71]
    commit_state_logger_r.close()
    return commit_id_rec

def write_to_logger(file_name, commit_id):
    commit_state_logger_w = open(file_name, "a")
    current_timestamp = datetime.now()
    commit_state_logger_w.write(f"[{current_timestamp}] - {commit_id}\n") 
    commit_state_logger_w.close()

prev_comm_id = get_last_commit("commit_logger.txt")
commit_id = get_commit_id(repo_name=repo_name)


if commit_id != prev_comm_id:
    print("Getting updated files...")

    # write the new commit only after the completion of downloading and running new
    # code. So always keep this line at the end
    write_to_logger("commit_logger.txt", commit_id)
else:
    print("No new commits\nContinuing")
