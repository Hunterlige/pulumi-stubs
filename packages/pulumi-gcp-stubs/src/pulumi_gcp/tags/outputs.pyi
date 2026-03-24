

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TagKeyIamBindingCondition', 'TagKeyIamMemberCondition', 'TagValueIamBindingCondition', 'TagValueIamMemberCondition', 'GetTagKeysKeyResult', 'GetTagValuesValueResult']
@pulumi.output_type
class TagKeyIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TagKeyIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TagValueIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TagValueIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetTagKeysKeyResult(dict):
    def __init__(__self__, *, allowed_values_regex: _builtins.str, create_time: _builtins.str, description: _builtins.str, name: _builtins.str, namespaced_name: _builtins.str, parent: _builtins.str, purpose: _builtins.str, purpose_data: Mapping[str, _builtins.str], short_name: _builtins.str, update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValuesRegex")
    def allowed_values_regex(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedName")
    def namespaced_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="purposeData")
    def purpose_data(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetTagValuesValueResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, description: _builtins.str, name: _builtins.str, namespaced_name: _builtins.str, parent: _builtins.str, short_name: _builtins.str, update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedName")
    def namespaced_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


