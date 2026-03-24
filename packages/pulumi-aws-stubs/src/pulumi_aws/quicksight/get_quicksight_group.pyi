

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetQuicksightGroupResult', 'AwaitableGetQuicksightGroupResult', 'get_quicksight_group', 'get_quicksight_group_output']
@pulumi.output_type
class GetQuicksightGroupResult:
    
    def __init__(__self__, arn=..., aws_account_id=..., description=..., group_name=..., id=..., namespace=..., principal_id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetQuicksightGroupResult(GetQuicksightGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetQuicksightGroupResult]:
        ...
    


def get_quicksight_group(aws_account_id: Optional[_builtins.str] = ..., group_name: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetQuicksightGroupResult:
    
    ...

def get_quicksight_group_output(aws_account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., namespace: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetQuicksightGroupResult]:
    
    ...

