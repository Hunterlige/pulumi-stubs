

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListManagedClusterAdminCredentialsResult', 'AwaitableListManagedClusterAdminCredentialsResult', 'list_managed_cluster_admin_credentials', 'list_managed_cluster_admin_credentials_output']
@pulumi.output_type
class ListManagedClusterAdminCredentialsResult:
    
    def __init__(__self__, kubeconfigs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.CredentialResultResponse]:
        
        ...
    


class AwaitableListManagedClusterAdminCredentialsResult(ListManagedClusterAdminCredentialsResult):
    def __await__(self): # -> Generator[Never, Any, ListManagedClusterAdminCredentialsResult]:
        ...
    


def list_managed_cluster_admin_credentials(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., server_fqdn: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListManagedClusterAdminCredentialsResult:
    
    ...

def list_managed_cluster_admin_credentials_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., server_fqdn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListManagedClusterAdminCredentialsResult]:
    
    ...

