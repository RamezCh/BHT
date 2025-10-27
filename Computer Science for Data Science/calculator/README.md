# Solution A2: Creating a Python Project

This assignment demonstrates **best practices** for creating and structuring a Python project.  
While conventions may vary between languages, several general rules should always be followed when setting up a new software project.

---

## General Project Structure

- Source code resides in the `src/` directory of the project.
- Test code (unit tests) is **always** separated from the source code and typically resides in a `tests/` directory.
- Both `src/` and `tests/` can have subdirectories to further organize the code.
  - The structure under `tests/` should **mirror** the structure under `src/`.
- Only **source code** is checked into version control (e.g., Git) — no build artifacts, tools, or binaries.
- A **build process** must be clearly defined so the project can be built from scratch at any time.

> Note: Python does not enforce any particular project structure (unlike Java/Maven).  
> You are responsible for maintaining a clear, consistent organization.

---

## Recommended Reading

Ken Reitz’s article  
[**"Structuring Your Project"**](https://docs.python-guide.org/writing/structure)  
is a highly regarded guide on Python project layout and best practices.  
Although opinions vary, this structure is widely adopted and provides a solid foundation.

---

## Assignment Goal

Set up a new **Python project** following the best practices from the above article.

The project will include two components:

### Calculator

A singleton component that implements:

- `add(a, b)` → returns the sum of *a* and *b*  
- `sub(a, b)` → subtracts *b* from *a*  
- `mul(a, b)` → multiplies *a* and *b*  
- `div(a, b)` → divides *a* by *b*  
- `factorize(n)` → returns the prime factors of *n*

### Collection

An instantiable component that provides list and set operations:

- `contains(s, e)` → counts how many times element *e* appears in *s*  
- `zip(s, p)` → pairs consecutive elements from *s* and *p*  
- `pset(s)` → calculates the powerset of *s*  
- `perm(p)` → computes all permutations of *p*

---

## Steps

1. [**Answer Questions for Python Project Setup**](#1-answer-questions-for-python-project-setup)  
2. [**Create the project: `py-fun`**](#2-create-project-py-fun)  
3. [**Build the project**](#3-build-the-project)  
4. [**Create the Calculator**](#4-create-the-calculator)  
5. [**Run the Calculator**](#5-run-the-calculator)  
6. [**Extend the Calculator**](#6-extend-the-calculator)  
7. [**Check project into a local Git repository**](#7-check-project-into-local-git-repository)  
8. [**Push the project to a remote Git repository**](#8-push-project-to-remote-git-repository)  
9. [**Add Unit Tests**](#9-unit-tests)

---

## Answer Questions for *Python* Project Setup

1. **What is a project scaffold?**  
   → The initial structure or template of a project. It defines the directory layout, configuration files, and boilerplate code.

2. **What is a software build process?**  
   → A sequence of steps that convert source code into a runnable artifact (e.g., executable, library, or package).  
   In Python, this typically means creating a distributable package (`.whl` or `.tar.gz`) rather than compiling machine code.

3. **When does the build process start and end?**  
   → It starts once the source code and dependencies are ready and ends when a runnable or deployable artifact is produced.  
   Example: *Start → Code + Dependencies → Testing → Packaging → End*

4. **What are the steps and results of the build process?**  
   → Typical steps include:
   - Fetch dependencies (`requirements.txt`)
   - Compile/preprocess code (if needed)
   - Run tests
   - Bundle/package the output
   - Deploy or publish the artifact

5. **What is `make`?**  
   → `make` is a build automation tool that uses a *Makefile* to define build rules and dependencies.

6. **What is the purpose of `requirements.txt`?**  
   → Lists all project dependencies. Install them with:  
     ```bash
     pip install -r requirements.txt
     ```

7. **What is a Build Server? (for Python)**  
   → A dedicated system that automatically runs builds whenever code changes (e.g., via Git push).  
     Examples: GitHub Actions, Jenkins, CircleCI.  
     For Python, it typically:
     - Sets up a virtual environment  
     - Installs dependencies  
     - Runs tests  
     - Builds and optionally deploys the package

8. **What are Nightly Builds?**  
   → Automated builds created on a schedule (e.g., every night).  
     They include the latest code and help detect regressions early. Common in Continuous Integration (CI) pipelines.

9. **What are the differences between Scripts, Modules, Packages, and Libraries?**
   - **Script** → executable file (e.g., `main.py`)  
   - **Module** → a file with functions, classes, or variables that can be imported  
   - **Package** → a directory of modules containing an `__init__.py` file  
   - **Library** → a reusable collection of modules/packages (e.g., `numpy`, `requests`)

10. **What is `__init__.py` used for?**
    → Marks a directory as a Python package so it can be imported.  
       The `__all__` variable can be used to define which symbols get exported.

---

## Example: Show Project Scaffold

```bash
find .    # display project structure
```
**NOTE** Adding -n after make shows the steps without execution