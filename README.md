
![heavy-wait](img/heavy-wait-logo.png)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/mechregard/heavy-wait)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mechregard/heavy-wait)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
![Keybase PGP](https://img.shields.io/keybase/pgp/dlange)
![PyPI](https://img.shields.io/pypi/v/heavywait)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/heavywait)

`heavy-wait` is a tool which can decorate markdown with LLM generated content. 
Lumbering companion to [light-wait](https://github.com/mechregard/light-wait)

Light-wait generates a static blog site from markdown, including label (tag) based navigation.
The metadata required by light-wait (labels, titles) along with additional helpful content, is automatically 
generated by heavy-wait.

Your original markdown:
```
# Some markdown
this is all well and good
```
Your decorated markdown, thanks to Heavy-wait:
```
description: a short description of your markdown
labels: a set of labels used to catagorize your markdown
keywords: up to 5 keywords from your markdown

A few sentence summary of your markdown.

# Some markdown
this is all well and good

A list of up to 3 supporting links based on the content of your markdown
```

## Usage
To call `heavywait` you need an OpenAI API key. Set the following ENV vars:

- OPENAI_API_KEY
- OPENAI_ORG

The `heavywait` CLI is called `hw`. Use `--help` for usage:

```
Usage: hw [OPTIONS] COMMAND [ARGS]...

  Heavywait is a CLI for decorating markdown files or directories of markdown
  files with AI generated metadata

Options:
  --help  Show this message and exit.

Commands:
  dir   Decorate files in given directory with AI generated metadata
  file  Decorate given markdown file with AI generated metadata
```

## Quick Start

Install with pip

    + `$ pip install heavywait`


Decorate a single markdown file:
```
% hw file tests/resources/src/efficient-transformers.md tests/resources/dst/efficient-transformers.md
Wrote tests/resources/dst/efficient-transformers.md
```

Decorate a directory of markdown files:
```
% hw dir tests/resources/src tests/resources/dst                                                     
Wrote tests/resources/dst/efficient-transformers.md
```

## Tool Chain and Frameworks
The following frameworks and tools enable Heavy-wait:

* https://github.com/hwchase17/langchain
* https://platform.openai.com/docs/api-reference
* https://python-poetry.org/docs/


## How to Contribute
1. Clone repo and create a new branch: `$ git checkout https://github.com/mechregard/heavy-wait -b name_for_new_branch`.
2. Make changes and test
3. Submit Pull Request with comprehensive description of changes

#### Details
Config pypi test repo:
```
poetry config repositories.test-pypi https://test.pypi.org/legacy/
```

## Donations
This is free, open-source software. 

Image credit goes to: `some random movie fan`
