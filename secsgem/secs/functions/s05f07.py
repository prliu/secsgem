#####################################################################
# s05f07.py
#
# (c) Copyright 2021, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################
"""Class for stream 05 function 07."""

from .base import SecsStreamFunction


class SecsS05F07(SecsStreamFunction):
    """
    list enabled alarms - request.

    **Structure**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS05F07
        Header only

    **Example**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS05F07()
        S5F7 W .

    :param value: parameters for this function (see example)
    :type value: list
    """

    _stream = 5
    _function = 7

    _data_format = None

    _to_host = False
    _to_equipment = True

    _has_reply = True
    _is_reply_required = True

    _is_multi_block = False