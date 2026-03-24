

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterEncryptionDetailArgs', 'ClusterEncryptionDetailArgsDict', 'ClusterMultiRegionPropertiesArgs', 'ClusterMultiRegionPropertiesArgsDict', 'ClusterPeeringTimeoutsArgs', 'ClusterPeeringTimeoutsArgsDict', 'ClusterTimeoutsArgs', 'ClusterTimeoutsArgsDict']
class ClusterEncryptionDetailArgsDict(TypedDict):
    encryption_status: pulumi.Input[_builtins.str]
    encryption_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClusterEncryptionDetailArgs:
    def __init__(__self__, *, encryption_status: pulumi.Input[_builtins.str], encryption_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionStatus")
    def encryption_status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_status.setter
    def encryption_status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClusterMultiRegionPropertiesArgsDict(TypedDict):
    clusters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    witness_region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterMultiRegionPropertiesArgs:
    def __init__(__self__, *, clusters: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., witness_region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @clusters.setter
    def clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="witnessRegion")
    def witness_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @witness_region.setter
    def witness_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterPeeringTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterPeeringTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


