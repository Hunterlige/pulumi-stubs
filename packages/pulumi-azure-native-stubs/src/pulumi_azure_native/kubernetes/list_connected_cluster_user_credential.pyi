import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListConnectedClusterUserCredentialResult",
    "AwaitableListConnectedClusterUserCredentialResult",
    "list_connected_cluster_user_credential",
    "list_connected_cluster_user_credential_output",
]

@pulumi.output_type
class ListConnectedClusterUserCredentialResult:
    def __init__(__self__, hybrid_connection_config=..., kubeconfigs=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hybridConnectionConfig")
    def hybrid_connection_config(self) -> outputs.HybridConnectionConfigResponse: ...
    @_builtins.property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence[outputs.CredentialResultResponse]: ...

class AwaitableListConnectedClusterUserCredentialResult(
    ListConnectedClusterUserCredentialResult
):
    def __await__(self): ...

def list_connected_cluster_user_credential(
    authentication_method: Optional[Union[_builtins.str, AuthenticationMethod]] = ...,
    client_proxy: Optional[_builtins.bool] = ...,
    cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListConnectedClusterUserCredentialResult: ...
def list_connected_cluster_user_credential_output(
    authentication_method: Optional[
        pulumi.Input[Union[_builtins.str, AuthenticationMethod]]
    ] = ...,
    client_proxy: Optional[pulumi.Input[_builtins.bool]] = ...,
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListConnectedClusterUserCredentialResult]: ...
