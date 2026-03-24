

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListApplicationTokensResult', 'AwaitableListApplicationTokensResult', 'list_application_tokens', 'list_application_tokens_output']
@pulumi.output_type
class ListApplicationTokensResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ManagedIdentityTokenResponse]]:
        
        ...
    


class AwaitableListApplicationTokensResult(ListApplicationTokensResult):
    def __await__(self): # -> Generator[Never, Any, ListApplicationTokensResult]:
        ...
    


def list_application_tokens(application_name: Optional[_builtins.str] = ..., authorization_audience: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Sequence[_builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListApplicationTokensResult:
    
    ...

def list_application_tokens_output(application_name: Optional[pulumi.Input[_builtins.str]] = ..., authorization_audience: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., user_assigned_identities: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListApplicationTokensResult]:
    
    ...

