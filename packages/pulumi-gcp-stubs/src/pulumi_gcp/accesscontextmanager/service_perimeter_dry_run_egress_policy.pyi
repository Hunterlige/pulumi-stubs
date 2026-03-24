import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ServicePerimeterDryRunEgressPolicyArgs",
    "ServicePerimeterDryRunEgressPolicy",
]

@pulumi.input_type
class ServicePerimeterDryRunEgressPolicyArgs:
    def __init__(
        __self__,
        *,
        perimeter: pulumi.Input[_builtins.str],
        egress_from: Optional[
            pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromArgs]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressToArgs]
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
    ) -> Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromArgs]]: ...
    @egress_from.setter
    def egress_from(
        self,
        value: Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressToArgs]]: ...
    @egress_to.setter
    def egress_to(
        self,
        value: Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressToArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ServicePerimeterDryRunEgressPolicyState:
    def __init__(
        __self__,
        *,
        access_policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        egress_from: Optional[
            pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromArgs]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressToArgs]
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
    ) -> Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromArgs]]: ...
    @egress_from.setter
    def egress_from(
        self,
        value: Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressFromArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressToArgs]]: ...
    @egress_to.setter
    def egress_to(
        self,
        value: Optional[pulumi.Input[ServicePerimeterDryRunEgressPolicyEgressToArgs]],
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
class ServicePerimeterDryRunEgressPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        egress_from: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterDryRunEgressPolicyEgressFromArgs,
                    ServicePerimeterDryRunEgressPolicyEgressFromArgsDict,
                ]
            ]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterDryRunEgressPolicyEgressToArgs,
                    ServicePerimeterDryRunEgressPolicyEgressToArgsDict,
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
        args: ServicePerimeterDryRunEgressPolicyArgs,
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
                    ServicePerimeterDryRunEgressPolicyEgressFromArgs,
                    ServicePerimeterDryRunEgressPolicyEgressFromArgsDict,
                ]
            ]
        ] = ...,
        egress_to: Optional[
            pulumi.Input[
                Union[
                    ServicePerimeterDryRunEgressPolicyEgressToArgs,
                    ServicePerimeterDryRunEgressPolicyEgressToArgsDict,
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        perimeter: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ServicePerimeterDryRunEgressPolicy: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="egressFrom")
    def egress_from(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ServicePerimeterDryRunEgressPolicyEgressFrom]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="egressTo")
    def egress_to(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ServicePerimeterDryRunEgressPolicyEgressTo]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def perimeter(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]: ...
