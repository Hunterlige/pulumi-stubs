import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServicePerimeterEgressPolicyArgs", "ServicePerimeterEgressPolicy"]

@pulumi.input_type
class ServicePerimeterEgressPolicyArgs:
    def __init__(
        __self__,
        *,
        perimeter: pulumi.Input[_builtins.str],
        egress_from: Optional[
            pulumi.Input[ServicePerimeterEgressPolicyEgressFromArgs]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[ServicePerimeterEgressPolicyEgressToArgs]
        ] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def perimeter(self) -> pulumi.Input[_builtins.str]: ...
    @perimeter.setter
    def perimeter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressFromArgs]]: ...
    @egress_from.setter
    def egress_from(
        self, value: Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressFromArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressToArgs]]: ...
    @egress_to.setter
    def egress_to(
        self, value: Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressToArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ServicePerimeterEgressPolicyState:
    def __init__(
        __self__,
        *,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_from: Optional[
            pulumi.Input[ServicePerimeterEgressPolicyEgressFromArgs]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[ServicePerimeterEgressPolicyEgressToArgs]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        perimeter: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_policy_id.setter
    def access_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressFromArgs]]: ...
    @egress_from.setter
    def egress_from(
        self, value: Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressFromArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressToArgs]]: ...
    @egress_to.setter
    def egress_to(
        self, value: Optional[pulumi.Input[ServicePerimeterEgressPolicyEgressToArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def perimeter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @perimeter.setter
    def perimeter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ServicePerimeterEgressPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        egress_from: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterEgressPolicyEgressFromArgs,
                    ServicePerimeterEgressPolicyEgressFromArgsDict,
                ]
            ]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterEgressPolicyEgressToArgs,
                    ServicePerimeterEgressPolicyEgressToArgsDict,
                ]
            ]
        ] = ...,
        perimeter: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServicePerimeterEgressPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_from: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterEgressPolicyEgressFromArgs,
                    ServicePerimeterEgressPolicyEgressFromArgsDict,
                ]
            ]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterEgressPolicyEgressToArgs,
                    ServicePerimeterEgressPolicyEgressToArgsDict,
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        perimeter: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ServicePerimeterEgressPolicy: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> pulumi.Output[Optional[outputs.ServicePerimeterEgressPolicyEgressFrom]]: ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> pulumi.Output[Optional[outputs.ServicePerimeterEgressPolicyEgressTo]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def perimeter(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]: ...
