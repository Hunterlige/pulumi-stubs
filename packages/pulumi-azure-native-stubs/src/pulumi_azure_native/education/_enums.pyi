

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['StudentRole']
@pulumi.type_token("azure-native:education:StudentRole")
class StudentRole(_builtins.str, Enum):
    
    STUDENT = ...
    ADMIN = ...


