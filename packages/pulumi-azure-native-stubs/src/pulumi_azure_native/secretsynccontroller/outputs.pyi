

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
__all__ = [..., 'KubernetesSecretObjectMappingResponse', 'SecretSyncConditionResponse', 'SecretSyncStatusResponse', 'SystemDataResponse']
@pulumi.output_type
class AzureResourceManagerCommonTypesExtendedLocationResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KubernetesSecretObjectMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_path: _builtins.str, target_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePath")
    def source_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetKey")
    def target_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecretSyncConditionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: _builtins.str, message: _builtins.str, observed_generation: _builtins.float, reason: _builtins.str, status: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecretSyncStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Sequence[outputs.SecretSyncConditionResponse], last_successful_sync_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.SecretSyncConditionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulSyncTime")
    def last_successful_sync_time(self) -> _builtins.str:
        
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
    


