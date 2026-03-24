

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListManagedClusterMonitoringUserCredentialsResult', ..., 'list_managed_cluster_monitoring_user_credentials', ...]
@pulumi.output_type
class ListManagedClusterMonitoringUserCredentialsResult:
    
    def __init__(__self__, kubeconfigs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.CredentialResultResponse]:
        
        ...
    


class AwaitableListManagedClusterMonitoringUserCredentialsResult(ListManagedClusterMonitoringUserCredentialsResult):
    def __await__(self): # -> Generator[Never, Any, ListManagedClusterMonitoringUserCredentialsResult]:
        ...
    


def list_managed_cluster_monitoring_user_credentials(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., server_fqdn: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListManagedClusterMonitoringUserCredentialsResult:
    
    ...

def list_managed_cluster_monitoring_user_credentials_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., server_fqdn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListManagedClusterMonitoringUserCredentialsResult]:
    
    ...

