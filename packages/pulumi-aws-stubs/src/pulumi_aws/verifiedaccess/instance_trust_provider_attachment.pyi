import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceTrustProviderAttachmentArgs", "InstanceTrustProviderAttachment"]

@pulumi.input_type
class InstanceTrustProviderAttachmentArgs:
    def __init__(
        __self__,
        *,
        verifiedaccess_instance_id: pulumi.Input[_builtins.str],
        verifiedaccess_trust_provider_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @verifiedaccess_instance_id.setter
    def verifiedaccess_instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="verifiedaccessTrustProviderId")
    def verifiedaccess_trust_provider_id(self) -> pulumi.Input[_builtins.str]: ...
    @verifiedaccess_trust_provider_id.setter
    def verifiedaccess_trust_provider_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _InstanceTrustProviderAttachmentState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        verifiedaccess_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        verifiedaccess_trust_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verifiedaccess_instance_id.setter
    def verifiedaccess_instance_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="verifiedaccessTrustProviderId")
    def verifiedaccess_trust_provider_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verifiedaccess_trust_provider_id.setter
    def verifiedaccess_trust_provider_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class InstanceTrustProviderAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        verifiedaccess_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        verifiedaccess_trust_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceTrustProviderAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        verifiedaccess_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        verifiedaccess_trust_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> InstanceTrustProviderAttachment: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="verifiedaccessTrustProviderId")
    def verifiedaccess_trust_provider_id(self) -> pulumi.Output[_builtins.str]: ...
