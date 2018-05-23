# regex2grok
Simplify the steps from regex to grok format.


## Installation

Create virtualenv:
```bash
$ virtualenv .env-python
$ source .env-python/bin/activate
(.env-python) $
```

Install **regex2grok**:
```bash
(.env-python) $ python setup.py install
```

Usage:
```bash
(.env-python) $ regex2grok -h
Usage:
    regex2grok.py <regex_rules_file>
    regex2grok.py <regex_rules_file> <output_grok_template>
    regex2grok.py (-h | --help)
Options:
    -h --help               Show usage.
    <regex_rules_file>      The input RegEx rules file path.
    <output_grok_template>  The output grok template file path.
```

Run:
```bash
(.env-python) $ regex2grok input.ref.template 
```
