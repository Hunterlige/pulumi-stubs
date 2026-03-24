

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccountResult', 'AwaitableGetAccountResult', 'get_account', 'get_account_output']
@pulumi.output_type
class GetAccountResult:
    
    def __init__(__self__, account_id=..., arn=..., email=..., id=..., joined_method=..., joined_timestamp=..., name=..., parent_id=..., state=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetAccountResult(GetAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetAccountResult]:
        ...
    


def get_account(account_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccountResult:
    
    ...

def get_account_output(account_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccountResult]:
    
    ...

