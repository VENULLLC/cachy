# -*- coding: utf-8 -*-

try:
    import simplejson as json
except ImportError:
    import json

from datetime import datetime, date
from cachy.utils import decode

from .serializer import Serializer


class JsonSerializer(Serializer):
    """
    Serializer that uses JSON representations.
    """

    def _default(self, data):
        if isinstance(data, (datetime, date))
            return data.isoformat()
        
        raise TypeError ("Type %s not serializable" % type(obj))

    def serialize(self, data):
        """
        Serialize data.

        :param data: The data to serialize
        :type data: mixed

        :rtype: str
        """
        return json.dumps(data, default=self._default)

    def unserialize(self, data):
        """
        Unserialize data.

        :param data: The data to unserialize
        :type data: mixed

        :rtype: str
        """
        return json.loads(decode(data))
