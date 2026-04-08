import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceConfigurationArgs", "ServiceConfiguration"]

@pulumi.input_type
class ServiceConfigurationArgs:
    def __init__(
        __self__,
        *,
        endpoint_name: pulumi.Input[_builtins.str],
        resource_uri: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[Union[_builtins.str, ServiceName]],
        port: Optional[pulumi.Input[_builtins.float]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[Union[_builtins.str, ServiceName]]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[Union[_builtins.str, ServiceName]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceConfigurationName")
    def service_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_configuration_name.setter
    def service_configuration_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class ServiceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.float]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        service_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[Union[_builtins.str, ServiceName]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ServiceConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
