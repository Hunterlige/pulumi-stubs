

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
__all__ = ['BindingPropertiesResponse', 'ComponentPropertiesResponse', 'ExtendedLocationResponse', 'ReconciliationPolicyResponse', 'SystemDataResponse', 'TargetSelectorPropertiesResponse', 'TopologiesPropertiesResponse']
@pulumi.output_type
class BindingPropertiesResponse(dict):
    
    def __init__(__self__, *, config: Any, provider: _builtins.str, role: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ComponentPropertiesResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str, dependencies: Optional[Sequence[_builtins.str]] = ..., properties: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class ExtendedLocationResponse(dict):
    
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
class ReconciliationPolicyResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, interval: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.str]:
        
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
    


@pulumi.output_type
class TargetSelectorPropertiesResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TopologiesPropertiesResponse(dict):
    
    def __init__(__self__, *, bindings: Optional[Sequence[outputs.BindingPropertiesResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bindings(self) -> Optional[Sequence[outputs.BindingPropertiesResponse]]:
        
        ...
    


