# 1.1 Conda

Anaconda is your quarterback. Set it up correctly, and life is good.

````{margin}
MYST special code blocks are really easy. This one's a warning, and below you see a tip and hint which use the same styling.
````

````{warning}
The name Miniconda seems like it might be great option that's easier to use, but Anaconda Navigator is best for beginners.
````

## Download Anaconda. Use Navigator

Go to [Anaconda.com](https://www.anaconda.com/products/individual) and dowload the free individual package of Anaconda. Once it's installed, find **Anaconda Navigator**. Don't just open it, put the icon in your start menu. You'll neeed it often.

Conda is an environment manager which can handle multiple complex coding environments. We don't need that. We just want one simple coding environment. Let's create it and keep things simple.

````{hint}
Don't make any changes to the base(root) environment. That's the control center.
````

````{margin}
To create the hint, we just use the following:
```

````{hint}

```
Then type in the hint, and close with 4 more ticks.
````


### Python Environment
I suggest you begin with a Python environment, just to get started. My entire Geometry Juypyterbook was built in markdown only (no engine). Why not get everything working properly in less than an hour, then work on other environments and engines? Wish I had.

To create your new environment, click the "Environments" tab on the left menu bar, then create as shown below.

````{margin}
Check out this [wiki](https://wiki.math.ntnu.no/_media/anaconda) for pretty good instructions about installing and setting up Anaconda.
````

![Conda Navigator Illustrion](https://wiki.math.ntnu.no/_media/anaconda/navigator-create-environment.png?w=550&tok=9ef301)


If you're creating markdown only Jupyter-books, then select the default Python engine which, as of January, 2021, is version 3.8. That's your engine. If you want to use R, MATLAB or SciLab as your engine I'll try to help with that later. The install will take a minute or two. When it's ready, click back to "Home" from the top-left menu and use the drop-down to make sure you are in the new environment.

````{hint}
You must click "Install" below CMD.exe Prompt and JupyterLab. This activates them so they can be launched.
````

You'll have the option to install several packages, all of which have their uses. For JupyterBooks, we only need to install JupyterLabs and the CMD.exe Prompt.

### Installing packages

We need to get the **JupyterBooks** and **github** packages installed, and the Python installer program **pip** helps with that. Open the CMD.exe Prompt and execute these commands:

````
conda install git
````
````
pip install -U jupyter-book
````
````
pip install ghp-import
````

Install `git` in the base environment so that it's commands will be available in all your environments. For the `jupyter-book` and `ghp-import` packages, they **must** be installed in the environment where you're planning to build out the JupyterBook. If you have multiple environments to create multiple books, you have to install them for each one.