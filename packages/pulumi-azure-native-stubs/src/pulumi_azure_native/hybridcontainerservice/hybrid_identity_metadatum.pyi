import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["HybridIdentityMetadatumArgs", "HybridIdentityMetadatum"]

@pulumi.input_type
class HybridIdentityMetadatumArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        hybrid_identity_metadata_resource_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        identity: Optional[pulumi.Input[ProvisionedClusterIdentityArgs]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hybridIdentityMetadataResourceName")
    def hybrid_identity_metadata_resource_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hybrid_identity_metadata_resource_name.setter
    def hybrid_identity_metadata_resource_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ProvisionedClusterIdentityArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[ProvisionedClusterIdentityArgs]]
    ): ...
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
class HybridIdentityMetadatum(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        hybrid_identity_metadata_resource_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    ProvisionedClusterIdentityArgs, ProvisionedClusterIdentityArgsDict
                ]
            ]
        ] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: HybridIdentityMetadatumArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> HybridIdentityMetadatum: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ProvisionedClusterIdentityResponse]]: ...
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
