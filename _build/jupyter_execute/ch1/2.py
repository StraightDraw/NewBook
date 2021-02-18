# 1.2 GitHub

GitHub was intimidating when I first began. I didn't understand all the pushing, pulling, cloning and forking. I didn't know where to go to do any of that Tug-of-War crap. Turns out, the solution is rather simple. 

````{warning}
GitHub can be confusing for noobies because there are several easy ways to accomplish most everything. That makes googling help for GitHub a bit difficult at times. Here, we'll just operate GitHub from the CMD.exe Prompt in Conda.
````
Here are some terms you'll have to learn to deal with GitHub.

````{margin}
MYST produces the *definition styling* you see here using a specially placed colon. That's it.
````

Clone
: Create a repo on your local machine that is both linked to and is an exact copy of a GitHub repo (online).

Add, Commit, Push
: Three step process that updates your local repo's files, syncs it with the online repo and pushes the changes over.

GitHub Pages
: Feature that allows GitHub repos to be compiled as HTML web pages and run from a branch called gh-pages.

Pull
: Creates a repo on your local machine that is an exact copy of a GitHub repo, yours and someone else's. Like cloning, except that a pull doesn't link the two repos.

````{margin}
Tweak special code blocks like tip, warning and *see also* by using an *admonition*. Here, we've hijacked the *note* special code block and inserted our title "wow."
````

````{admonition} Wow!
:class: note
GitHub Pages is totally free. Yep, web hosting for zero cost.
````

Programmers use GitHub branches differently than we will which again creates confusion, especially when trying to Google up some help.

Branch
: A secondary set of files where changes can be made and tested before updating the main (live) files.

Create a branch in your GitHub repo called **gh-pages**, and GitHub knows you're planning to publish web pages. GitHub automatically configures the branch for HTML and links it all to a URL.

## Cloning and Branching

````{margin}
Use one asterisk on either side to italicize a word or phrase. Double it up for bold. Hashtags create headings. One hashtag creates an HTML H1 class heading, two hashtags creates H2, and so on. We also have another example of the *tip* special code block.
````

If you don't have a GitHub account, now's the time. Skip the "Hello World" tutorial. Just create a new repository with a easy name like "newbook." Do **not** add the "ReadMe" file, and be sure it's public.

````{tip}
The name of your repo on GitHub will match the file folder where you edit things locally, so keep it short and sweet. Avoid special characters that are hard to type.
````

### Cloning

In Conda, open a CMD.exe Prompt. Use the change directory command **cd** to navigate to the where you want your book to live:

```
cd documents/conda
```

The example is based on my experience. In my Documents folder, I have a folder called "conda" where I store everything Conda-related: JupyterLabs, JuypterBooks, notes and projects. 

```
git clone git clone https://github.com/Straightdraw/newbook
```

````{warning}
When trying to enter your GitHub password in the command prompt environment, beware! The cursor doesn't move when you type. It's hiding your password for security, but not with the normal **** format. It feels weird, but type your password and hit Enter.
````

The cloning process creates a new folder called "newbook." It's linked and synched with your GitHub repo. Don't copy it or paste it. That usually breaks the link. If it ended up in the wrong place (and mine have), just delete the misplaced folder and reclone from the correct spot.

### Branching

You cannot branch an empty repo, so let's put some files in it. Switch to your newbook local repo.

```
cd newbook
```

Now, pull in the `newbook` files from my GitHub with this command.

```
git pull https://github.com/StraightDraw/NewBook
```

When you open up the folder, you will see a **config.yml** file in the newbook folder along with the content folder. The content folder houses all the notebooks which will be the chapters and sections of your `jupyter-book`.

#### Add, Commit and Push

Even though we have pulled the files into the newbook folder on our local machine, the repo that lives there is clueless. We have to wake it up and show it the new files we want it to include.

````{margin}
Four ticks create special code blocks. Three ticks create the copyable code blocks we're using here.
````

```
git add ./*
```
Now the local repo is up-to-date and includes *everything* in the folder. No clutter! Since everything gets pushed into the repo, we include essential files only.

```
git commit -m "Adding first files"
```

The local repo has now contacted the mother ship and said, "Hey, new files incoming." 

````{tip}
When you commit, use `-m` and put a comment inside double quotes. It is possible to commit without the comment, but it's far easier just to add a brief note about what's being updated. GitHub tracks the update notes like a changelog.
````

```
git push
```

Now the files are out on the GitHub repo and updated. You can check. You will also now have the option to branch your repo. The main branch now has a drop-down menu where you can add a branch.

```{image} https://docs.github.com/assets/images/help/branch/branch-selection-dropdown.png
:alt: Branching GitHub repo
:width: 35%
```

Create a branch called **gh-pages**. You have to use that exact name. You should check your settings, but GitHub is pretty good at guessing what you want with this branch. In settings, scroll to the GitHub Pages section and verify that your website is using the gh-pages branch, not the main branch. You also need the folder option to be **/root** which is the default. Don't select a theme. We're not building our website with Jekyll and GitHub. We're building our website with JupyterBook on our local machine and shoving it over.

