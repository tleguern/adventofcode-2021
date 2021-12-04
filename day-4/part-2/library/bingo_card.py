#!/usr/bin/python
# -*- coding: utf-8 -*-

#import os
#import re

from ansible.module_utils.basic import AnsibleModule


def bingo_argument_spec():
    return dict(
        card = dict(
            type = "list",
            elements = "int",
            required = True),
        draws = dict(
            type = "list",
            elements = "int",
            required = True),
    )


if __name__ == '__main__':
    module_args = bingo_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    result = dict(
        changed=False,
        debug=[],
        msg=""
    )
    card = module.params["card"]
    draws = module.params["draws"]

    # Check lines
    for i in [0, 1, 2, 3, 4]:
        line = card[0 + i * 5:5 + i * 5]
        if all([ x in draws for x in line ]):
            result['changed'] = True
            result['msg'] = "Victory on line {}.".format(i + 1)

    # Check rows
    for i in [0, 1, 2, 3, 4]:
        row = card[0 + i:25:5]
        if all([ x in draws for x in row ]):
            result['changed'] = True
            result['msg'] = "Victory on row {}.".format(i + 1)

    module.exit_json(**result)
