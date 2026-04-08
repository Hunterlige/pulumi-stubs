import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterInstanceHybridIdentityMetadatumArgs",
    "ClusterInstanceHybridIdentityMetadatum",
]

@pulumi.input_type
class ClusterInstanceHybridIdentityMetadatumArgs:
    def __init__(
        __self__,
        *,
        connected_cluster_resource_uri: pulumi.Input[_builtins.str],
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectedClusterResourceUri")
    def connected_cluster_resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @connected_cluster_resource_uri.setter
    def connected_cluster_resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_uid.setter
    def resource_uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ClusterInstanceHybridIdentityMetadatum(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        connected_cluster_resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ClusterInstanceHybridIdentityMetadatumArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ClusterInstanceHybridIdentityMetadatum: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
