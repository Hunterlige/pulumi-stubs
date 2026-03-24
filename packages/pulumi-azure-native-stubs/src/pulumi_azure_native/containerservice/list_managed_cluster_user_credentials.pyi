

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListManagedClusterUserCredentialsResult', 'AwaitableListManagedClusterUserCredentialsResult', 'list_managed_cluster_user_credentials', 'list_managed_cluster_user_credentials_output']
@pulumi.output_type
class ListManagedClusterUserCredentialsResult:
    
    def __init__(__self__, kubeconfigs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.CredentialResultResponse]:
        
        ...
    


class AwaitableListManagedClusterUserCredentialsResult(ListManagedClusterUserCredentialsResult):
    def __await__(self): # -> Generator[Never, Any, ListManagedClusterUserCredentialsResult]:
        ...
    


def list_managed_cluster_user_credentials(format: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., server_fqdn: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListManagedClusterUserCredentialsResult:
    
    ...

def list_managed_cluster_user_credentials_output(format: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., server_fqdn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListManagedClusterUserCredentialsResult]:
    
    ...

