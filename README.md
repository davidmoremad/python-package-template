# 🐍 Your Python package

## ✋ Edit before to use

Before to publish your new python package, edit these lines:
 - `Copyrights`: You should edit and add copyrights on every file with your name
 - `./setup.py`: Ensure all data is correct. You should edit the global variables and check the setup method
 - `./package/__init__.py`: Fill with your information
 - `./.github/workflows/`: There are 2 github workflows to automate Pypi publishing and Release creation

## 📚 Files explanation

* **setup.py**: Installer of your package
* **VERSION**: Version of your package. It will be published to pypi and can't be overwritten
* **LICENSE**: License of your package. (Current: MIT License). If you want to change license you need to change it on every file
* **requirements.txt**: Dependencies of your package. They'll be installed when someone installs your package
* **requirements-dev.txt**: Dependencies only for testing or CI pipelines

## 🤖 Github Actions

There are 2 actions on your `.github/workflows`:
* **test.yaml**: Build and lint your code every time you create a new PR
* **release.yaml**: Triggered on `VERSION` changes. After to built, lint and test, 
it publish package to Pypi and create a new Tag and Release in Github


## ☁️ Publish to Pypi

If you want to publish your package manually, these are the steps to follow:

1. Ensure your project is well-formatted (setup.py, packages, everything...)
2. Install needed packages: `python -m pip install –-user –-upgrade setuptools wheel twine`
3. Create package: `python setup.py sdist bdist_wheel`
4. Install & check if works properly: `pip install -e`
5. Upload to Test-Pypi: `twine upload —-repository testpypi dist/*`
5. Upload to Pypi: `twine upload dist/*`