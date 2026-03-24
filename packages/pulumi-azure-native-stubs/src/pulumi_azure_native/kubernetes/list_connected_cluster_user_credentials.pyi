

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListConnectedClusterUserCredentialsResult', 'AwaitableListConnectedClusterUserCredentialsResult', 'list_connected_cluster_user_credentials', 'list_connected_cluster_user_credentials_output']
@pulumi.output_type
class ListConnectedClusterUserCredentialsResult:
    
    def __init__(__self__, hybrid_connection_config=..., kubeconfigs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridConnectionConfig")
    def hybrid_connection_config(self) -> outputs.HybridConnectionConfigResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.CredentialResultResponse]:
        
        ...
    


class AwaitableListConnectedClusterUserCredentialsResult(ListConnectedClusterUserCredentialsResult):
    def __await__(self): # -> Generator[Never, Any, ListConnectedClusterUserCredentialsResult]:
        ...
    


def list_connected_cluster_user_credentials(authentication_method: Optional[Union[_builtins.str, AuthenticationMethod]] = ..., client_proxy: Optional[_builtins.bool] = ..., cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListConnectedClusterUserCredentialsResult:
    
    ...

def list_connected_cluster_user_credentials_output(authentication_method: Optional[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]] = ..., client_proxy: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListConnectedClusterUserCredentialsResult]:
    
    ...

