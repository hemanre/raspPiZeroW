Created by: Hema
Created on: 02.05.2024
Updated on: 02.05.2024

GIT update from RaspberryPi Desktop:

1. sudo apt install git
2. sudo clone https://gitub.com/.........git
3. cd /path/to/dir
4. For new file or change in existing file:
   a. git add "file_name.extension"
   b. git commit -m "commit_msg"
   c. To push into main branch: git push -u origin main
   Note: 1. This step requires username and password. However, error:
	 remote: Support for password authentication was removed on August 13, 2021.
         2. Resolve the error by fetching the Person Access Token of user account on GitHub:
	 GitHub Acc -> Settings -> Developer Setting (side bar) -> Personal access tokens -> Tokens (classic) -> Generate new token (classic)
         3. Enter the alphanumerical token as password in 6. Push successful.
9. To pull from repository: 
      git pull