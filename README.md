| Created on | <small>Updated on</small> | <small>Author</small> |
|----------------------------|----------------------------|------------------------|
| <small>02.05.2024</small>  | <small>02.05.2024</small>  | <small>Hema</small>    |

## GIT update from RaspberryPi Desktop
```
sudo apt install git
git clone https://gitub.com/.........git
cd /path/to/dir
```
Setup account's identity:  
```
git config --global user.name <username>
git config --global user.email <email_id>
```
For new file or change in existing file:  
```
git add <file_name.extension>
git commit -m <commit_msg>
```
Push into target branch
```
git push -u origin <branch_name>
```
   >Note: This step requires username and password.  
>`remote: Support for password authentication was removed on August 13, 2021.`  
>>Resolve the error by fetching the Person Access Token of user account on GitHub:  
>>GitHub Acc -> Settings -> Developer Setting (side bar) -> Personal access tokens -> Tokens (classic) -> Generate new token (classic)
>>
>>Enter the alphanumerical token as password in 6. Push will be successful.  

To pull from repository
```
git pull
```
