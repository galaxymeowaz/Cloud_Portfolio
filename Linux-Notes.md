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

