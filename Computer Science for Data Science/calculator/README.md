## Solution A2: Creating a *Python*-Project

The assignment shows good practices how to create and structure a *Python*
project. Few rules should be followed when creating a new software development.
They generally apply, regardless of the programming language:

- source code resides in the `src` directory (sub-tree) in the project
    directory.

- test code (unit tests) is always separated from the source code and typically
    resides in a `tests` directory (sub-tree).

- each, `src` and `tests`, have sub-directories to further structure the source
    code. The structure underneath `tests` mirrors the structure under `src`.

- only source code is under code management (e.g. *git*), no built artifacts,
    tools or binaries.

- a *build-process* must be defined and communicated in a project such that
    the project can be *"built"* any time from scratch.

*Python* does not assume or enforces (unlike Java/maven) any structure of a
software development project.

Read article by Ken Reitz:
[*"Structuring Your Project"*](https://docs.python-guide.org/writing/structure)
to learn about *best-practices* that should be followed in *Python* according to
Ken Reitz (obviously, this particular approach can be debated, but it is quite
common).

---

Goal of this assignment is to set up a new *Python* project following the guidance
from the article.
The project will create two components, a *"Calculator"* with methods:

- *add(a, b)* - return the sum of *a* and *b*, 

- *sub(a, b)* - subtract *b* from *a*,

- *mul(a, b)* - multiply *a* and *b*,

- *div(a, b)* - divide *a* by *b*,

- *factorize( n )* - return prime factors of *n*.

*"Calculator"* is a singleton component.


*"Collection"* provides *list* and *set* methods:

- *contains( s, e )* - calculate the number of times element *e* is in *s*,

- *zip(s, p)* - pair consecutive elements from *s* and *p*,

- *pset( s )* - calculate the powerset of *s*,

- *perm( p )* - calculate permutations of *p*,

*"Collection"* is an instantiatable component.


---
Steps:

1. Step: [*Answer Questions for Python Project-Setup*](#1-answer-questions-for-python-project-setup).

1. Step: [*Create project: "py-fun"*](#2-create-project-py-fun).

1. Step: [*Build the Project*](#3-build-the-project).

1. Step: [*Create the Calculator*](#4-create-the-calculator).

1. Step: [*Run the Calculator*](#5-run-the-calculator).

1. Step: [*Extend the Calculator*](#6-extend-the-calculator).

1. Step: [*Check Project into Local git Repository*](#7-check-project-into-local-git-repository).

1. Step: [*Push Project to Remote *git* Repository*](#8-push-project-to-remote-git-repository).

1. Step: [*Unit Tests*](#9-unit-tests).

### 1. Answer Questions for *Python* Project-Setup

1. What is the *project scaffold*?
    
    -> The initial structure or template of a software project. It provides a pre-defined directory layout, configuration files and boilerplate code

2. What is a software *build process*?

    -> A sequence of steps that convert source code into a runnable product like an executable, library or deployable package. In Python, building usually means creating a distributable package like .whl or .tar.gz rather than compiling to machine code

3. When does the software *build process* start and when does it end?

    -> It starts when the source code and dependencies are ready to be integrated or distributed and ends when we have a runnable artifact or deployable package. E.g. Start -> Code + Dependencies -> Testing -> Packaging -> End

4. What are steps and what is the result of the software *build process*?

    -> Typical steps are: Fetch dependencies (requirements.txt), Compile/pre-process code(if needed), Run Tests, Bundle or Package, Deploy or publish

5. What is *make*?

    -> Make is a build automation tool that uses a Makefile to define rules and dependencies for building software

6. What is the purpose of file *requirements.txt*? How is it used?

    -> It lists all Python dependencies needed for a project and can be installed with pip install -r requirements.txt

7. What is a *Build Server*? What does it mean for *Python*?

    -> A Building Server is a dedicated machine or service that automatically runs the build process whenever code changes (e.g. a Git push). You can think of Jenkins, GitHubActions, CircleCI and so on.. For Python it means setting up a virtual environment, installing dependencies, running tests, building the package, optionally deploying

8. What are *Nightly Builds*?

    -> They are automated builds created every night or on a schedule that contain the latest code and help catch regressions early. They are often used in CI(Continuous Integration) systems to monitor code stability over time.

9. What are the differences between
    [*"Scripts, Modules, Packages, and Libraries"*](https://realpython.com/videos/scripts-modules-packages-and-libraries)
    in *Python*?

    -> A Script is meant to be executed directly like main.py, a Module has functions, classes or variables that can be imported, A Package is a directory containing multiple modules and an __init__.py file, a Library is a collection of modules/packages designed for re-use like numpy or requests

10. What is *_ _ _init_ _ _.py* meant to be used for?

    -> It marks a directory as a Python package so it can be imported. __all__ is used to specify what is imported from package

---

```sh
find .                          # show project scaffold
```

---
### 9. Unit Tests

to follow...

<!-- 
Create unit tests for method: *factorize(int n)* with tests:

1. *regular cases:* n=1, n=2, n=3, n=4, n=27, n=65536, n=10952347, n=100000039 (prime number).

1. *corner cases (valid):* n=0, n=2147483646 (MAX_INT-1), n=2147483647 (MAX_INT) -- corner cases test valid input boundaries.

1. *error and exception cases (invalid):* n=-1, n=-10, n=-2147483648 -- exception cases test that the factorize(int n) method throw an IllegalArgumentException with message: negative argument.

Create a new test class:
 -->


<!-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -->
<!-- 
&nbsp;

### 10. Release

Create release branch:

```sh
git switch main                     # switch to the 'main' branch
git checkout -b release             # branch new 'release' branch off the 'main' branch
git branch                          # show branches
```

Change GAV-coordinates in *pom.xml* for the *artifactId* from `my-app` to `factorizer`
and for *version* from `1.0-SNAPSHOT` to `RELEASE-1.0.0`:
```xml
<groupId>de.factorizer</groupId>
<artifactId>factorizer</artifactId>
<version>RELEASE-1.0.0</version>
```

Commit the change to the release-branch:
```sh
git add . && git commit -m "update pom.xml, GAV to 'de.factorizer' 'RELEASE-1.0.0'"
```

The development is on branch `factorizer` and needs to be merged to the
`release` branch.

See the changes of the upcoming merge of the *factorizer* branch
to the *release* branch:

```sh
git diff HEAD..factorizer --name-status
```
```
M   pom.xml
D   src/main/java/com/mycompany/app/App.java
A   src/main/java/de/factorizer/App.java
A   src/main/java/de/factorizer/Factorizer.java
A   src/main/java/de/factorizer/FactorizerImpl.java
R086src/test/java/com/mycompany/app/AppTest.java   src/test/java/de/factorizer/AppTest.java
A   src/test/java/de/factorizer/FactorizerTests.java
```

Merge branch `factorizer` to the `release` branch:
```sh
git merge factorizer
```
```
Auto-merging pom.xml
CONFLICT (content): Merge conflict in pom.xml
Automatic merge failed; fix conflicts and then commit the result.
```

Resolve the merge conflict and rebuild to verify everything works:
```sh
mvn clean package

java -jar target/factorizer-RELEASE-1.0.0.jar 10 100 1000
```
```
Error: Could not find or load main class com.mycompany.app.App
Caused by: java.lang.ClassNotFoundException: com.mycompany.app.App
```

Fix the bug, rebuild and re-run:

```sh
# fix: <mainClass>de.factorizer.App</mainClass>
mvn clean package

java -jar target/factorizer-RELEASE-1.0.0.jar 31 961 29791 923521
```
```
Hello Factorizer!
 - n=31 -> [31] (prime number)
 - n=961 -> [31, 31]
 - n=29791 -> [31, 31, 31]
 - n=923521 -> [31, 31, 31, 31]
```

Commit the open merge and tag the release commit:

```sh
git add pom.xml && git commit -m "merge branch factorizer"

git tag "RELEASE-1.0.0"

# show log of merged branch
git log --oneline --all --graph
```
```
*   ef40d7a (HEAD -> release, tag: RELEASE-1.0.0) merge branch factorizer
|\
| * cba7669 (factorizer) add FactorizerTests
| * b2ac291 refactoring groupId: "de.factorizer"
| * 2fe6eeb add Factorizer
* | 39fe1b8 update pom.xml, GAV to 'de.factorizer' 'RELEASE-1.0.0'
|/
* 52c981d (main) add pom.xml src
* b97a250 add .gitignore
* fb58d32 (tag: root) root commit (empty)
```

<img src="https://raw.githubusercontent.com/sgra64/mvn-fun/refs/heads/markup/img/git-log-after-merge.png" width="600"/>

&nbsp;

Double-check the code builds cleanly and works for the release:

```sh
mvn clean compile           # clean rebuild before running the code

mvn test                    # run unit tests -> BUILD SUCCESS

java de.factorizer.App 3 27 1092 65536 10952347 100000039
```

Output:

```
Hello Factors!
 - n=3 -> [3] (prime number)
 - n=27 -> [3, 3, 3]
 - n=1092 -> [2, 2, 3, 7, 13]
 - n=65536 -> [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
 - n=10952347 -> [7, 23, 59, 1153]
 - n=100000039 -> [100000039] (prime number)
```

Commit with message `"changed version in pom.xml to: RELEASE-1.0.0"` to the *release*-branch
and tag the commit with `RELEASE-1.0.0`.

Push branches:

- `main`,

- `factorizer`,

- `release`

to a remote repository: `mvn-fun` you can create at
[*BHT GitLab*](https://gitlab.bht-berlin.de/)
or another Git service such as
[*GitHub*](https://github.com/). -->