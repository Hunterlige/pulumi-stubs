import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterInstanceHybridIdentityMetadatumResult",
    ...,
    "get_cluster_instance_hybrid_identity_metadatum",
    ...,
]

@pulumi.output_type
class GetClusterInstanceHybridIdentityMetadatumResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        provisioning_state=...,
        public_key=...,
        resource_uid=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetClusterInstanceHybridIdentityMetadatumResult(
    GetClusterInstanceHybridIdentityMetadatumResult
):
    def __await__(self): ...

def get_cluster_instance_hybrid_identity_metadatum(
    connected_cluster_resource_uri: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterInstanceHybridIdentityMetadatumResult: ...
def get_cluster_instance_hybrid_identity_metadatum_output(
    connected_cluster_resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterInstanceHybridIdentityMetadatumResult]: ...
