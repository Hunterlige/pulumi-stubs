import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CapabilityArgs", "Capability"]

@pulumi.input_type
class CapabilityArgs:
    def __init__(
        __self__,
        *,
        parent_provider_namespace: pulumi.Input[_builtins.str],
        parent_resource_name: pulumi.Input[_builtins.str],
        parent_resource_type: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        target_name: pulumi.Input[_builtins.str],
        capability_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parentProviderNamespace")
    def parent_provider_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @parent_provider_namespace.setter
    def parent_provider_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parentResourceName")
    def parent_resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @parent_resource_name.setter
    def parent_resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parentResourceType")
    def parent_resource_type(self) -> pulumi.Input[_builtins.str]: ...
    @parent_resource_type.setter
    def parent_resource_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_name.setter
    def target_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="capabilityName")
    def capability_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capability_name.setter
    def capability_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:chaos:Capability")
class Capability(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        capability_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CapabilityArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Capability: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.CapabilityPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
