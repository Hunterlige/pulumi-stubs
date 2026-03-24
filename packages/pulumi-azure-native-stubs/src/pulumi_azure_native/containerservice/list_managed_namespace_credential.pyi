

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListManagedNamespaceCredentialResult', 'AwaitableListManagedNamespaceCredentialResult', 'list_managed_namespace_credential', 'list_managed_namespace_credential_output']
@pulumi.output_type
class ListManagedNamespaceCredentialResult:
    
    def __init__(__self__, kubeconfigs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.CredentialResultResponse]:
        
        ...
    


class AwaitableListManagedNamespaceCredentialResult(ListManagedNamespaceCredentialResult):
    def __await__(self): # -> Generator[Never, Any, ListManagedNamespaceCredentialResult]:
        ...
    


def list_managed_namespace_credential(managed_namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListManagedNamespaceCredentialResult:
    
    ...

def list_managed_namespace_credential_output(managed_namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListManagedNamespaceCredentialResult]:
    
    ...

