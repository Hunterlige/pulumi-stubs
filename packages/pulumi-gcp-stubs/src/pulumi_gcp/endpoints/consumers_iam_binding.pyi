import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConsumersIamBindingArgs", "ConsumersIamBinding"]

@pulumi.input_type
class ConsumersIamBindingArgs:
    def __init__(
        __self__,
        *,
        consumer_project: pulumi.Input[_builtins.str],
        members: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        role: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        condition: Optional[pulumi.Input[ConsumersIamBindingConditionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> pulumi.Input[_builtins.str]: ...
    @consumer_project.setter
    def consumer_project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[ConsumersIamBindingConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[ConsumersIamBindingConditionArgs]]
    ): ...

@pulumi.input_type
class _ConsumersIamBindingState:
    def __init__(
        __self__,
        *,
        condition: Optional[pulumi.Input[ConsumersIamBindingConditionArgs]] = ...,
        consumer_project: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[ConsumersIamBindingConditionArgs]]: ...
    @condition.setter
    def condition(
        self, value: Optional[pulumi.Input[ConsumersIamBindingConditionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_project.setter
    def consumer_project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @members.setter
    def members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ConsumersIamBinding(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    ConsumersIamBindingConditionArgs,
                    ConsumersIamBindingConditionArgsDict,
                ]
            ]
        ] = ...,
        consumer_project: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConsumersIamBindingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[
            pulumi.Input[
                Union[
                    ConsumersIamBindingConditionArgs,
                    ConsumersIamBindingConditionArgsDict,
                ]
            ]
        ] = ...,
        consumer_project: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ConsumersIamBinding: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> pulumi.Output[Optional[outputs.ConsumersIamBindingCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]: ...
