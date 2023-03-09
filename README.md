## Brain Games: the collection of 5 math mini-games
<hr>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/AndryVanDuk/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/AndryVanDuk/python-project-49/actions) 
[![Maintainability](https://api.codeclimate.com/v1/badges/9a62c14fcac3cf24eddb/maintainability)](https://codeclimate.com/github/AndryVanDuk/python-project-49/maintainability)

This is project ["Brain Games"](https://ru.hexlet.io/programs/python/projects/49) on the Python Development course on [Hexlet.io](https://ru.hexlet.io/programs/python)

### Used technologies:
![](https://img.shields.io/badge/language-python-blue)
![](https://img.shields.io/badge/lybrary-prompt-brightgreen)
![](https://img.shields.io/badge/lybrary-random-orange)
![](https://img.shields.io/badge/lybrary-math-ff67b4)

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
| [wemake-python-styleguide](https://wemake-python-stylegui.de)               | "the strictest and most opinionated python linter ever" |

---
## Install
```
git clone https://github.com/AndryVanDuk/python-project-49.git
cd python-project-49
make package-install
```

### Description:

**"Mind Games"** is a set of five console games based on the popular mobile brain-pumping apps. Each game asks questions that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end the game and prompt you to play it again. 

Games:

* __Brain Even__ (Answer __"yes"__ if the number is even, otherwise answer __"no"__)
* __<g>Brain Calculator__ (Answer what is the result of the expression?)
* __Brain GCD__ (Answer what is the greatest common divisor of given numbers)
* __Brain Progression__ (Answer what number is missing in the progression?)
* __Brain Prime__ (Answer "yes" if given number is prime, otherwise answer "no")

They are launched with simple commands:*
```commandline
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```
:pencil2:*_Make sure that you have Python version 3.6 or higher installed._


### Game: "Is even?"
The essence of the game is as follows: the user is shown a random number.
And he needs to answer 'yes' if the number is even, or 'no' if it is odd:
[![asciicast](https://asciinema.org/a/561485.svg)](https://asciinema.org/a/561485)


### Game: "Calculator"
The essence of the game is as follows: the user is shown a random mathematical
expression that needs to be calculated and written down the correct answer.
[![asciicast](https://asciinema.org/a/561486.svg)](https://asciinema.org/a/561486)

### Game: "GCD" 
The essence of the game is as follows: the user shows two random numbers, for example,
25 50. The user must calculate and introduce the largest total divider of these numbers.
[![asciicast](https://asciinema.org/a/565155.svg)](https://asciinema.org/a/565155)

### Game: "Progression"
The essence of the game is as follows: the user is shown a series of numbers, forming an
arithmetic progression, replacing any of the numbers with two dots. The player must determine this number.
[![asciicast](https://asciinema.org/a/565973.svg)](https://asciinema.org/a/565973)


### Game: ""

### Good luck and have a fun game! 🤚