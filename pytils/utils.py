# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_utils -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Misc utils for internal use
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

def provide_unicode(stext, encoding, default=u"неизвестно"):
    """
    Provide Unicode from text
    
    @param stext: text
    @type stext: C{str}
    
    @param encoding: encoding if input text
    @type encoding: C{str}
    
    @return: C{unicode}
    """
    try:
        utext = str(stext).decode(encoding)
    except UnicodeDecodeError:
        utext = default
    return utext

def provide_str(utext, encoding, default="unknown"):
    """
    Provide text from Unicode
    
    @param utext: unicode text
    @type utext: C{unicode}
    
    @param encoding: encoding of output text
    @type encoding: C{str}
    
    @return: C{str}
    """
    try:
        stext = unicode(utext).encode(encoding)
    except UnicodeEncodeError:
        stext = default
    return stext
