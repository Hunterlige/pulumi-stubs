import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OriginArgs", "Origin"]

@pulumi.input_type
class OriginArgs:
    def __init__(
        __self__,
        *,
        endpoint_name: pulumi.Input[_builtins.str],
        host_name: pulumi.Input[_builtins.str],
        profile_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        http_port: Optional[pulumi.Input[_builtins.int]] = ...,
        https_port: Optional[pulumi.Input[_builtins.int]] = ...,
        origin_host_header: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        private_link_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_approval_message: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]: ...
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @http_port.setter
    def http_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @https_port.setter
    def https_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_host_header.setter
    def origin_host_header(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originName")
    def origin_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_name.setter
    def origin_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_alias.setter
    def private_link_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_approval_message.setter
    def private_link_approval_message(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_location.setter
    def private_link_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_resource_id.setter
    def private_link_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("azure-native:cdn:Origin")
class Origin(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        http_port: Optional[pulumi.Input[_builtins.int]] = ...,
        https_port: Optional[pulumi.Input[_builtins.int]] = ...,
        origin_host_header: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        private_link_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_approval_message: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OriginArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Origin: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointStatus")
    def private_endpoint_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[_builtins.int]]: ...
