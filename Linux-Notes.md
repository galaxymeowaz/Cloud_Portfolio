

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

* 4 + 1 = **5** (meaning the access group has permission to read and execute)

* 2 + 1 = **3** (meaning the access group has permission to edit and execute)

* 4 + 2 + 1 = **7** (meaning the access group has permission to read, write, and execute)

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
```

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
  ```

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

  ## Linux Notes: Archiving and Compressing (`tar`)

`tar` is short for **Tape Archive**.

### 1. Creating a Compressed Archive (`-czvf`)
Used to bundle and compress an entire folder into a single file.

**Command:** `tar -czvf backup_logs.tar.gz app_logs/`

**Breakdown:**
* `tar`: The Linux command used to bundle files together.
* `-czvf`: The flags dictating the action.
    * `c`: **C**reate a new archive.
    * `z`: Compress the archive using g**z**ip (this is what makes the file size smaller).
    * `v`: **V**erbose (displays the progress on the screen).
    * `f`: **F**ilename (specifies the output file name; must be the last letter).
* `backup_logs.tar.gz`: The name of the new compressed file being created.
* `app_logs/`: The target folder being backed up.

### 2. Viewing an Archive (`-tzvf`)
Used to view the contents of a compressed file without extracting it.

**Command:**
`tar -tzvf backup_logs.tar.gz`
* `t`: Lis**T** the contents.

### 3. Extracting an Archive (`-xzvf`)
Used to unpack a zipped archive back into a standard folder.

**Command:**
`tar -xzvf backup_logs.tar.gz`
* `x`: e**X**tract the files.

## 26 Feb 2026: Directory Synchronization (`rsync`)

I learned the enterprise upgrade to the basic `cp` command. `rsync` (Remote Sync) is used to mirror folders locally or across the network efficiently.

### 1. The Concept
- **What:** A command that synchronizes files from a source directory to a destination.
- **Why:** If I have 10GB of data and I change a single 10KB text file, `cp` will copy all 10GB again. `rsync` calculates the delta (the difference) and only copies the 10KB change.

### 2. The Command
- **Syntax:** `rsync -av [source_folder]/ [destination_folder]/`
- **The Flags:**
  - `-a` (Archive): Preserves all critical file permissions, ownership, and symbolic links.
  - `-v` (Verbose): Shows exactly what files are being transferred on the screen.
  - `-P` (Progress): Shows a progress bar and allows the command to resume exactly where it left off if the transfer is interrupted.

  ## 27 Feb 2026: Live Terminal Monitoring (`watch`)

I learned how to turn any standard static Linux command into a real-time, self-updating dashboard. 

### 1. The Concept
- **What:** The `watch` command executes a designated program periodically and shows the output in full-screen.
- **Why:** Instead of manually typing `df -h` over and over to see if a hard drive is getting full during a massive file transfer, `watch` automates the refresh process.

### 2. The Command
- **Syntax:** `watch -n [seconds] [command]`
- **The Flags:**
  - `-n`: Specifies the interval in seconds.
  - `-d`: (Highlight Differences) Visually highlights exactly which characters changed between the last refresh and the current one.

### 3. Practical DevOps Examples
- **Monitoring Disk Space:** `watch -n 5 df -h` (Refreshes every 5 seconds).
- **Monitoring Active Processes:** `watch -n 2 "ps aux | grep python"` (Monitors a running Python script).
- **Monitoring Live Logs:** `watch -n 1 tail -n 15 /var/log/auth.log` (Watches for live SSH login attempts).
- **Monitoring RAM usage in WSL** `watch -n 1 free -h` (watches for RAM usage every 1 second)

## 28 Feb 2026: Locating Executables (`which`)

I learned how to verify exactly where a command is running from on the system.

### 1. The Concept
- **What:** The `which` command searches the system's `$PATH` to find the exact file location of an executable program.
- **Why:** If I type `python3` and it fails, or if it runs the wrong version, `which python3` tells me exactly which binary file Linux is executing. This is critical for troubleshooting server environments with multiple software versions.

### 2. The Command
- **Syntax:** `which [command_name]`
- **Example:**
  ```bash
  which terraform
  ```

  ## 1 Mar 2026: Modifying File Ownership (`chown`)

I learned that permissions (`chmod`) are useless if the wrong person owns the file. The `chown` command allows me to transfer ownership of files and directories between users and groups.

### 1. The Concept
- **What:** `chown` stands for Change Owner. 
- **Why:** If a web server (like Nginx) is hacked, the hacker assumes the identity of the `www-data` user. If my database credentials are owned by `www-data`, the hacker can read them. If they are owned by `root`, the hacker is blocked.

### 2. The Command
- **Syntax:** `chown [User]:[Group] [Filename]`
- **Examples:**
  - `sudo chown root:root app.py` (Changes both user and group to root).
  - `sudo chown nginx: web_directory/` (Changes the user to nginx, and defaults to the nginx group).
  - `sudo chown -R myuser:mygroup /var/www/` (The `-R` flag recursively changes ownership for all files inside a folder).

### 3. The DevSecOps Use Case
When deploying applications to AWS EC2, you never run the application as `root`. You create a specific, restricted user account for the application and use `chown` to ensure that account can only access its own specific files and absolutely nothing else on the system.

## 2 Mar 2026: Data Sorting and Filtering (`sort` & `uniq`)

I learned how to organize raw text data and quickly identify duplicate entries, which is a critical skill for parsing server logs and identifying anomalies.

### 1. The Concept
- **`sort`:** Organizes lines of text alphabetically or numerically.
- **`uniq`:** Filters out adjacent duplicate lines.
- **The Golden Rule:** `uniq` only removes duplicates if they are right next to each other. Therefore, you must *always* run data through `sort` before piping it to `uniq`.

### 2. The Commands
- **Basic Sort:** `sort access.log`
- **Unique List:** `sort access.log | uniq` (Outputs a clean list of individual IPs).
- **Count Duplicates (`-c`):** 
  ```bash
  sort access.log | uniq -c
  ```
"sort access.log | uniq -c | sort -nr" is used to sort out the data, hides any duplicate numbers and shows how many times the same line of IP addresses appear if I am viewing an access.log file.

When I run "sort" and "uniq" it does not affect the main log file itself, it is only sorted for my view. This is important as when I want to verify what issues may happen, I can not let any evidence/clues disappear.

## 3 Mar 2026: Troubleshooting `locate` (Missing Packages)

I learned that many Linux environments (like base WSL) do not include the `locate` utility by default.

### 1. The Fix
If you get "command not found," you must install the package and initialize the database.
- **Install:** `sudo apt install plocate`
- **Initialize:** `sudo updatedb` (This scans the entire file system and builds the search index).

### 2. Why `locate` matters
Unlike `find`, which scans the live hard drive in real-time (slow), `locate` scans the index created by `updatedb` (instant).

### 3. Usage
- `locate [filename]` : Finds the file path instantly.
- `locate -n 5 [filename]` : Limits output to the first 5 results.

## 4 Mar 2026: User & Group Management

I learned how to manage identity on a Linux system, which is the foundational layer of system security.

### 1. The Concept
- **User:** A unique identity assigned to a person or a software service (e.g., `www-data` or `postgres`).
- **Group:** A collection of users. Permissions are usually assigned to the **Group** rather than individual users to make management easier.

### 2. The Commands
- **`adduser`:** Creates a new user with a home directory.
- **`groupadd`:** Creates a new access group.
- **`usermod -aG [group] [user]`:** - `-a`: **A**ppend (Add to the group).
  - `-G`: **G**roup (Specify the target group).

### 3. Practical DevOps Use Case
When deploying a multi-tier application, you create a "Service Account" (a user that isn't a real person). You then use `groupadd` to create a `web-admins` group and add your own user account to it. This allows you to deploy code without needing to log in as `root`.

## 5 Mar 2026: System Hardware Inspection

I learned how to check the system resources of a Linux instance using built in tools.

### 1. The Concept
- **`lscpu`**: Shows the CPU architecture, core counts, and vendor info.
- **`lsblk`**: Displays all block devices (Hard drives, partitions, and external disks).
- **`free -h`**: Provides a real-time summary of Physical RAM and Swap usage.

### 2. Why this matters for DevOps/FinOps
- **Scaling:** If `lscpu` shows only 1 core but your application is multi-threaded, your server is a bottleneck.
- **FinOps:** Checking `lsblk` helps verify if your storage volume (EBS on AWS) is correctly mounted. If a volume isn't listed here, your application will crash.
- **Troubleshooting:** If your server is "laggy," checking `free -h` helps identify if you have run out of RAM and are hitting the "Swap" file (which is much slower than RAM).

## 6 Mar 2026: Network Port Monitoring (`ss`)

I learned how to check network connections to ensure my cloud applications are actually "listening" for traffic on the correct ports.

### 1. The Concept
- **What:** `ss` stands for "Socket Statistics." It displays information about TCP and UDP network connections.
- **Why:** Before you blame a firewall or cloud security group for an outage, you must first verify that your application is actually running and listening on the server's local port.

### 2. The Flags (The "TULN" acronym)
- `-t`: **T**CP connections.
- `-u`: **U**DP connections.
- `-l`: **L**istening ports (the most important part for DevSecOps).
- `-n`: **N**umeric (show port numbers instead of service names like 'http').
- `-p`: **P**rocess (shows which program owns the connection; requires `sudo`).

## 7 Mar 2026: Mastering Standard Streams (0, 1, 2) & Output Redirection

I learned how Linux segregates successful command outputs from failure messages, and how to control where that data goes. This is the foundation of automated logging in DevOps.

### 1. The Concept (The Three Streams)
Every Linux command communicates using three standard data streams:
- **0 (stdin):** Standard Input (Data fed *into* a command).
- **1 (stdout):** Standard Output (The successful text a command prints).
- **2 (stderr):** Standard Error (The failure/error messages).

### 2. The Operators
- `>` : Redirects Stream 1 (stdout) into a file.
- `2>` : Redirects Stream 2 (stderr) into a file.
- `2>&1` : Merges Stream 2 into Stream 1 (Combines errors and success into the same output).

### 3. Practical Execution & Verification
I ran a test to prove I could capture both successful output and errors simultaneously:
```bash
# 1. Provide the command with one real file and one fake file.
ls real_data.txt fake_data.txt > combined.log 2>&1
```
# 2. Verify the capture by reading the file.
cat combined.log

## 8 Mar 2026: File Integrity & Hashing (`sha256sum`)

I learned how to verify that a file has not been tampered with or corrupted by generating a cryptographic fingerprint.

### 1. The Concept
- **What:** A "hash" is a fixed-length string of characters generated by a mathematical algorithm based on the exact contents of a file.
- **Why:** If even a single space or letter is changed inside a 10GB file, the resulting hash will look completely different. This proves the file was altered.

### 2. The Command
- **Generate a Hash:** `sha256sum [filename]`
- **The Algorithm:** SHA-256 (Secure Hash Algorithm 256-bit) is the current enterprise standard. The older version, `md5sum`, is considered vulnerable and should be avoided for security purposes.

### 3. DevSecOps Use Case
When downloading a tool like Terraform from the official HashiCorp website, they provide a `.sha256` file containing the official fingerprint. After I download the `.zip` file to my Linux server, I run `sha256sum` on it. If my output matches their website, I know the file is safe to install.

## 9 Mar 2026: DNS Troubleshooting (`nslookup`) & Package Management

I learned how to check Domain Name System (DNS) records directly from the terminal, and how to handle missing networking packages in the Linux server environment.

### 1. The Concept
- **What:** `nslookup` (Name Server Lookup) checks DNS servers to find the IP address associated with a domain name.
- **Why:** When launching or migrating a website, DNS changes take time to propagate across the internet. `nslookup` allows me to verify exactly which server IP my domain is currently pointing to before I announce a launch.

### 2. The Commands
- **Standard Query:** `nslookup aztay.org` (Returns the IPv4 address).
- **Specific Record Query:** `nslookup -type=mx aztay.org` (Returns the Mail Exchange servers handling email).

### 3. Troubleshooting Missing Packages
If a Linux environment returns `Command 'nslookup' not found`, the core networking tools are missing. 
- **The Fix:** Run `sudo apt install bind9-dnsutils`. This package contains `nslookup` and other essential DNS utilities.

## 10 Mar 2026: Directory Visualization (`tree`) & Package Installation

I learned how to install missing utilities and instantly generate a visual map of my project folders.

### 1. The Installation Breakdown
Command: `sudo apt install tree -y`
- **`sudo`**: Executes the command with root (Administrator) privileges.
- **`apt`**: Advanced Package Tool (The Linux package manager).
- **`install`**: The action telling `apt` to fetch and unpack the software.
- **`tree`**: The specific package/utility name.
- **`-y`**: The "Yes" flag. It automatically approves the installation prompt, which is essential for hands-free automation.

### 2. The Concept (`tree`)
- **What:** The `tree` command lists the contents of directories in a hierarchical, branching format.
- **Why it matters:** It is highly useful for quickly confirming which files are at what location. This allows me to easily see where my files and folders are before I change directories or write deployment paths.

## 12 Mar 2026: Pagination and Log Reading (`less`)

I learned how to safely inspect massive server log files without consuming all of my system's RAM or freezing my terminal session. ('less' seems very helpful compared to 'cat' as it prevents the entire file from loading into memory which could cause the server to crash.)

### 1. The Concept
- **What:** `less` is a terminal pager. It displays text files one screen at a time.
- **Why:** `cat` dumps the entire file to the screen instantly. `less` only loads the portion of the file you are currently looking at. This is critical for reading multi-gigabyte production logs without crashing the server.

### 2. The Keyboard Shortcuts
- `Spacebar`: Page down.
- `b`: Page up (backwards).
- `/word`: Search forward for a specific string.
- `n`: Jump to the next search match.
- `q`: Quit and return to the command prompt.

## 13 Mar 2026: System Health & Load Average (`uptime`)

I learned how to instantly check how long a server has been running and assess its CPU workload over time.

### 1. The Concept
- **What:** The `uptime` command outputs the current time, how long the system has been running, the number of logged-in users, and the system load averages.
- **Why:** If an application went offline at 2:00 AM, checking the `uptime` tells me if the entire server crashed and rebooted, or if just the application failed while the server stayed online.

### 2. Reading the "Load Average"
The command prints three numbers at the very end (e.g., `load average: 0.15, 0.05, 0.01`). These represent the CPU queue over the last **1 minute**, **5 minutes**, and **15 minutes**.
- **The Rule of 1.0:** If you have a 1-core CPU, a load of `1.0` means the CPU is at exactly 100% capacity. 
- **Overload:** A load of `2.0` on a 1-core CPU means the system is receiving twice as much work as it can handle, and processes are waiting in a queue (causing severe lag).

## 14 Mar 2026: Networking Identity (`hostname` & `ifconfig.me`)

I learned how to identify the internal and external addresses of my Linux environment, which is critical for configuring cloud firewalls and API allow-lists.

### 1. The Concept
- **Internal vs. External:** My server has a private identity (Hostname/Internal IP) for local communication and a public identity (Public IP) for the internet.
- **Why it matters:** When setting up the Gemini API, I may need to "whitelist" my server's Public IP so Google knows the traffic is coming from a trusted source.

### 2. The Commands
- `hostname`: Shows the local name of the machine.
- `hostname -I`: Shows the internal private IP address.
- `curl ifconfig.me`: Reaches out to an external service to reveal the server's Public IP.

### 3. Practical Use Case
If I am building a secure bot for the Gemini Hackathon, I can use `curl ifconfig.me` to find my server's address and then configure my Google Cloud Security settings to ONLY allow traffic from that specific IP address. This is a core "Zero Trust" practice.

## 15 Mar 2026: Centralized Log Management (`journalctl`)

I learned how to query the systemd journal to monitor system-wide events and troubleshoot service failures in real-time.

### 1. The Concept
- **What:** `journalctl` is a utility for retrieving and viewing logs collected by systemd.
- **Why:** In modern Linux, logs aren't always just plain text files in `/var/log`. `journalctl` provides a unified way to see logs from the kernel, background services (daemons), and applications in a single, searchable stream.

### 2. The Commands
- `journalctl -f`: **F**ollows logs live as they happen.
- `journalctl -n 50`: Shows the **N**umber of most recent lines (50).
- `journalctl -u nginx`: Filters logs for a specific **U**nit (service), such as Nginx or Docker.
- `journalctl --since "1 hour ago"`: Filters by time, allowing for rapid pinpointing of when a specific error started.

## 16 Mar 2026: System Clock & Calendar (`date` & `cal`)

I learned how to verify system time and view calendars without leaving the command line. This is essential for ensuring my server stays synchronized with external APIs like Google Gemini.

### 1. The Concept
- **What:** `date` prints the current system time; `cal` prints a formatted calendar.
- **Why:** Cloud services often fail if the server's time deviates by more than a few minutes from the API's time. Checking `date` is a standard first step in troubleshooting "Unauthorized" or "Invalid Token" errors.

### 2. The Commands
- `date`: Shows the full date, time, and timezone.
- `date +%s`: Shows the "Unix Epoch Time" (seconds since 1970). This is how computers talk to each other about time.
- `cal`: Displays a simple calendar of the current month.
- `cal -y`: Displays the calendar for the entire year.

## 17 Mar 2026: Fast Command Correction (`^old^new`)

I learned the "Quick Substitution" shortcut to fix typos or swap parameters in my previous command without using the arrow keys or retyping.

### 1. The Concept
- **What:** The `^` operator is a bash shortcut that performs a search-and-replace on the *most recent* command and executes it again.
- **Why:** During the Gemini Hackathon, I will be running complex deployment commands. If I misspell a folder name or want to quickly switch between `main.py` and `test.py`, this shortcut saves valuable seconds and reduces frustration.

### 2. The Command
- **Syntax:** `^original_text^replacement_text`
- **Result:** Linux takes the last command, replaces the first occurrence of `original_text` with `replacement_text`, and hits Enter for you.

## 18 Mar 2026: System Identity & CPU Architecture (`uname` & `lscpu`)

I learned how to pull a complete technical summary of my server's identity and processing power.

### 1. The Concept
- **What:** `uname` provides the "name" of the system.

- **Why:** When installing specific DevOps tools (like Docker or Terraform), you must know your CPU architecture (e.g., `x86_64` vs `aarch64`). Using these commands ensures I download the correct version of software for my specific environment.

## 19 Mar 2026: Real-Time Network Diagnostics (`mtr`)

I learned how to use `mtr` to combine the functions of `ping` and `traceroute` into a live-updating diagnostic dashboard.

### 1. The Concept
- **What:** `mtr` (My TraceRoute) constantly probes the path to a destination, updating statistics for every "hop" (router) in between.
- **Why:** While `ping` only tells me if the final destination is up, `mtr` shows me exactly which router in the middle is dropping packets or causing lag. This is essential for troubleshooting AWS connectivity or Gemini API latency.

### 2. The Columns to Watch
- **Loss%:** If a middle hop shows 50% loss but the final hop shows 0%, the middle router is likely just "limiting" ICMP traffic. If the final hop shows loss, you have a real connection problem.
- **Snt:** The number of packets sent. Let it run until `Snt` is at least 50 for an accurate report.
- **Last/Avg/Best/Wrst:** The speed of your connection in milliseconds (ms).

## 20 Mar 2026: The "Last Argument" Keyboard Shortcut (`Alt + .`)

I learned the fastest way to reuse the last piece of information from my previous command without re-typing or copy-pasting.

### 1. The Concept
- **What:** `Alt + .` is a Bash shell shortcut that inserts the last "argument" (the final word) of the previous command into your current prompt.
- **Why:** In Cloud Architecture, file paths are often very long (e.g., `/var/www/html/assets/img/logo.png`). Typing them once is enough; `Alt + .` allows me to chain commands together instantly.

### 2. Practical Examples
- **Step A:** `nano secret_config.txt` (You edit the file).
- **Step B:** `git add [Alt + .]` (Automatically becomes `git add secret_config.txt`).
- **Step C:** `git commit -m "update [Alt + .]"` (Automatically becomes `git commit -m "update secret_config.txt"`).

## 22 Mar 2026: Job Control & Background Processes (`&`, `jobs`, `fg`)

I learned how to manage multiple running processes within a single terminal session without needing to open multiple windows.

### 1. The Concept
- **What:** The `&` operator tells Linux to execute a command but immediately return control of the terminal to the user while the command finishes in the background.
- **Why:** When testing a live web server or running a massive file download (`curl`), I do not want my terminal frozen. Pushing the task to the background allows me to continue writing code or checking logs in the same session.

### 2. The Commands
- **`[command] &`**: Appending the ampersand starts the task in the background.
- **`jobs`**: Lists all tasks currently running in the background of this specific terminal session.
- **`fg [Job_ID]`**: Brings a background job back to the **F**ore**g**round.
- **`Ctrl + Z`**: If I forget to use `&` and trap my terminal, `Ctrl + Z` suspends (pauses) the active program, allowing me to type `bg` to force it into the background.

## 23 Mar 2026: Persistent Background Processes (`nohup`)

I learned how to run server applications that survive terminal disconnections. This is critical for keeping my Hackathon API backend alive after I log out of the server.

### 1. The Concept
- **What:** `nohup` stands for "No Hang Up." It intercepts the `SIGHUP` signal that Linux sends when a user disconnects, preventing the target application from being killed.
- **Why:** `&` puts a task in the background, but it is still tied to the active session. `nohup ... &` completely detaches the task, allowing it to run indefinitely on the server.

### 2. The Commands
- **Start Detached Task:** `nohup python3 main.py &`
- **View Output:** Because the task can no longer print to the terminal, all `stdout` and `stderr` streams are automatically routed to a file named `nohup.out` in the directory where the command was run.
- **Custom Log File:** `nohup python3 main.py > server.log 2>&1 &` (Routes the output to a specific file instead of the default `nohup.out`).

## 24 Mar 2026: Stealth Execution & History Hygiene (`HISTCONTROL`)

I learned how to execute sensitive Linux terminal commands without leaving a trace in the system's bash history logs.

### 1. The Concept
- **What:** By placing a single `Space` character at the very beginning of a command line, Linux will execute the command but refuse to save it to the history file.
- **Why:** When testing DevSecOps pipelines, I often need to temporarily export a real API key or database password into the environment. If I do not use the space trick, that credential is saved in plain text in my `~/.bash_history` file, creating a massive security vulnerability.

### 2. The Requirement
- This trick relies on a hidden environment variable called `HISTCONTROL`. 
- In Ubuntu/WSL, it is set to `ignoreboth` by default (which means it ignores commands starting with a space, and ignores consecutive duplicate commands).
- **Verification:** `echo $HISTCONTROL`

## 25 Mar 2026: Terminal Cursor Navigation (`Ctrl` Shortcuts)

I learned how to navigate and edit long command-line strings instantly without using the arrow keys or mouse.

### 1. The Concept
- **What:** Standard Bash environments use Emacs-style keybindings for line editing. 
- **Why:** In DevSecOps, commands (like AWS CLI queries or Terraform initializations) are often incredibly long. Keyboard shortcuts allow for rapid corrections, saving significant time during high-pressure deployments.

### 2. The Core Shortcuts
- `Ctrl + A`: Jump cursor to the **A**bsolute beginning of the line.
- `Ctrl + E`: Jump cursor to the **E**nd of the line.
- `Ctrl + W`: Delete one **W**ord backward from the cursor.
- `Ctrl + U`: Cut/Clear everything from the cursor to the beginning of the line.
- `Ctrl + L`: Clears the entire terminal screen (faster than typing `clear`).

## 26 Mar 2026: Directory Stack Navigation (`pushd` & `popd`)

I learned how to navigate between complex directory structures instantly without retyping file paths.

### 1. The Concept
- **`pushd` (Push Directory):** Changes your directory and "bookmarks" your previous location by pushing it onto a hidden stack.
- **`popd` (Pop Directory):** Pulls the most recent bookmark off the stack and instantly teleports you back to that directory.
- **`dirs`:** Shows the current list of saved directories in your stack.

### 2. The DevSecOps Use Case
When an application crashes, I need to check the logs in `/var/log/` and then edit the configuration file in `/etc/`. `pushd` allows me to jump to the config file, fix the error, and immediately `popd` back to the logs to see if the error is resolved, saving critical time during an outage.

## 27 Mar 2026: Command Resolution (`type`)

I learned how to debug how the Bash shell interprets commands, differentiating between aliases, built-ins, and physical binaries.

### 1. The Concept
- **What:** The `type` command tells you exactly what will happen when you type a specific word into the terminal and hit Enter.
- **Why:** If I type `docker` and get an unexpected error, `which docker` might tell me the file is correct, but `type docker` will reveal if another developer secretly aliased `docker` to a different, broken script. 

### 2. The Command
- **`type [command]`**: Analyzes the word and returns its nature:
  1. **Alias:** A custom shortcut.
  2. **Shell Builtin:** A command native to Bash (like `cd`, `echo`, or `export`).
  3. **File:** An executable binary located in the system's `$PATH`.

  ## 28 Mar 2026: Identity Verification (`whoami` & `id`)

I learned how to instantly verify my active user privileges and group memberships before executing system commands.

### 1. The Concept
- **`whoami`:** Returns the exact username currently logged into the terminal session.
- **`id`:** Returns the username, User ID (UID), primary Group ID (GID), and all other secondary groups the user belongs to.

### 2. The DevSecOps Use Case
In AWS EC2 or Docker containers, applications often run under restricted service accounts. If a script is failing with a "Permission Denied" error, typing `id` confirms whether the current session actually has the correct group permissions (e.g., the `docker` group) required to execute the file.

## 29 Mar 2026: Parsing JSON Data (`jq`)

I learned how to format and read complex JSON API responses directly in the terminal without exporting the data to a graphical text editor.

### 1. The Concept
- **What:** `jq` is a lightweight, command-line JSON processor. It acts like `sed` or `awk`, but is specifically designed for JSON data structures.
- **Why:** Cloud CLIs (like AWS CLI or Google Cloud CLI) and AI APIs output data in JSON format. When an API request fails, finding the specific `"error_message"` inside a 500-line unformatted JSON block is nearly impossible without `jq`.

### 2. The Commands
- **Pretty Print:** `cat file.json | jq` (Formats and color-codes the data).
- **Extract Specific Key:** `cat file.json | jq '.data.model'` (Outputs only the value associated with the 'model' key).

## 30 Mar 2026: Reclaiming Trapped Network Ports (`lsof`)

I learned how to identify and terminate background processes that are locking critical network ports, preventing "Address already in use" errors during deployment.

### 1. The Concept
- **What:** `lsof` stands for "List Open Files." In Linux, everything is a file, including active network connections and sockets.
- **Why:** When a Python or Node.js web server crashes, it often fails to release its assigned port. You cannot launch the application again until you find the hidden process holding the port and kill it.

### 2. The Commands
- **Find the Culprit:** `lsof -i :[PORT_NUMBER]` (e.g., `lsof -i :8080`).
- **The Execution:** The output provides the specific `PID` (Process ID). Execute `kill -9 [PID]` to forcefully terminate the process and free the port.

## 31 Mar 2026: High-Speed Configuration Editing (`nano` Shortcuts)

I learned advanced navigation and deletion shortcuts for the `nano` editor to accelerate my DevSecOps workflow when editing Docker configuration files.

### 1. The Concept
- **Efficiency:** Editing text in a terminal can be slow. Shortcuts like `Alt + T` (Cut to End) and `Alt + Backspace` (Delete Word) allow for rapid refactoring of code without using a mouse or the arrow keys.
- **Why it matters for Docker:** `Dockerfile` instructions often have long paths. Being able to delete a whole word or a whole block of code instantly reduces human error during manual configuration.

### 2. The Essential Shortcuts
- `Alt + T`: **T**runcate/Cut everything from the cursor to the end of the file.
- `Alt + Backspace`: Delete the entire word to the left of the cursor.
- `Ctrl + K`: Cut the entire current line.
- `Ctrl + U`: **U**ncut (Paste) the last thing you deleted with `Alt + T` or `Ctrl + K`.

## 2 Apr 2026: Terminal Flow Control (`Ctrl + S` & `Ctrl + Q`)

I learned how to pause and resume the visual output of the terminal to inspect high-velocity logs during a live deployment.

### 1. The Concept
- **What:** `Ctrl + S` (XOFF) stops the terminal from sending output to the display. `Ctrl + Q` (XON) resumes it.
- **Why:** When a Docker container or a Gemini API script is dumping thousands of lines of logs (Standard Output), I often need to "pause time" to read a specific error code without killing the process with `Ctrl + C`. 

### 2. The Use Case
During the Hackathon, if my agent is in a "loop" and spitting out text, I can hit `Ctrl + S` to freeze the frame, copy the error message, and then hit `Ctrl + Q` to let the program continue running in the background.

## 4 Apr 2026: Rapid File Generation (`Heredoc / EOF`)

I learned how to use the `cat <<EOF` syntax to create multi-line configuration files (like Dockerfiles or YAML manifests) directly from the command line.

### 1. The Concept
- **What:** A "Heredoc" (Here Document) is a redirection operator that tells the shell to read input until it sees a specific delimiter (usually `EOF` for "End Of File").
- **Why:** In DevSecOps automation, I cannot manually open a text editor on a remote server. Heredocs allow me to write scripts that generate their own configuration files automatically during a deployment.

### 2. The Command Structure
- `cat <<EOF > filename`: The `>` overwrites the file with everything you type until you type `EOF` on a new line.
- `cat <<EOF >> filename`: The `>>` appends the text block to the bottom of an existing file.

## 6 Apr 2026: Column Extraction (`awk`)

I learned how to isolate and extract specific vertical columns of text from terminal outputs and log files.

### 1. The Concept
- **What:** `awk` is a powerful text-processing language, but its most common DevSecOps use case is column extraction. By default, it treats any space or tab as a "column divider."
- **Why:** If I run `ps aux | grep python` to find a frozen server, it returns a long string of data. I only need the PID (Process ID) which is located in the 2nd column. `awk` grabs that specific number so I can pipe it directly into a `kill` command.

### 2. The Command Structure
- `awk '{print $1}'`: Prints the 1st column.
- `awk '{print $2}'`: Prints the 2nd column.
- `awk '{print $0}'`: Prints the entire line (equivalent to standard output).
- `awk '{print $NF}'`: Prints the **N**umber of **F**ields (the very last column, no matter how many columns there are).

## 6 Apr 2026: Execution Profiling (`time`)

I learned how to benchmark command and script execution speed to optimize cloud resource consumption.

### 1. The Concept
- **What:** Placing the word `time` before any Linux command tracks exactly how many seconds and milliseconds the CPU spent executing it.
- **Why:** In Serverless Cloud environments (like AWS Lambda or Google Cloud Functions), I am billed by the millisecond. If my Python script takes 2.5 seconds to process a Gemini API response instead of 0.5 seconds, my cloud infrastructure costs will multiply by 5x.

### 2. Reading the Output
- **Real:** The total time passed in the real world (Latency + Processing). This is the metric that affects the end-user waiting for a response.
- **User/Sys:** The actual time the CPU spent working. If `real` is high but `user/sys` are near zero, it means the script isn't doing heavy math; it is just waiting on the network.

## 7 Apr 2026: The "Double Bang" Shortcut (`sudo !!`)

I learned the fastest way to re-execute the previous command with Administrative (root) privileges without retyping the entire string.

### 1. The Concept
- **What:** In Bash, `!!` is a designator that refers to the entire previous command line.
- **Why:** In DevSecOps, we follow the "Principle of Least Privilege," meaning we don't stay logged in as `root`. We often forget to prefix a command with `sudo`. This shortcut saves 5–10 seconds of retyping every time a permission error occurs.

### 2. The Logic
When you type `sudo !!`, the shell replaces the exclamation points with your last command before executing. 
- *Example:* If you typed `touch /root/secret.txt`, running `sudo !!` actually executes `sudo touch /root/secret.txt`.

## 8 Apr 2026: File Immutability (`chattr`)

I learned how to apply advanced file attributes to protect critical configuration files from accidental deletion or malicious modification.

### 1. The Concept
- **What:** The `chattr` (Change Attribute) command modifies file properties at the Linux file-system level, which is a layer deeper than standard read/write (`chmod`) permissions.
- **Why:** If a hacker gains `root` access, or a junior developer runs `sudo rm -rf /`, standard permissions will not stop them. The `+i` (Immutable) flag completely freezes the file state.

### 2. The Commands
- **Lock a File:** `sudo chattr +i [filename]`
- **Unlock a File:** `sudo chattr -i [filename]`
- **View Attributes:** `lsattr [filename]` (Standard `ls -l` will NOT show the immutable flag; you must use `lsattr` to see if the 'i' is present).

## 9 Apr 2026: Remote Port Scanning (`nc`)

I learned how to use Netcat to instantly verify if a remote server's port is open and accepting traffic, which is critical for debugging cloud firewalls.

### 1. The Concept
- **What:** `nc` (Netcat) is a networking utility for reading and writing data across network connections. 
- **Why:** `ping` only tells me if a server is turned on. It does not tell me if the specific application port (like Port 5432 for PostgreSQL or Port 8080 for my API) is open. `nc` tests the exact port directly.

### 2. The Command
- **Syntax:** `nc -zv [IP_or_Domain] [Port]`
- **The Flags:**
  - `-z`: Zero-I/O mode. It tells Netcat to just scan for a listening daemon without actually sending any data.
  - `-v`: Verbose. Forces Netcat to print "succeeded" or "failed" to the screen so I can read the result.

  ## 9 Apr 2026: Task Automation (`crontab`)

I learned how to schedule background scripts to run automatically at specific intervals using the Linux Cron daemon.

### 1. The Concept
- **What:** `cron` is a background service that reads the `crontab` (cron table) and executes the listed commands at the specified times.
- **Why:** Essential for DevSecOps automation, such as triggering daily database backups, rotating logs, or pulling API data every 5 minutes without human intervention.

### 2. The Time Syntax (5 Asterisks)
The schedule is defined by 5 fields: `Minute Hour Day Month DayOfWeek`
- `* * * * *`: Run every minute.
- `0 * * * *`: Run at the top of every hour (Minute 0).
- `0 2 * * *`: Run every day at 2:00 AM.
- `*/5 * * * *`: Run every 5 minutes (using the step operator `/`).

### 3. The Commands
- `crontab -e`: **E**dit the schedule.
- `crontab -l`: **L**ist scheduled tasks.
- `crontab -r`: **R**emove (Delete) the entire table.

## 11 Apr 2026: Pipeline Argument Execution (`xargs`)

I learned how to bridge the gap between text-filtering tools and execution commands using `xargs`.

### 1. The Concept
- **What:** `xargs` reads items from standard input (separated by spaces or newlines) and executes a specified command once for every item.
- **Why:** Many core Linux commands (like `rm`, `kill`, or `cp`) do not accept data directly through the pipe (`|`). `xargs` catches the piped text and formats it correctly for the receiving command.

### 2. The DevSecOps Use Case
If a rogue script spawns 50 broken Python processes, I do not type `kill` 50 times. I combine `grep`, `awk`, and `xargs` to terminate them all instantly:
```bash
ps aux | grep "python" | awk '{print $2}' | xargs kill -9

## 12 Apr 2026: Safe Data Transport (`base64`)

I learned how to encode and decode text strings to ensure special characters do not break cloud configuration files.

### 1. The Concept
- **What:** `base64` translates any text or binary data into a restricted alphabet of 64 standard characters (A-Z, a-z, 0-9, +, /).
- **Why:** In DevOps, tools like Kubernetes strictly require secrets (like passwords or API keys) to be injected as Base64 encoded strings in their YAML manifests. This ensures parsing engines do not crash when they encounter strange symbols.

### 2. The Commands
- **Encode:** `echo -n "secret_text" | base64`
- **Decode:** `echo "encoded_text" | base64 --decode`

## 14 Apr 2026: AWS Identity Verification (`sts get-caller-identity`)

I learned the AWS CLI equivalent of the Linux `whoami` command to instantly verify my active IAM context before executing cloud infrastructure changes.

### 1. The Concept
- **What:** STS stands for Security Token Service. The `get-caller-identity` command returns details about the IAM user or role whose credentials are used to call the API.
- **Why:** In DevSecOps, I manage multiple AWS environments (e.g., Personal Sandbox, Hackathon Project, Client Production). Running a command like `aws s3 rm --recursive s3://my-bucket` while accidentally authenticated to a production profile will result in severe data loss. 

### 2. The Verification Workflow
Before executing `terraform apply` or any destructive AWS CLI command, it is mandatory hygiene to run `aws sts get-caller-identity` to confirm the `Account` ID and `Arn` match the intended target environment.

## 15 Apr 2026: Command-Line Network Management (`nmcli`)

I learned how to scan for and connect to Wi-Fi networks using the terminal, a critical skill for managing headless servers and remote Linux environments.

### 1. The Concept
- **What:** `nmcli` is the command-line interface for NetworkManager, the standard Linux service that handles network connections.
- **Why:** In a DevSecOps role, you will often manage servers (like a Raspberry Pi or an AWS Snowcone) that have no monitor or mouse. Being able to reconfigure network interfaces via SSH or serial console is a mandatory survival skill.

### 2. The Essential Commands
- `nmcli dev wifi list`: Scans the airwaves for available SSIDs, showing signal strength and security types.
- `nmcli dev wifi connect "SSID" password "PWD"`: Establishes a connection and saves the profile permanently.
- `nmcli connection show`: Lists all saved network profiles on the machine.
- `nmcli connection up/down [Name]`: Manually toggles a specific connection on or off.