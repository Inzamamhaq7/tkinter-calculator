````markdown
# Tkinter Calculator

A simple calculator application built with Python and Tkinter.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Decimal calculations
- Chained calculations
- Clear button
- Backspace button
- Clean calculation output
- Dark-themed user interface

## Technologies

- Python
- Tkinter

## How to Run

Make sure Python is installed on your computer.

Run:

```bash
python calculator.py
````

## Calculator Layout

```text
7   8   9   +
4   5   6   -
1   2   3   *
.   0   /   =
```

## Project Status

Completed.

````

Your folder should now look like:

```text
tkinter-calculator/
├── calculator.py
└── README.md
````

## 4. Check Git

In Git Bash:

```bash
git status
```

You should see:

```text
Untracked files:
    calculator.py
    README.md
```

## 5. Add the files

```bash
git add .
```

Then check:

```bash
git status
```

The files should now appear under **Changes to be committed**.

## 6. Make your first commit

```bash
git commit -m "Initial calculator project"
```

If Git asks you to configure your name/email, tell me what message it shows and I'll help you fix it.

## 7. Create the GitHub repository

Open GitHub in your browser.

Click:

**New repository**

Use:

```text
Repository name:
tkinter-calculator
```

You can add a description:

```text
A simple calculator built with Python and Tkinter.
```

Choose **Public** if you want it visible on your GitHub profile.

### Important

When creating the repository, **do NOT initialize it with**:

* README
* `.gitignore`
* License

We've already created the README locally.

Click **Create repository**.

## 8. Connect your local project to GitHub

GitHub will show you commands. You'll want the section for an **existing repository**.

It will look approximately like:

```bash
git remote add origin https://github.com/YOUR_USERNAME/tkinter-calculator.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

Then run them in Git Bash.

### 9. Push 🚀

Finally:

```bash
git push -u origin main
```

GitHub may open a browser authentication window.

After it succeeds, refresh your GitHub repository page.

You should see:

```text
tkinter-calculator
│
├── calculator.py
└── README.md
```

🎉 **Your first Tkinter project will be on GitHub.**

If you want to learn Git properly while doing this, **send me the output of each command as you go**, starting with:

```bash
git init
```

I'll tell you what each command is doing rather than just giving you commands to blindly copy.
