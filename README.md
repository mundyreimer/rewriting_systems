# Rewriting Systems

## TL;DR
Collection of personal experiments centered around applying *Rewriting Systems* to the study of artificial biological systems, computation, linguistics, and physics.

![minkowski_island](/images/n2_island.gif = 300x300)

---
Check out my sequence of articles I wrote on *Rewriting Systems*:
* [An Introduction to Lindenmayer Grammars](https://mundyreimer.github.io/blog/lindenmayer-grammars-0)
* [Generating a Garden with Python](https://mundyreimer.github.io/blog/lindenmayer-grammars-1)

(Overlapping) topics to be covered: 
* Artificial Life + Chemistry
* Lindenmayer Systems
* Cellular Automata
* Formal Grammars
* Fractal Generation
* Graph-based CA
* Evolutionary Algorithms

## Setup

For my graphics I chose to use [Turtle](https://docs.python.org/3/library/turtle.html) because it already comes pre-packaged with Python and follows the general "[batteries included](https://protocolostomy.com/2010/01/22/what-batteries-included-means/)" philosophy.  Because of this, all you have to do is copy the specific *\*.py* script you'd like and run that.  Alternatively, if are a bit more advanced in your software skills, you might want to consider following the steps below.  This will become more relevant when I start incorporating more 3rd party packages.

### 1) Installing dependencies:

If just using venv, create a [virtual environment](https://towardsdatascience.com/virtual-environments-104c62d48c54) named `venv_linden` using:

`python3 -m venv venv_linden`

If additionally using [Pyenv](https://github.com/pyenv/pyenv) to manage and easily switch between multiple Python versions (recommended practice), create a virtual environment using:

`pyenv virtualenv <python_version> <environment_name>`

See [tutorial here](https://realpython.com/intro-to-pyenv/) and [here](https://opensource.com/article/19/5/python-3-default-mac) for more on Pyenv. Since some of the above graphics-based code relies on a pre-installed Python library called [Turtle](https://docs.python.org/3/library/turtle.html) which itself relies on Python's standard GUI package [Tkinter](https://realpython.com/python-gui-tkinter/), you might run into problems with Tkinter if you are running on a device that's updating to MacOS Big Sur (as of 12/23/2020).  If you do, you might need to install different Python versions via the patch found [here by @htp 8/31/2020](https://github.com/pyenv/pyenv/issues/1643).   

Then activate the environment: 

(Just using virtualenv) `source venv_linden/bin/activate`

(Using Pyenv's virtual environment) `pyenv local myproject`

The latter command creates a .python-version file in your current working directory from which you run `eval "$(pyenv virtualenv-init -)"` in your environment, allowing the environment to automatically activate upon entry into that directory (nifty!) Alternatively, you can manually activate your Pyenv environments using `pyenv activate <environment_name>` and deactivate using `pyenv deactivate`.

Then install any necessary packages or other dependencies I have (not required as of 12/23/20, but might need to do later down the road): 

`pip install -r requirements.txt`

### 2) Troubleshooting:

* [See here](https://github.com/pyenv/pyenv/issues/1643) if you are having trouble with Tkinter running on your device.  
## Running the Code

### Example User Input:
Running the *\*.py* script on the command line will prompt the user for at least 6 inputs.  See my linked tutorials I wrote above for an in-depth explanation.  Below is an example of what you can input to get something that eventually outputs a fern-looking plant:

`Enter starting axiom (w): X`

`Enter production rule #1 (Input 0 if no more rules): X->F[+X][-X]FX`

`Enter production rule #2 (Input 0 if no more rules): F->FF`

`Enter production rule #3 (Input 0 if no more rules): 0`

`Enter number of iterations n: 7`

`Enter segment length: 1`

`Enter initial angle: 90`

`Enter drawing angle: 25.7`

### Example Output:

![generated_fern](/images/generate_fern1.gif = 300x300)

![generated_fern](/images/fern3.png = 300x300)

## Sources:

* [See here](http://algorithmicbotany.org/papers/abop/abop.pdf) for *The Algorithmic Beauty of Plants* by [Przemyslaw Prusinkiewicz](https://en.wikipedia.org/wiki/Przemys%C5%82aw_Prusinkiewicz) (director of the Computer Graphics group studying Fibonacci numbers and modeling using grammars) and [Aristid Lindenmayer](https://en.wikipedia.org/wiki/Aristid_Lindenmayer) (a theoretical biologist studying sequence generators). This textbook is based off Lindenmayer's original notes discusssing the theory and practice of Lindenmayer (L-)Systems for modeling plant growth.  It provides much of the theoretical material from which I "draw" from 😅

* [See here](https://www.cs.tau.ac.il/~nachum/papers/survey-draft.pdf) for further theory behind abstract rewrite systems.  It gives a link to Chapter 6 of the *Handbook of Theoretical Computer Science* by Nachum Dershowitz and Jean-Pierre Jouannaud. 

* [See here](https://realpython.com/beginners-guide-python-turtle/) for a beginner's tutorial on how to use `Turtle` in Python.  I chose Turtle since it is a pre-installed Python library and follows the general "*batteries included*" philosophy. 

* [See here](https://hackaday.io/project/11721-python-l-system) for an alternative to the Turtle package called *PyGame*.  This should be more familiar to graphics/game programmers but is still low-level enough for beginners.  Note that if your examples aren't running and you are using a recent version of Mac OS X, it might be a problem with the interaction between *pygame* and *virtualenv*. More [details here](https://github.com/pygame/pygame/issues/203#issuecomment-365798598).  Other plotting packages options to choose among are [Pycairo](https://pycairo.readthedocs.io/en/latest/), [Pillow](https://pillow.readthedocs.io/en/stable/), and [Processing.py](https://py.processing.org/).  

* Much of the rendering template I used was built from Gianni Perez's [original implementation](https://github.com/ambron60/l-system-drawing), with fixes and comments based on Prusinkiewicz & Lindenmayer's original textbook linked above and [this tutorial](https://cgjennings.ca/articles/l-systems/) from Christopher Jennings.  Extra *Production Rules* were based off of an implementation done in an entirely different package [found here](https://hackaday.io/project/11721-python-l-system) and [here](https://cdn.hackaday.io/files/11721501471264/baum.py).  




