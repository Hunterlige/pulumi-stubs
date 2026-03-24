

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['AllowCrashDumpCollection', 'OSFeedType', 'RegionalDataBoundary', 'UpdatePolicy']
@pulumi.type_token("azure-native:azuresphere:AllowCrashDumpCollection")
class AllowCrashDumpCollection(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:azuresphere:OSFeedType")
class OSFeedType(_builtins.str, Enum):
    
    RETAIL = ...
    RETAIL_EVAL = ...


@pulumi.type_token("azure-native:azuresphere:RegionalDataBoundary")
class RegionalDataBoundary(_builtins.str, Enum):
    
    NONE = ...
    EU = ...


@pulumi.type_token("azure-native:azuresphere:UpdatePolicy")
class UpdatePolicy(_builtins.str, Enum):
    
    UPDATE_ALL = ...
    NO3RD_PARTY_APP_UPDATES = ...


