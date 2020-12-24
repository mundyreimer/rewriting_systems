# Rewrite Systems

---

## TL;DR
Collection of personal experiments centered around applying *Rewrite Systems* to the study of artificial biological systems, computation, linguistics, and physics.

[See here] for my sequence of articles on *Rewriting Systems*.

(Overlapping) topics to be covered: 
* Artificial Life + Chemistry
* Cellular Automata
* Lindenmayer Systems
* Formal Grammars
* Fractal Generation
* Symbolic Dynamics
* Graph-based CA
* Evolutionary Algorithms

---

## Setup

For my graphics I chose to use [Turtle](https://docs.python.org/3/library/turtle.html) because it already comes pre-packaged with Python and follows the general "*batteries included*" philosophy.  Because of this, all you have to do is copy the specific *\*.py* script you'd like and run that.  Alternatively, if are a bit more advanced in your software skills, you might want to consider following the steps below.

### 1) Installing dependencies:

If just using venv, create a virtual environment named `venv_linden` using:
`python3 -m venv venv_linden`

If additionally using [Pyenv](https://github.com/pyenv/pyenv) to manage and easily switch between multiple Python versions (recommended practice), create a virtual environment using:

`pyenv virtualenv <python_version> <environment_name>`

See [tutorial here](https://realpython.com/intro-to-pyenv/) for more on Pyenv. Since some of the above graphics-based code relies on a pre-installed Python library called [Turtle](https://docs.python.org/3/library/turtle.html) which itself relies on Python's standard GUI package [Tkinter](https://realpython.com/python-gui-tkinter/), you might run into problems with Tkinter if you are running on a device that's updating to MacOS Big Sur (as of 12/23/2020).  If you do, you might need to install different Python versions via the patch found [here by @htp 8/31/2020](https://github.com/pyenv/pyenv/issues/1643).   

Then activate the environment: 

(Just using virtualenv) `source venv_linden/bin/activate`

(Using Pyenv's virtual environment) `pyenv local myproject`

The latter command creates a .python-version file in your current working directory from which you run `eval "$(pyenv virtualenv-init -)"` in your environment, allowing the environment to automatically activate upon entry into that directory (nifty!) Alternatively, you can manually activate your Pyenv environments using `pyenv activate <environment_name>` and deactivate using `pyenv deactivate`.

Then install any necessary packages or other dependencies I have (not required as of 12/23/20, but might need to do later down the road): 
`pip install -r requirements.txt`

### 2) Troubleshooting:

* [See here](https://github.com/pyenv/pyenv/issues/1643) if you are having trouble with Tkinter running on your device.  

---

## Sources:

* [See here](https://realpython.com/beginners-guide-python-turtle/) for a beginner's tutorial on how to use `Turtle` in Python.  I chose Turtle since it is a pre-installed Python library and follows the general "*batteries included*" philosophy.

* [See here](https://hackaday.io/project/11721-python-l-system) for an alternative to the Turtle package called *PyGame*.  This should be more familiar to graphics/game programmers but is still low-level enough for beginners.  Note that if your examples aren't running and you are using a recent version of Mac OS X, it might be a problem with the interaction between *pygame* and *virtualenv*. More [details here](https://github.com/pygame/pygame/issues/203#issuecomment-365798598).

* [See here](http://algorithmicbotany.org/papers/abop/abop.pdf) for *The Algorithmic Beauty of Plants* by [Przemyslaw Prusinkiewicz](https://en.wikipedia.org/wiki/Przemys%C5%82aw_Prusinkiewicz) (director of the Computer Graphics group studying Fibonacci numbers and modeling using grammars) and [Aristid Lindenmayer](https://en.wikipedia.org/wiki/Aristid_Lindenmayer) (a theoretical biologist studying sequence generators). This textbook is based off Lindenmayer's original notes discusssing the theory and practice of Lindenmayer (L-)Systems for modeling plant growth.  It provides much of the theoretical material from which I will be drawing from.

* [See here] for my sequence of articles on Rewriting Systems from the perspectives of theoretical biology, artificial life, physics, mathematics, computation, linguistics, and philosophy.


