

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListApplianceClusterUserCredentialResult', 'AwaitableListApplianceClusterUserCredentialResult', 'list_appliance_cluster_user_credential', 'list_appliance_cluster_user_credential_output']
@pulumi.output_type
class ListApplianceClusterUserCredentialResult:
    
    def __init__(__self__, hybrid_connection_config=..., kubeconfigs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridConnectionConfig")
    def hybrid_connection_config(self) -> outputs.HybridConnectionConfigResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.ApplianceCredentialKubeconfigResponse]:
        
        ...
    


class AwaitableListApplianceClusterUserCredentialResult(ListApplianceClusterUserCredentialResult):
    def __await__(self): # -> Generator[Never, Any, ListApplianceClusterUserCredentialResult]:
        ...
    


def list_appliance_cluster_user_credential(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListApplianceClusterUserCredentialResult:
    
    ...

def list_appliance_cluster_user_credential_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListApplianceClusterUserCredentialResult]:
    
    ...

