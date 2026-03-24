

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ContainerGroupProfileResponse', 'ContainerGroupPropertiesResponse', 'StandbyContainerGroupPoolElasticityProfileResponse', 'StandbyVirtualMachinePoolElasticityProfileResponse', 'SubnetResponse', 'SystemDataResponse']
@pulumi.output_type
class ContainerGroupProfileResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, revision: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ContainerGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_group_profile: outputs.ContainerGroupProfileResponse, subnet_ids: Optional[Sequence[outputs.SubnetResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerGroupProfile")
    def container_group_profile(self) -> outputs.ContainerGroupProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[outputs.SubnetResponse]]:
        
        ...
    


@pulumi.output_type
class StandbyContainerGroupPoolElasticityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_ready_capacity: _builtins.float, refill_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReadyCapacity")
    def max_ready_capacity(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refillPolicy")
    def refill_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StandbyVirtualMachinePoolElasticityProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_ready_capacity: _builtins.float, min_ready_capacity: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReadyCapacity")
    def max_ready_capacity(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReadyCapacity")
    def min_ready_capacity(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SubnetResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


