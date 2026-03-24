

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IndexTimeouts', 'SearchResourceResult', 'SearchResourceCountResult', 'SearchResourcePropertyResult', 'ViewFilters', 'ViewIncludedProperty']
@pulumi.output_type
class IndexTimeouts(dict):
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
    


@pulumi.output_type
class SearchResourceResult(dict):
    def __init__(__self__, *, arn: _builtins.str, last_reported_at: _builtins.str, owning_account_id: _builtins.str, properties: Sequence[outputs.SearchResourcePropertyResult], region: _builtins.str, resource_type: _builtins.str, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReportedAt")
    def last_reported_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="owningAccountId")
    def owning_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Sequence[outputs.SearchResourcePropertyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SearchResourceCountResult(dict):
    def __init__(__self__, *, complete: _builtins.bool, total_resources: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def complete(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalResources")
    def total_resources(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class SearchResourcePropertyResult(dict):
    def __init__(__self__, *, data: _builtins.str, last_reported_at: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReportedAt")
    def last_reported_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ViewFilters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterString")
    def filter_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ViewIncludedProperty(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


