# Next Steps

JupyterBooks are great, but the documentation is sparse and high level, perfect for data science junkies who already use GitHub, Python and Jupyter. The compiler is opaque, especially the `build-a-book` commmand and the `ghp-import` command. If they fail, it can be difficult to decode why.

My plan is to post a couple of interesting tools in this chapter. First up is using the \<iframe> call to embed YouTube videos and Geogebra Animations. After that, I want to post about how to add different engines to JupyterLab and JupyterBooks. SciLab is an engine I'm dying to work with, an open-source equivalent to Mathematica or Maple, and I've already got a MATLAB engine for Linear Algebra.


## Tips and Tricks
1. Never leave an empty code block at the bottom of your JupyterLab notebook. The JupyterBook compiler often interprets that as an un-executed code block, and fails to compile.
    ````{Tip}
    Before spending long minutes debugging a bunch of code, always try re-executing all code blocks from top to bottom. See if the book will compile. Unexecuted code blocks are the number one reason JupyterBooks don't compile.
    ````
    ````{margin}
    Use single ticks to create mini-code blocks in a line of text. We can use it to highlight commands or files, as in `config.yml`.
    ````
2. Edit your `config.yml` and '`toc.yml` files directly in JupyterLab. Just be careful about the spacing. The indents control what chpaters and sections go where. 

3. To speed up the compiler, set the recompile option to “auto,” not “force,” in your `config.yml` file. That setting means only files that have changed get compiled. Saves a ton of time.

4. Control your logo file by finding a pic or creating a graphic and saving it as `logo.png` in your content folder. Then add this line in the config.yml file below your name.
    
    ```
    logo: logo.png
    ```
    
5. Only the `config.yml` file exists at the root, everything else goes inside the content folder, including your `toc.yml` file, your `Introduction.ipynb` file, your chapter folders and your logo picture.

6. When using `git` at the command shell, you will be asked for your password to push or update content from your laptop out to GitHub. YOU WON’T SEE YOUR PASSWORD AS YOU TYPE. In fact, nothing happens at all. It’s a security feature of the command prompt to not show your password. It would be really helpful if it showed the typical \**** as you were typing so you could know your keystrokes were making a difference, but it doesn’t. Trust the force, Luke.

7. The URL for your content will be MUCH easier to find after several hours. Initially, you have type the EXACT URL to see anything (use the Introduction.html page url for best results initially). Later, URL's will less case sensitive, and shorthand URL's (like those without the https) will work. It takes 2-3 hours for a new URL to propogate onto the interwebs.

8. Don't use **periods** in your file names for your notebooks. They will not work correctly in JupyterBooks if you use something Chap1.1 for chapter 1, section 1.

8. The broader community has embraced LaTeX so much that they’ve given it a hip new hacker name: dollar sign math (DSM). When using double-dollar sign math (DDSM) in MYST markdown, put two hard returns above and below the DDSM code. If there is no empty line between text and DDSM, it tends to display incorrectly.


```{toctree}
:hidden:
:titlesonly:


1
2
```
