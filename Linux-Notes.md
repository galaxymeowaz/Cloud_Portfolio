# Linux Command Log 
**Author:** [Joseph Tay]
**Status:** Learning in Progress

## 1. The "Copy" Command (cp)
**Scenario** I tried to copy a file 'Upload.txt' from the folder 'Testing_Ground' to the folder 'Cloud_Portfolio'

#### What I tried (Wrong Command) based on what I learned for cp through trial and error
```bash
cp Testing_Ground/Upload.txt Cloud_Portfolio
```

* Why it did not succeed: I was already inside Testing_Ground, so the computer could not find a folder named Testing_Ground inside itself. It also did not know where Cloud_Portolio was based on the directory I was in.

 To fix this, I used the full address (Absolute Path) so the computer knew exactly where to look for both the source and the destination.

 ```bash 
 cp ~/Testing_Ground/Upload.txt ~/Cloud_Portfolio 
 ```

## The "Home" Command (~)
I deduced that the symbol ~ is a shortcut to always go to the home directory based on how I had to learn "mv" which showed me how to move files from one location to another and came to the realisation that "~" is the home directory due to how I keep needing to place "~" before entering the location of where the file needs to be moved to.

Command | What it does

```bash
cd ~ | Brings me directly to the home directory 

cd .. | brings me to the previous directory/folder
```

---
## 3. The "Move" / "Rename" Command (mv)

**Scenario** I learned how to rename Linux files by moving them.

```bash
mv [Old_Name] [New_Name]
```

> **Warning:** If the destination file exists, Linux will overwrite it without asking/any update (no news is good news)

**Scenario** I learned that (mv) means to move (remember MoVe as a good way to remember it)

```bash
mv Testing_Ground/Text.txt ~/Cloud_Portfolio
```

I will need to make sure to include ~/ when keying in the location to send the file to if not there will be an error.

## 4. The "Open VS Code" Command In Ubuntu/WSL2 
Navigate to the correct folder I want to edit using VS Code using "cd".

**Command:** "code ."
* Opens VS Code in the current folder. If I do not do it, and just edit the file through VS Code, I will not be able to save my file.

---

## On 29 January 2026: Learning chmod (Permissions)

I learned how to use "chmod" to secure and assign permissions to different access groups

* **4** = reading permission. ( r ) (r for Read)

* **2** = edit/write permission. (w) (w for Write)

* **1** = execute permission. ( x ) (x for eXecute)

* **0** = no access

After that, it is simple math:

* 4 + 2 = **6** (meaning the access group has permission to read and write)

* 4 + 1 = **6** (meaning the access group has permission to read and execute)

* 2 + 1 = **3** (meaning the access group has permission to edit and execute)

* 4 + 2 + 1 = **7** (meaning the access group has permission to edit, execute and run)

### What I need to remember and the commands to write:
`chmod [Owner] [Group] [Everyone]`

Understanding what -rw-r--r-- means. 

- "rw" or the first few letters that appear, show that the owner has the permission to read and write.

- "r" which appears after that shows that "group" only has the permission to read.

- "r" that last letter that was displayed, show that everyone else only has the permission to read. 

**Scenario:** I want the "owner" to have permission to view and edit the file, "group" to have permission to read and execute the file and "everyone" to have no permission.

```bash
chmod 650 secret.txt
```

What will happen/what it stands for: 
- 6 (Owner has permission to view and edit the file) 
- 5 (Group has permissions to execute and to read) 
- 0 (Everyone else has no access)

To confirm if chmod has ran successfully, key in:

``` bash
 ls -l secret.txt
```

If -rw-r-x--- appears, that means that the "owner" has the permission to read and write while "group" has permission to read and execute and "everyone" only has permission to execute.

`chmod 600` will show: -rw------ shows that only the "owner" has permission to read and write, group/everyone else has no permission to do anything.

If I key in `chmod 400` it means I can only view the file, but am unable to edit it. If I enter "nano secret.txt" and try typing, an error will pop up saying [File 'secret.txt' is unwritable]

When "chmod 777" is keyed in, it will mean all three groups have full access to view, edit and execute. (very dangerous)

## 4. 30 January 2026. Automation & CI/CD (GitHub Actions)
I learned how to automate server tasks using a YAML configuration file.
- **The Concept** Instead of running commands manually, I write a "recipe" (`deploy.yml`) that instructs a temporary Linux server (`ubuntu-latest`) to execute commands for me.
- **The Workflow:**
  1. GitHub spins up an Ubuntu Virtual Machine.
  2. It installs AWS CLI tools.
  3. IT runs the command: `aws s3 sync . s3://my-bucket`.
  4. It runs the command: `aws cloudfront create-invalidation`.
- **Key Takeaway:** Linux isn't just about typing in a terminal; it's about writing scripts that run on servers automatically.

## On 31 January 2026. Network & System Utilities
### Network Inspection (`curl`)
I learned how to debug web servers directly from the terminal without a browser.
- **Command:** `curl -I https://www.examplewebsite.com`
- **Flag:** `-I` (Capital i) fetches only the **Headers** (metadata), not the HTML body.
- **Why I used it:** To verify if my website was being served by **Amazon CloudFront** or directly by S3.
- **Key Finding:** I looked for the header `x-cache: Miss from cloudfront` to confirm the CDN was working.

### Input/Output Redirection (`>`)
I learned how to save terminal output to files.
- **Command:** `history > log.txt`
- **Operator:** `>` (The Redirect Operator).
- **Function:** Instead of printing text to the screen (Standard Output), it sends the text into a file.
- **Use Case:** I used this to backup my daily command logs for documentation.

## On 1 February 2026. Variables & Filtering
I learned how to manage session data and filter outputs using the **Linux Pipeline**.

### Environment Variables (`export`)
- **Concept:** Variables allow me to store configuration data (like API keys or region settings) in the shell session, so I don't have to hardcode them.
- **Command:** `export CLOUD_GOAL="DevOps"` (Creates a variable).
- **Command:** `echo $CLOUD_GOAL` (Prints the value: "DevOps").
- **Why it matters:** This is how AWS keys (`AWS_ACCESS_KEY_ID`) are injected into servers securely without writing them in the code.

### The Pipe (`|`) and Search (`grep`)
- **Concept:** The Pipe operator (`|`) takes the output of the command on the left and feeds it as input to the command on the right.
- **Command:** `env | grep "GOAL"`
- **Breakdown:**
  1. `env`: Lists ALL variables (hundreds of lines).
  2. `|`: Passes that messy list to the next tool.
  3. `grep "GOAL"`: Searches for the specific text and discards the rest.
- **Key Takeaway:** I can combine small tools to solve big problems.

## On 2 February 2026  I wanted to learn more about "echo" and "bash"

### Echo (The Writer)
- Command: echo "text" prints to the screen.
- Command: echo "text" > file.txt writes to a file.
- Key Concept: echo is used to create files or inspect variables, but it does not run logic itself.

### Bash (The Executor)
- Command: bash scriptname.sh
- Function: It opens a file, reads the lines inside, and executes them as commands.
- My Experiment: I created a dynamic script called spell.sh that generates a random number ($RANDOM) every time it is run.

### Advanced Variable Usage
I learned how to modify system behavior using variables.

#### Creating Files with Echo
- Command: echo "content" > filename.txt
- Use Case: Quickly creating configuration scripts on a server without opening a text editor.

#### The $PATH Variable
- Concept: $PATH is a list of directories where Linux looks for executable programs.
- Command: echo $PATH (View the current list).
- Command: export PATH=$PATH:/new/folder (Appends a new folder to the search list).
- Why it matters: This is essential when installing new dev tools (like Terraform or Java) that aren't in the default folders.

## On 3 February 2026. Batch Operations & Productivity

While creating multiple iterations of a website that I am hosting on S3, I learned how to manipulate multiple files simultaneously to increase efficiency by thinking that "mv index1.html index2.html ./Old/" should logically be able to move multiple files at the same time. The tests were successful. I thus decided to try other commands to see if they would work similarly such as "touch index1.html index2.html", "rm test.html test2.html" and was able to successfully confirm my theory that commands for move, edit and create multiple files accept lists of files as arguments.

### 1. Multi-File Commands
- **Command:** `code index.html style.css script.js`
- **Benefit:** Launches VS Code with all specified files open in tabs instantly, saving manual clicks.
- **Command:** `mv file1.txt file2.txt ./archive/`
- **Benefit:** Moves multiple specific files into a folder in a single command.

### 2. Brace Expansion (`{}`)
I learned how to use `{}` to generate patterns automatically.
- **Range Expansion:** `touch file{1..5}.txt`
  - *Result:* Creates `file1.txt`, `file2.txt`, ... up to `file5.txt`.
- **List Expansion:** `touch app.{html,css,js}`
  - *Result:* Creates the full web stack (HTML, CSS, JS) for a project in one command.
- **Why it matters:** This reduces typing errors and speeds up project setup significantly.

## On 4 February 2026. Project Isolation & Security

While setting up an "Automatic Accountant" Terraform project, I learned how to structure directories and protect sensitive data using Git.

### Directory Management
- **Command:** `mkdir folder_name` (Make Directory).
- **Command:** `cd folder_name` (Change Directory).
- **Concept:** Terraform and Git operate contextually based on the folder I am currently "standing" in. Creating a sub-folder (`automatic-accountant`) keeps the main repository clean.

### The Security Shield (.gitignore)
- **Concept:** Before writing code, I configured `.gitignore` to strictly exclude secret files.
- **Pattern:** `*.tfvars` (Ignores any file ending in .tfvars).
- **Why it matters:** This prevents me from accidentally committing API keys or passwords to GitHub, which is a critical security vulnerability.

### File Compression
- **Command:** `zip output.zip input.py`
- **Use Case:** AWS Lambda requires code to be uploaded as a `.zip` file. I learned to compress the Python script directly from the terminal before deployment.