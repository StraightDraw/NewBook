# Building Blocks

Anaconda will be the quarterback running from your local machine, and GitHub will be the engine that runs your web content. Best news? It's all open-source and available free.

````{margin}
MYST has several pre-defined special code blocks: *tips*, *warnings*, *notes*, *margins* (which display in right margin like this) and *see also*.
````

````{note}
Anaconda is often abbreviated *conda*. *Repo* stands for repository.
````

I have created a set of template files that you can pull from GitHub into your repo. Since I've compiled them already, I know that they will work when you run JupyterBook and not throw error codes.

````{margin}
Numbered lists in MYST are far easier than LaTeX or HTML.
````

## Quick Overview: Creating a JupyterBook 

1. Create online repo on github
2. Clone the repo onto local machine
3. Pull template files into local repo
4. Add, commit, push to get files out to your github repo
5. Create branch in github repo called "gh-pages" for web hosting
6. Build JupyterBook on local machine
7. Add, commit, push again
8. Run ghp-import script to knit the whole thing together and publish it online


```{toctree}
:hidden:
:titlesonly:


1
2
3
```
