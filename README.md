# python-programming
Course material for Python Programming


# Python Installation

Follow the guide in the official Python documentation on how to do it for different operating systems: [Windows](https://docs.python.org/3/using/windows.html#installation-steps), [Mac](https://docs.python.org/3/using/mac.html#getting-and-installing-macpython), or [Unix](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) systems.


## Download and extract the course material
1. If Git is installed on the system, clone the repository by running: 
    ```bash
    git clone https://github.com/pavanshanbhag/python-programming.git
    ```
   Otherwise, download the zip from [Python-Programming](https://github.com/pavanshanbhag/python-programming/archive/refs/heads/main.zip) and extract the content.

2. Rename the root directory to `python-programming`. This step is necessary only if the extracted folder has a different name.

** Root Folder Structure:**
```plaintext
    python-programming
        |-- session1
        |   |-- xyz.ipynb
        |-- session2
        |   |-- xyz.ipynb
        |-- session3
        |-- session4
        |-- static
        |-- .gitignore
        |-- README.md
```

## Virtual Environment and Package Installs

Make sure that you have Python 3.8+ already properly installed on your machine.

I will be using `python3.12` when running Python

You should choose some base folder (created in previous step) where you will:
- Save the course materials
- Create your virtual environment(s)
- Save your Python code

Let's say the path to this directory is `<my_root>`.


## Package Installations

I decided to name my virtual environment `venv`. You can choose another name if you prefer.

We can use the same virtual environment for the entire course, so only need to do the following steps once.

1. Open a command prompt/terminal, and make sure to switch to the `<my_root>` directory.

2. Create the new virtual environment (In below example Python 3.9 is used, but you can choose version of your choice):
    - Mac/Linux: `python3.11 -m venv venv`
    - Windows: `py -3.12 -m venv venv`

3. Activate the new environment:
    - Mac/Linux: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate.bat`

4. In the shell (command prompt) where you just activated your environment, run the package installer with the specific package name (and optionally version):
    ```
    pip install jupyterlab
    ```

   That's it! Once `pip` has finished running, your virtual environment is ready to be used. 
   You only need to do this once, unless you delete the virtual environment, in which case you just follow the same steps again.

   The next time you want to use this environment, you just need to activate it.

   If you want to see what packages have been installed in your environment, use:
    ```
    pip freeze
    ```

   But be careful, this will list not just the packages you installed but also additional packages that were required by the packages you installed (so `pip` installs both the package you specify and the required dependencies for that package).


# Running Jupyter Lab

**From a command prompt:**
1. Navigate to your project root folder.
2. Activate your virtual environment.
    - If JupyterLab is not installed, Install it with pip: `pip install jupyterlab`
3. Launch JupyterLab with: `jupyter lab`
4. If a web browser does not automatically open up, find the URL in the command prompt window (output when Jupyter starts up), and paste that URL into your browser.

You can create Jupyter notebooks anywhere in your project folder - it does not have to be in the root of your project folder. You can create sub-folders and organize your notebooks however you want - just like you would organize Excel or Word documents.

## Keyboard Shortcuts

- Execute a cell: Shift+Enter
- Select current cell: Esc (or click on cell margin)
- Delete selected cell: DD (type D twice in succession)
- Change selected cell to Markup: M
- Change selected cell to Code: Y
- Save: S
- Insert cell above currently selected cell: B
- Insert cell after currently selected cell: A

Don't forget to re-run your Jupyter notebook when you re-load it later - this will re-execute all the cells (but it will stop processing the cells if it encounters an error).

**Project Jupyter documentation:** [https://docs.jupyter.org/en/latest/](https://docs.jupyter.org/en/latest/)
