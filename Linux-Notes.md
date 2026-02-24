# Linux Command Log 
**Author:** [Joseph Tay]
**Status:** Learning in Progress

## 1. The "Copy" Command (cp)
**Scenario** I tried to copy a file 'Upload.txt' from the folder 'Testing_Ground' to the folder 'Cloud_Portfolio'

#### What I tried (Wrong Command) based on what I learned for cp through trial and error
```bash
cp Testing_Ground/Upload.txt Cloud_Portfolio
```

* Why it did not succeed: I was already inside Testing_Ground, so the computer could not find a folder named Testing_Ground inside itself. It also did not know where Cloud_Portfolio was based on the directory I was in.

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

## 5 February 2026: Bash Scripting (Automation)

I learned how to write a script to automate repetitive tasks (like creating project folders).

### Key Concepts
1.  **The Shebang (`#!/bin/bash`):** The first line that tells Linux to use the Bash interpreter.
2.  **Variables (`$1`):** A placeholder that allows me to input a custom name when running the script.
    * *Example:* `./script.sh MyProject` -> The code replaces `$1` with `MyProject`.
3.  **Permissions:** Scripts are not executable by default. I must run `chmod +x scriptname.sh` or `chmod 700` to unlock them.

### My First Script (`project_init.sh`)
I created a script that automatically:
1.  Creates a directory.
2.  Navigates into it.
3.  Creates a generic README file.

**Usage:**
```bash
./project_init.sh [Project_Name]
```

## 6 February 2026: Grep (Searching Files)

I wanted to learn more about "grep" as I feel like I did not properly grasp it and understood how to fully utilize it. Today, I learnt how to search for specific text inside a file without opening it.

Command:
grep "text_to_find" filename

Example:
If I have a log file with thousands of lines, I can instantly find errors:
```bash
grep "Error" server_log.txt
``` 

## 7 February 2026: Piping (Connecting Commands)

I learned more about the Pipe symbol (`|`). It functions like an assembly line: it takes the output of the Left command and passes it as input to the Right command.

**Syntax:**
`Command_A | Command_B`

**Practical Use Case:**
Since `history` prints thousands of past commands, I can use a pipe to filter for specific ones (like when I was fixing my Java config):

```bash
# Find all previous commands related to "java"
history | grep "java"
```

### Advanced Piping Examples

**1. Counting Lines (`wc -l`)**
Instead of reading a long list, I can just count the results.
```bash
# How many "java" commands have I typed?
history | grep "java" | wc -l
```

## 9 February 2026: Curl (The API Tester)

I learned how to fetch data from the internet directly through the terminal. This is essential for AWS because it allows servers to communicate without a graphical browser.

**Command:** `curl` (Client URL)

**1. Checking Server Health (`-I`)**
In AWS, I will use this to check if my Load Balancer is active. The `-I` flag fetches just the "Header" (Status) to see if the site is up (Status 200).
```bash
curl -I [https://google.com](https://google.com)
```

**2. Downloading Files (-o) I can download scripts or configuration files directly to my instance.**

```bash
curl -o myfile.html [https://example.com](https://example.com)
```

Why this matters for DevOps: This is the primary tool for testing APIs and debugging network connections between microservices.

## 9 February 2026: Top (System Monitoring)

I learned how to check the health of my system instantly. This is the Linux equivalent of "Task Manager."

**Command:** `top`

**Key Metrics to Watch:**
1.  **%CPU:** If this is near 100%, the server is overloaded.
2.  **%MEM:** If this is high, the server is running out of RAM.
3.  **Load Average:** The 3 numbers at the top right (1 min, 5 min, 15 min averages).

**Exit:** Press `q` to return to the command line.

## On 10 February 2026. Process Management (The Task Manager)
I learned how to monitor system performance and terminate unresponsive programs manually.

### Monitoring (`top`)
- **Command:** `top`
- **Function:** Displays a real-time, dynamic view of the system's running processes.
- **Key Metrics:**
  - **PID:** Process ID (The unique number for the program).
  - **%CPU:** How much processing power it is using.
  - **%MEM:** How much RAM it is using.
- **Exit:** Press `q` to quit the dashboard.

### Listing Processes (`ps`)
- **Command:** `ps aux`
- **Flags:**
  - `a`: Show processes for all users.
  - `u`: Display the process's user/owner.
  - `x`: Show processes not attached to a terminal (background tasks).
- **Combo:** `ps aux | grep "python"` (Finds only Python processes).

### Terminating Processes (`kill`)
- **Command:** `kill [PID]`
- **Example:** `kill 12345`
- **Logic:** Sends a specific signal (SIGTERM) to the process ID, telling it to shut down gracefully.
- **Force Kill:** `kill -9 [PID]` (The "Nuclear Option" – forces the kernel to rip the process out of memory immediately).

### Troubleshooting: The "Grep Trap" & Force Kill
- **The Grep Trap:** When running `ps aux | grep name`, the search command itself often appears in the results.
  - *Fix:* Ignore the line that says `grep --color=auto name`. Only kill the line running the actual program.
- **Force Kill (`-9`):**
  - **Command:** `kill -9 [PID]`
  - **Why:** Standard `kill` sends a "Please Stop" signal (SIGTERM). If a program is frozen or stopped (Ctrl+Z), it might ignore this. `-9` sends a "Die Now" signal (SIGKILL) which cannot be ignored.

## On 11 February 2026. Productivity & Environment Customization (`alias`)
I learned how to create custom command-line shortcuts to speed up my development workflow.

### The `alias` Command
- **Concept:** `alias` allows me to map a long, complex command to a short, custom keyword. 
- **Temporary Creation:** `alias tf="terraform"`
  - *Result:* Typing `tf plan` now executes `terraform plan`.
- **Viewing Shortcuts:** Typing `alias` by itself lists all currently active shortcuts in the system.

### Permanent Aliases (`.bashrc`)
- **The Problem:** Aliases created directly in the terminal disappear when the session is closed.
- **The Solution:** To make them permanent, the alias command must be written into the `~/.bashrc` file. 
- **How it works:** Every time a new terminal window is opened, Linux reads the `.bashrc` file and loads all the custom settings and aliases into the new session automatically.
- **My standard aliases:**
  - `alias gs="git status"`
  - `alias ga="git add ."`
  - `alias gc="git commit -m"`

  ## On 12 February. Secure Access & Identity (`ssh-keygen`)
I learned how to generate cryptographic keys to authenticate with remote servers (AWS EC2) without using passwords.

### Key Generation
- **Command:** `ssh-keygen -t rsa -b 4096`
- **Flags:**
  - `-t rsa`: Specifies the type of encryption (RSA).
  - `-b 4096`: Specifies the bit-length (strength) of the key.
- **Output Location:** Keys are stored in the hidden directory `~/.ssh/`.

### The Key Pair Architecture 
- **Private Key (`id_rsa`):** The "Key." Kept strictly on the local machine. **NEVER** shared or uploaded.
- **Public Key (`id_rsa.pub`):** The "Lock." Uploaded to the remote server (e.g., AWS EC2 or GitHub).
- **Authentication Flow:** The server uses the Public Key to challenge the client; the client proves identity using the Private Key.

### Viewing Keys
- **Command:** `cat ~/.ssh/id_rsa.pub`
- **Use Case:** To copy the public key string so it can be pasted into the AWS Console or GitHub Settings.

## On 13 February 2026. History & Search
I learned how to retrieve and re-execute past commands to increase speed.

### Basic History
- **Command:** `history`
- **Function:** Lists previously executed commands with a specific ID number.
- **Filtering:** `history | grep "search_term"` (Finds specific past commands).

### Re-execution Shortcuts
- **`!n`:** Executes command number `n` from the history list (e.g., `!502`).
- **`!!`:** Re-executes the very last command (useful for adding `sudo`, e.g., `sudo !!`).

### Reverse Search (Interactive)
- **Shortcut:** `Ctrl + R`
- **Function:** Opens a search mode to find the most recent command matching your input.
- **Usage:**
  1. Press `Ctrl + R`.
  2. Type a keyword (e.g., "git").
  3. Press `Enter` to run the match, or `Ctrl + R` again to go further back.

  ## 14 February 2026. Log Monitoring (`tail`)
I learned how to inspect server logs and monitor files in real-time without opening them.

### Basic Usage
- **Command:** `tail [file]`
- **Function:** Outputs the last 10 lines of a file (useful for checking the most recent errors).
- **Flag `-n`:** `tail -n 20 [file]` (Displays the last 20 lines).

### Real-Time Monitoring (`-f`)
- **Command:** `tail -f [file]`
- **Function:** "Follows" the file. The command does not exit; it waits and prints new lines to the screen as they are added to the file.
- **Use Case:** Watching `var/log/syslog` or application logs while triggering an error to see exactly what happens.
- **Exit:** `Ctrl + C`.

## On 15 February. Disk Usage Monitoring
I learned how to analyze storage space to prevent "Disk Full" errors.

### System-Wide Check (`df`)
- **Command:** `df -h`
- **Flag `-h`:** "Human-readable" (Converts bytes to KB, MB, GB).
- **Function:** Displays total available space on the main hard drive (`/dev/root` or `/`).

### Directory-Specific Check (`du`)
- **Command:** `du -sh [directory]`
- **Flag `-s`:** "Summary" (Only shows the total for the folder, not every single file inside).
- **Flag `-h`:** "Human-readable".
- **Example:** `du -sh .` (Checks size of current folder).
- **Example:** `du -sh /var/log` (Checks size of the log folder).

## On 16 February 2026. Bulk Permission Fixing (WSL/Linux)
I learned how to fix files that look "green" (777 permissions) after moving them from Windows to WSL.

### The Problem
- **777 (rwxrwxrwx):** Readable, Writable, and Executable by everyone.
- **Risk:** SSH keys and Terraform will refuse to run if files are too open.

### The Fix (Recursive)
Instead of changing files one by one, use `find` to change them all at once.

1. **Fix Directories (Folders) -> 755**
   `find . -type d -exec chmod 755 {} +`
   * *Translation:* Find all items that are directories (`-type d`) and execute `chmod 755` on them.

2. **Fix Files (Text/Code) -> 644**
   `find . -type f -exec chmod 644 {} +`
   * *Translation:* Find all items that are files (`-type f`) and execute `chmod 644` on them.

   ## 17 February 2026. Advanced File Search
I learned the difference between searching for a *file name* and searching for *text inside a file*.

### 1. Find by Name (`find`)
- **Command:** `find ~ -name "main.tf"`
- **Use case:** I know the file is called "main.tf" but I don't know which folder it is in.
- **Tip:** Use `~` to search the entire home directory.

### 2. Find by Content (`grep`)
- **Command:** `grep -r "bakery" ~`
- **Use case:** I forgot the file name, but I know I wrote the word "bakery" inside it.
- **Flag `-r`:** Recursive (searches inside every folder and sub-folder).

## On 18 February 2026. Command Chaining (Logic Operators)
I learned that running commands one by one is slow, but chaining them incorrectly is dangerous. I learned the "Traffic Light" operators to control execution flow.

### 1. The Success Operator (`&&`)
- **Concept:** "Do X, and **IF** that works, do Y."
- **Symbol:** `&&` (Double Ampersand).
- **Logic:** Linux checks the "Exit Code" of the first command. If it is `0` (Success), it runs the second. If it fails, it stops immediately.
- **The "Dev" Use Case:** Preventing errors from cascading.
  - *Bad Practice:* `mkdir NewProject; cd NewProject` (If `mkdir` fails, `cd` will still try to run and confuse me).
  - *Best Practice:* `mkdir NewProject && cd NewProject` (If `mkdir` fails, the chain stops).

### 2. The Failure Operator (`||`)
- **Concept:** "Do X, and **IF** that fails, do Y."
- **Symbol:** `||` (Double Pipe).
- **Logic:** Only runs the second command if the first one errors out.
- **Use Case:** Creating "Fallbacks" or error messages.
  ```bash
  ping -c 1 google.com || echo "Internet Connection Lost"
  ```

  ## 19 Feb 2026. I Learned About Git Pre-Commit Hooks (Blocking Secrets)

Instead of relying only on `.gitignore`, a local Git hook can physically block sensitive files from being committed.

### 1. The Concept
- **What:** A hidden Bash script located at `.git/hooks/pre-commit`.
- **How:** It runs automatically when you type `git commit`. If the script exits with an error (`exit 1`), the commit is stopped immediately.

### 2. The Code
Save this inside `.git/hooks/pre-commit` and run `chmod +x .git/hooks/pre-commit` to make it executable:

```bash
#!/bin/bash

# Block .env, .pem, .key, and .sqlite files from being committed
if git diff --cached --name-only | grep -Eq '\.env|\.pem|\.key|\.sqlite'; then
    echo "🚨 ERROR: Sensitive file detected. Commit blocked."
    exit 1
fi

## 20 Feb 2026: Linux Output Redirection (`>` vs `>>`)

Instead of printing command results to the screen, redirection saves that output directly into files.

### 1. The Concept
- **What:** Using the `>` (Overwrite) and `>>` (Append) symbols to route output.
- **How:** Linux catches the text that would normally appear in the terminal and sends it to a document instead.

### 2. The Commands
- **`>` (Overwrite):** Creates a new file or completely erases an existing one to write the new data.
  ```bash
  echo "Server started" > log.txt 
  # log.txt is created and contains only this line.

## 21 Feb 2026: Output Redirection vs. Piping with `tee`

I learned the exact differences between silent file redirection (`>` and `>>`) and visible data splitting (`tee` and `tee -a`).

### 1. Core Differences

| Command / Operator | Action to File | Action to Screen (Terminal) |
| :--- | :--- | :--- |
| `>` | **Overwrites** existing file (or creates new). | **Hidden** (Does not print to screen). |
| `>>` | **Appends** to the bottom of the file. | **Hidden** (Does not print to screen). |
| `tee` | **Overwrites** existing file (or creates new). | **Visible** (Prints to screen). |
| `tee -a` | **Appends** to the bottom of the file. | **Visible** (Prints to screen). |

### 2. Practical Examples

* **`>` (Silent Overwrite):** ```bash
  echo "Data" > log.txt
  ```

  ## 22 Feb 2026: Symbolic Links (`ln -s`)

I learned how to create Linux shortcuts, known as Symbolic Links (or symlinks). This allows me to access or edit a file from multiple locations without creating duplicate copies that waste storage space.

### 1. The Concept
- **What:** A file that points to another file or folder on the system.
- **How:** Editing the symlink edits the original file. If the original file is deleted, the symlink breaks and becomes useless.

### 2. The Command
- **Syntax:** `ln -s [Original_File] [Shortcut_Name]`
- **The Flag:** `-s` stands for "symbolic." Without it, Linux creates a "hard link" (a much more complex duplicate).

### 3. Real-World Use Case
In DevOps, server logs are often buried deep in the system (e.g., `/var/log/nginx/error.log`). Instead of typing that long path every time, I can create a shortcut right in my home directory:
```bash
ln -s /var/log/nginx/error.log ~/error_logs
```

## 23 Feb 2026: File Comparison (`diff`)

I learned how to compare the contents of two files line-by-line. This is the underlying command that powers `git diff` and is essential for tracking configuration drift.

### 1. The Concept
- **What:** The `diff` command checks two files and outputs only the lines that are different.
- **Why:** In DevSecOps, it is used to audit configuration changes, detect unauthorized modifications, or troubleshoot failing code by comparing a broken file to a working backup.

### 2. The Commands
- **Basic Comparison:**
  ```bash
  diff old_config.txt new_config.txt
  ```

  ## 24 Feb 2026: Find and Replace Text (`sed`)

I learned how to automatically find and replace text inside configuration files using the command line. This is essential for CI/CD pipelines where files must be updated programmatically.

### 1. The Concept
- **What:** `sed` stands for Stream Editor. It reads text, modifies it according to a rule, and outputs the result.
- **Why:** Opening files in `nano` or VS Code is impossible during an automated server deployment. `sed` acts as an automated "Ctrl+F and Replace."

### 2. The Command Structure
The syntax uses `s` for substitute and `g` for global (replace all occurrences on a line).
- **Format:** `sed 's/OLD_TEXT/NEW_TEXT/g' filename`

### 3. Practical Examples
- **Preview Changes (Dry Run):**
  ```bash
  sed 's/HTTP/HTTPS/g' config.txt
  ```