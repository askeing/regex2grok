#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# regex2grok
# Create by askeing on 23/05/2018

"""
Usage:
    regex2grok.py <regex_rules_file>
    regex2grok.py <regex_rules_file> <output_grok_template>
    regex2grok.py (-h | --help)
Options:
    -h --help               Show usage.
    <regex_rules_file>      The input RegEx rules file path.
    <output_grok_template>  The output grok template file path.
"""

import os
from docopt import docopt

class Regex2Grok(object):

    GROK_TEMPLATE = """
    grok {{
        break_on_match => false
    {rules}
    }}
    """

    RULE_TEMPLATE = '        match => {{ "message" => "{regex}" }}'

    def __init__(self, regex_rules_file, output_grok_template=None):
        self._validate(regex_rules_file)

        self.regex_rules_file = regex_rules_file
        self.output_grok_template = output_grok_template

    def _validate(self, input_file_path):
        if os.path.isfile(input_file_path):
            return True
        raise Exception('Input path {} is not a file.'.format(input_file_path))

    def run(self):
        ret_rules = []
        with open(self.regex_rules_file, 'r') as input_fh:
            lines = input_fh.readlines()

            for line in lines:
                # comments
                if line.startswith('#'):
                    ret_rules.append('\t{}'.format(line.strip()))
                # empty lines
                elif not line.strip():
                    continue
                else:
                    ret_rules.append(Regex2Grok.RULE_TEMPLATE.format(regex=line.strip()))

        # generate result
        ret = Regex2Grok.GROK_TEMPLATE.format(rules='\n'.join(ret_rules))

        # print result
        print(ret)

        # output result
        if self.output_grok_template:
            with open(self.output_grok_template, 'w') as output_fh:
                output_fh.write(ret)


def main():
    arguments = docopt(__doc__)

    app = Regex2Grok(regex_rules_file=arguments['<regex_rules_file>'], output_grok_template=arguments['<output_grok_template>'])
    app.run()


if __name__ == '__main__':
    main()
