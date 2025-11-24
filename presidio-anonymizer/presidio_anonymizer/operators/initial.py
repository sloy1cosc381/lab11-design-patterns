"""Replaces the PII text entity with initials"""
import re
from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """Leave only the initials of the given string"""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: the initials of the string."""
        def multiword(s):
            if s==None:
                return ""
            else:
                return s.group()
        letters=(re.search(r'^[^a-zA-Z0-9]*[a-zA-Z0-9]',text).group()+multiword(re.search(r' [a-zA-Z0-9]',text))).upper()
        letlist=letters.split()
        return ". ".join(letlist)+"."

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize