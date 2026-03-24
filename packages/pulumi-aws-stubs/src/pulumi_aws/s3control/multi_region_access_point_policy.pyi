import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MultiRegionAccessPointPolicyArgs", "MultiRegionAccessPointPolicy"]

@pulumi.input_type
class MultiRegionAccessPointPolicyArgs:
    def __init__(
        __self__,
        *,
        details: pulumi.Input[MultiRegionAccessPointPolicyDetailsArgs],
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> pulumi.Input[MultiRegionAccessPointPolicyDetailsArgs]: ...
    @details.setter
    def details(self, value: pulumi.Input[MultiRegionAccessPointPolicyDetailsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MultiRegionAccessPointPolicyState:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[pulumi.Input[MultiRegionAccessPointPolicyDetailsArgs]] = ...,
        established: Optional[pulumi.Input[_builtins.str]] = ...,
        proposed: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[pulumi.Input[MultiRegionAccessPointPolicyDetailsArgs]]: ...
    @details.setter
    def details(
        self, value: Optional[pulumi.Input[MultiRegionAccessPointPolicyDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def established(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @established.setter
    def established(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def proposed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proposed.setter
    def proposed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class MultiRegionAccessPointPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[
            pulumi.Input[
                Union[
                    MultiRegionAccessPointPolicyDetailsArgs,
                    MultiRegionAccessPointPolicyDetailsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MultiRegionAccessPointPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[
            pulumi.Input[
                Union[
                    MultiRegionAccessPointPolicyDetailsArgs,
                    MultiRegionAccessPointPolicyDetailsArgsDict,
                ]
            ]
        ] = ...,
        established: Optional[pulumi.Input[_builtins.str]] = ...,
        proposed: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MultiRegionAccessPointPolicy: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> pulumi.Output[outputs.MultiRegionAccessPointPolicyDetails]: ...
    @_builtins.property
    @pulumi.getter
    def established(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def proposed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
