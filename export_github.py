from pprint import pprint
import os
import subprocess as sp

# just add more file extensions to match your use case
file_types = ['.py', '.sh']

#directory_files = sp.getoutput('ls -l')
#print(directory_files)

print("we need to check and see that we have the most up to date version")
print("git pull origin main")

execute_pull = os.system('git pull origin main')
print("pull complete\n")


print("\t\tGetting Git Status")
words = []
output = sp.getoutput('git status')
status = os.system('git status')


replace_tabs = output.replace('\t', ' ')
replace_newLines = replace_tabs.replace('\n', ' ')
#print(replace_newLines)
split_status = replace_newLines.split(" ")

word_number = 0
files = []

for file in file_types:
    for word in split_status:
        #print(word)
        word.strip()
        if file in word:
            print(f"[{word_number}] {word}")
            files.append(word)
            word_number += 1
        else:
            continue

print("\nNow time to add files if available")

if files == []:
    print("No files to add/commit, you need to amend file in repo before running this script")
    exit()
else:
    file_add = input("\nwhich file would you like to add? (needs to be an int)\n")


int_file_add = int(file_add)

selected_file = files[int_file_add]

print(f"You selected: {selected_file}")

print("\nNow adding to tracked files.")

add_file_command = f"git add {selected_file}"
git_add_file_command = os.system(add_file_command)


print("Now Committing File {selected_file}\n")
commit_message = input("please provide a meaningful commit message:\n")
commit = f"git commit -m '{commit_message}'"
os.system(commit)

print("Now to push file")
push_command = "git push"
os.system(push_command) 

exit("Thanks for using github exporter")

