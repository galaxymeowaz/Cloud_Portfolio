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
- **Command:** `curl -I https://www.aztay.org`
- **Flag:** `-I` (Capital i) fetches only the **Headers** (metadata), not the HTML body.
- **Why I used it:** To verify if my website was being served by **Amazon CloudFront** or directly by S3.
- **Key Finding:** I looked for the header `x-cache: Miss from cloudfront` to confirm the CDN was working.

### Input/Output Redirection (`>`)
I learned how to save terminal output to files.
- **Command:** `history > log.txt`
- **Operator:** `>` (The Redirect Operator).
- **Function:** Instead of printing text to the screen (Standard Output), it sends the text into a file.
- **Use Case:** I used this to backup my daily command logs for documentation.
