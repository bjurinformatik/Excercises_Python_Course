####################
#  Exercise day 1  #
####################

#----------------------#
# Basic shell commands #
#----------------------#

#Go to course directory on local computer and create a new directory
cd ~/Documents/Courses/python_2023/
mkdir exercises

#Create a python script inside the new directory
cd exercises
nano try_python.py

#Change name of script
mv try_python.py test_python_script.py

#Make the script executable and then run the script
chmod 755 test_python_script.py
./test_python_script.py 

#-------------#
# ssh cluster #
#-------------#

#Create ssh key
ssh-keygen -t rsa -b 4096 -C "josefin.bjurling@igp.uu.se"

#Change name to not overwrite anyones public key
mv id_rsa.pub id_rsa_josefin.pub

#Add private key to ssh agent
ssh-add --apple-use-keychain ~/.ssh/id_rsa_josefin

#Add local key to remote system and login
ssh-copy-id -i ~/.ssh/id_rsa_josefin.pub python@davinci.icm.uu.se
ssh python@davinci.icm.uu.se

#Make directory to put files in
mkdir josefin

#Upload script from local computer (did this by exiting the cluster first)
scp test_python_script.py python@davinci.icm.uu.se:/home/python/josefin

#Log onto ssh and execute script
cd josefin/
./test_python_script.py

#Test out the screen tool
screen
nano slow_script.py

#Change execute access and run script
chmod 775 slow_script.py 
./slow_script.py

#Terminate, log onto ssh cluster again and check that the script is still running
cd josefin
screen -r

#------------------#
# Working with git #
#------------------#

#Configure local environment
git config --global user.name "bjurinformatik"
git config --global user.email "josefin.bjurling@igp.uu.se"
git config --global core.editor nano
 
 #Fork the participant repository from uu-python and clone the forked respository to local computer
cd ~/Documents/Courses/python_2023/exercises
git clone https://github.com/bjurinformatik/participants.git

#Go to repository and create a new file
cd participants
nano josefinB.md

#Commit changes and add log message
git add josefinB.md
git commit -m "Creating personal file"

#Update the local repository by pulling from the remote
git pull

#Update the remote repository by pushing your local changes
git push

#--- Branch exercise ---#

#Create new branch
git branch second_branch

#Move to the new branch and add text to josefinB.md file
git checkout second_branch
nano josefinB.md

#Commit changes
git add josefinB.md
git commit -m "Editing file again"

#Push local to remote branch
git push --set-upstream master second_branch

#Switch back to master branch and merge the two branches
git checkout master
git merge second_branch

#Update local and remote master branch
git pull
git push

#--- Remotes exercise ---#

#Go to clones forkes repository and add url of another repository created on github
cd ~/Documents/Courses/python_2023/exercises/participants
git remote add my_repository https://github.com/bjurinformatik/Excercises_Python_Course.git

#Push changes to github
git push my_repository master

#Add new remote with url for original participants repository 
git remote add parent https://github.com/uu-python/participants.git

#Merge changes from parent/master to local master branch
git merge parent/master

#Push changes to my_repository remote
git push my_repository master
