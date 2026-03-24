import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcEndpointConnectionAccepterArgs", "VpcEndpointConnectionAccepter"]

@pulumi.input_type
class VpcEndpointConnectionAccepterArgs:
    def __init__(
        __self__,
        *,
        vpc_endpoint_id: pulumi.Input[_builtins.str],
        vpc_endpoint_service_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VpcEndpointConnectionAccepterState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointState")
    def vpc_endpoint_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_state.setter
    def vpc_endpoint_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VpcEndpointConnectionAccepter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcEndpointConnectionAccepterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VpcEndpointConnectionAccepter: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointServiceId")
    def vpc_endpoint_service_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointState")
    def vpc_endpoint_state(self) -> pulumi.Output[_builtins.str]: ...
