

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListProvisionedClusterInstanceUserKubeconfigResult', ..., 'list_provisioned_cluster_instance_user_kubeconfig', ...]
@pulumi.output_type
class ListProvisionedClusterInstanceUserKubeconfigResult:
    
    def __init__(__self__, error=..., id=..., name=..., properties=..., resource_id=..., status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ListCredentialResponseResponseError]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ListCredentialResponseResponseProperties:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


class AwaitableListProvisionedClusterInstanceUserKubeconfigResult(ListProvisionedClusterInstanceUserKubeconfigResult):
    def __await__(self): # -> Generator[Never, Any, ListProvisionedClusterInstanceUserKubeconfigResult]:
        ...
    


def list_provisioned_cluster_instance_user_kubeconfig(connected_cluster_resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListProvisionedClusterInstanceUserKubeconfigResult:
    
    ...

def list_provisioned_cluster_instance_user_kubeconfig_output(connected_cluster_resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListProvisionedClusterInstanceUserKubeconfigResult]:
    
    ...

