# FOAL

[![PyPI version](https://badge.fury.io/py/foal.svg)](https://badge.fury.io/py/foal)

FOAL (From Organization Acronyms Lookup) is a tool to lookup acronyms from a set
of YAML files.

Given multiple YAML files that define acronyms and abbreviations, merge the
dictionaries in a contextually-sensitive order and lookup acronyms.

<!--TOC-->

- [What](#what)
- [Why](#why)
- [About the data structure](#about-the-data-structure)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [From source](#from-source)
- [Development](#development)

<!--TOC-->


## What

Define acronyms and abbreviations in context-aware files, then
merge and lookup definitions with the ability to prioritize the context.

For example, given these files:

```yaml
# technology.yaml

acronyms:
    cpu:
        shortform: CPU
        longform: Central Processing Unit

    eps:
        shortform: EPS
        longform: Encapsulated Postscript
```

```yaml
# finance.yaml

acronyms:
    cogs:
        shortform: COGS
        longform: Cost of Goods Sold

    cpu:
        shortform: CPU
        longform: Cost per Unit

    eps:
        shortform: EPS
        longform: Earnings per Share
```

Get a dictionary that prefers the technology context:

```shell
$ foal -p technology.yaml
[WARNING] prefer context: ['technology.yaml']
---
acronyms:
    cogs:
        shortform: COGS
        longform: Cost of Goods Sold
        source: finance.yaml
    cpu:
        shortform: CPU
        longform: Central Processing Unit
        source: technology.yaml
    eps:
        shortform: EPS
        longform: Encapsulated Postscript
        source: technology.yaml
```

Get a dictionary that prefers the finance context:

```shell
$ foal -p finance.yaml
[WARNING] prefer context: ['finance.yaml']
---
acronyms:
    cogs:
        shortform: COGS
        longform: Cost of Goods Sold
        source: finance.yaml
    cpu:
        shortform: CPU
        longform: Cost per Unit
        source: finance.yaml
    eps:
        shortform: EPS
        longform: Earnings per Share
        source: finance.yaml
```

Lookup specific acronyms that prefer the technology context:

```shell
$ foal -p technology.yaml -a cpu
[WARNING] prefer context: ['technology.yaml']
---
acronyms:
    cpu:
        shortform: CPU
        longform: Cost per Unit
        source: technology.yaml
```


## Why

It is sometimes necessary to lookup acronyms from a canonical list to use in
documentation. The acronyms (or abbreviations) can then be used in automated
documentation tools via something like
[pandoc-acronyms](https://github.com/scokobro/pandoc-abbreviations).

Acronyms form a vocabulary that people use within their own frame of reference.
The general acceptance of acronyms dependends on multiple factors, such as
political landscape, technical expertise, regional differences, context, and
native tongue.

For example, most people around the world recognize the United States of America
as the **USA**, the United Kingdom as the **UK**, and Germany as the **BRD**
(Bundesrepublik Deutschland). English speakers are more likely to recognize
BRD when it is used in the context of Olympic competition or an international
news broadcast than when BRD appears randomly in a document.

Take another example, **CPU**.

- People in Information Technology (IT)
  immediately think of _Central Processing Unit_.

- People in finance are likely to think of _Cost per Unit_,
  especially when CPU is used in a financial context.

Taken out of context, abbreviations are difficult to interpret and can lead to
misunderstanding in important documents.


## About the data structure

- `global.yaml` within a directory tree is authoritative.<br/>
  Acronyms and abbreviations within `global.yaml` override acronyms from
  other files. This is a global context reserved for acronyms that should
  have universal meaning across an organization. Names of products,
  BUs, and teams are all good choices for `global.yaml`.

- This format does **not** dictate the hierarchy of acronyms from other files
  in the git repo. Only `global.yaml` has special priority. Tool developers
  and authors may choose to incorporate the other files in whatever priority
  makes sense in a given context.

- The definition of "context" for files within a directory tree is left up
  to individual contributors (other than `global.yaml`). Be inclusive.
  [TimTowtdi](https://en.wikipedia.org/wiki/There%27s_more_than_one_way_to_do_it).

A formal [Kwalify](https://directory.fsf.org/wiki/Kwalify) schema
for the format is in [`schema/acronyms.yaml`](schema/acronyms.yaml).


## Installation

### From PyPI

```bash
pip install --user foal
```

### From source

```bash
pip install --user .
```


## Development

Run:

```shell
sdlc/bootstrap
sdlc/build
sdlc/test
```

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`TESTING.md`](TESTING.md).
