#####################################################################
# rsdc.py
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
"""RSDC data item."""
from .. import variables
from .base import DataItemBase


class RSDC(DataItemBase):
    """
    Request spooled data command.

    :Types:
       - :class:`SecsVarU1 <secsgem.secs.variables.SecsVarU1>`

    **Used In Function**
        - :class:`SecsS06F23 <secsgem.secs.functions.SecsS06F23>`

    """

    __type__ = variables.U1
    __count__ = 1

    TRANSMIT = 0
    PURGE = 1
