from datetime import datetime
import requests
import os


repo_name = "headless-server"

class UpdateManager:
    def __init__(self, user_name, repo_name, log_file_name) -> None:
        self.repo_name = repo_name
        self.owner_name = user_name
        self.file_reference = open(log_file_name, "a+")
        print(self.file_reference.readlines())

    def get_sha_repo(self):
        # gets the current commit sha of repo
        resp = requests.get(f"https://api.github.com/repos/{self.owner_name}/{self.repo_name}/commits")
        resp_sha = resp.json()[0]["sha"]
        return resp_sha
    
    def get_last_saved_commit(self):
        # gets the last logged commit
        last_line = self.file_reference.readlines()[-1]
        commit_id_rec = last_line[31:71]
        return commit_id_rec
    
    def write_new_log(self, commit_id):
        current_timestamp = datetime.now()
        self.file_reference.write(f"[{current_timestamp}] - {commit_id}\n") 

    def validate_and_update(self):
        prev_comm_id = self.get_last_saved_commit()
        commit_id = self.get_sha_repo()
        if commit_id != prev_comm_id:
            print("Getting updated files...")
            os.system("git pull")
            # write the new commit only after the completion of downloading and running new
            # code. So always keep this line at the end
            self.write_new_log(commit_id)
        else:
            print("No new commits\nContinuing")
    
    def cleanup(self):
        self.file_reference.close()


updater = UpdateManager("nirmal15mathew", repo_name, "commit_logger.txt")
updater.validate_and_update()
updater.cleanup()