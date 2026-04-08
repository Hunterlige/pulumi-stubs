import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DevicePoolRuleArgs",
    "DevicePoolRuleArgsDict",
    "TestGridProjectVpcConfigArgs",
    "TestGridProjectVpcConfigArgsDict",
]

class DevicePoolRuleArgsDict(TypedDict):
    attribute: NotRequired[pulumi.Input[_builtins.str]]
    operator: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DevicePoolRuleArgs:
    def __init__(
        __self__,
        *,
        attribute: Optional[pulumi.Input[_builtins.str]] = ...,
        operator: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute.setter
    def attribute(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TestGridProjectVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class TestGridProjectVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
