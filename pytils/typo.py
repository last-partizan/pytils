# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_typo -*-
# pytils - simple processing for russian strings
# Copyright (C) 2006-2008  Yury Yurevich
#
# http://www.pyobject.ru/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Russian typography
"""

def testrule(x):
    """
    Rule for tests. Do nothing.
    """
    return x

def _get_rule_by_name(name):
    f = testrule
    f.__name__ = name
    return f

def _resolve_rule_name(rule_or_name, forced_name=None):
    if isinstance(rule_or_name, str):
        # got name
        name = rule_or_name
        rule = _get_rule_by_name(name)
    elif callable(rule_or_name):
        # got rule
        name = rule_or_name.__name__
        rule = rule_or_name
    else:
        raise ValueError(
            "Cannot resolve %r: neither rule, nor name" % 
            rule_or_name)
    if forced_name is not None:
        name = forced_name
    return name, rule

class Typography(object):
    """
    Russian typography rules applier
    """
    def __init__(self, *args, **kwargs):
        """
        Typography applier constructor:
        
        possible variations of constructing rules chain:
            rules by it's names:
                Typography('first_rule', 'second_rule')
            rules callables as is:
                Typography(cb_first_rule, cb_second_rule)
            mixed:
                Typography('first_rule', cb_second_rule)
            as list:
                Typography(['first_rule', cb_second_rule])
            as keyword args:
                Typography(rule_name='first_rule', 
                           another_rule=cb_second_rule)
            as dict (order of rule execution is not the same):
                Typography({'rule name': 'first_rule', 
                            'another_rule': cb_second_rule})
        
        For standard rules it is recommended to use list of rules
        names.
            Typography(['first_rule', 'second_rule'])
        
        For custom rules which are named functions, 
        it is recommended to use list of callables:
            Typography([cb_first_rule, cb_second_rule])
        
        For custom rules which are lambda-functions,
        it is recommended to use dict:
            Typography({'rule_name': lambda x: x})
            
        I.e. the recommended usage is:
            Typography(['standard_rule_1', 'standard_rule_2'],
                       [cb_custom_rule1, cb_custom_rule_2],
                       {'custom_lambda_rule': lambda x: x})
        """     
        self.rules = {}
        self.rules_names = []
        # first of all, expand args-lists and args-dicts
        expanded_args = []
        expanded_kwargs = {}
        for arg in args:
            if isinstance(arg, (tuple, list)):
                expanded_args += list(arg)
            elif isinstance(arg, dict):
                expanded_kwargs.update(arg)
            elif isinstance(arg, str) or callable(arg):
                expanded_args.append(arg)
            else:
                raise TypeError(
                    "Cannot expand arg %r, must be tuple, list,"\
                    " dict, str or callable, not" % 
                    (arg, type(arg).__name__))
        for kw, arg in kwargs.items():
            if isinstance(arg, str) or callable(arg):
                expanded_kwargs[kw] = arg
            else:
                raise TypeError(
                    "Cannot expand kwarg %r, must be str or "\
                    "callable, not" % (arg, type(arg).__name__))
        # next, resolve rule names to callables
        for name, rule in (_resolve_rule_name(a) for a in expanded_args):
            self.rules[name] = rule
            self.rules_names.append(name)
        for name, rule in (_resolve_rule_name(a, k) for k, a in expanded_kwargs.items()):
            self.rules[name] = rule
            self.rules_names.append(name)

