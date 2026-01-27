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

# The "Home" Command (~)
I deduced that the symbol ~ is a shortcut to always go to the home directory based on how I had to learn "mv" which showed me how to move files from one location to another and came to the realisation that "~" is the home directory due to how I keep needing to place "~" before entering the location of where the file needs to be moved to.

Command | What it does

```bash
cd ~ | Brings me directly to the home directory 

cd .. | brings me to the previous directory/folder
```
