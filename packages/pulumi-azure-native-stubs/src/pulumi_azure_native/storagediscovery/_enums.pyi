import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["StorageDiscoveryResourceType", "StorageDiscoverySku"]

@pulumi.type_token(...)
class StorageDiscoveryResourceType(_builtins.str, Enum):
    STORAGE_ACCOUNTS = ...

@pulumi.type_token("azure-native:storagediscovery:StorageDiscoverySku")
class StorageDiscoverySku(_builtins.str, Enum):
    STANDARD = ...
    FREE = ...
