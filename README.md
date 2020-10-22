# cookiecutter-fchorney

CookieCutter template for my personal python projects

## Requirements
Install `cookiecutter` command line: `pip install cookiecutter`

## Usage

Generate a new Cookiecutter template layout: `cookiecutter https://github.com/fchorney/cookiecutter-fchorney`

If you have the `cookiecutter-fchorney` project checked out, you can just reference the local folder: `cookiecutter ./cookiecutter-fchorney`

## cookiecutter.json

The cookiecutter.json file contains a list of options that you will be prompted for when you create a new project. This section will offer some insight into those options.

- full\_name:
  - Your full name.
- email:
  - Your GitHub email.
- project\_name:
  - The human readable name for the project.
- project\_slug:
  - The actual python package name. Follow this [naming guide](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)
- project\_short\_description:
  - Short project description.
- release\_date:
  - The release date of the package.
- version:
  - The version to start this project on.
- is\_executable:
  - Select "yes" if your python package will be run as an executable rather than being a pure library.

## Development Note
`{{cookiecutter.project\_slug}}/init.sh` is git-ignored in its respective folder so that when the project is created it doesnt think `init.sh` is actually part of the new project. Thus if you need to edit `init.sh` in the future, make sure to `git add -f init.sh` so that it force adds it.
