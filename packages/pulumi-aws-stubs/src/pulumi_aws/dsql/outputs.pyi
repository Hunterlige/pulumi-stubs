

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterEncryptionDetail', 'ClusterMultiRegionProperties', 'ClusterPeeringTimeouts', 'ClusterTimeouts']
@pulumi.output_type
class ClusterEncryptionDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encryption_status: _builtins.str, encryption_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionStatus")
    def encryption_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ClusterMultiRegionProperties(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, clusters: Optional[Sequence[_builtins.str]] = ..., witness_region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusters(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="witnessRegion")
    def witness_region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterPeeringTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClusterTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


