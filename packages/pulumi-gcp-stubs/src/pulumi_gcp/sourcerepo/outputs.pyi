

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RepositoryIamBindingCondition', 'RepositoryIamMemberCondition', 'RepositoryPubsubConfig', 'GetRepositoryPubsubConfigResult']
@pulumi.output_type
class RepositoryIamBindingCondition(dict):
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
class RepositoryIamMemberCondition(dict):
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
class RepositoryPubsubConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, message_format: _builtins.str, topic: _builtins.str, service_account_email: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetRepositoryPubsubConfigResult(dict):
    def __init__(__self__, *, message_format: _builtins.str, service_account_email: _builtins.str, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        ...
    


