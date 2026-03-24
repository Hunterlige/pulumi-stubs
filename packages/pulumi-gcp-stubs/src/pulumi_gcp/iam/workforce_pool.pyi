import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkforcePoolArgs", "WorkforcePool"]

@pulumi.input_type
class WorkforcePoolArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        workforce_pool_id: pulumi.Input[_builtins.str],
        access_restrictions: Optional[
            pulumi.Input[WorkforcePoolAccessRestrictionsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        session_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessRestrictions")
    def access_restrictions(
        self,
    ) -> Optional[pulumi.Input[WorkforcePoolAccessRestrictionsArgs]]: ...
    @access_restrictions.setter
    def access_restrictions(
        self, value: Optional[pulumi.Input[WorkforcePoolAccessRestrictionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_duration.setter
    def session_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _WorkforcePoolState:
    def __init__(
        __self__,
        *,
        access_restrictions: Optional[
            pulumi.Input[WorkforcePoolAccessRestrictionsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        session_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessRestrictions")
    def access_restrictions(
        self,
    ) -> Optional[pulumi.Input[WorkforcePoolAccessRestrictionsArgs]]: ...
    @access_restrictions.setter
    def access_restrictions(
        self, value: Optional[pulumi.Input[WorkforcePoolAccessRestrictionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_duration.setter
    def session_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workforce_pool_id.setter
    def workforce_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:iam/workforcePool:WorkforcePool")
class WorkforcePool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_restrictions: Optional[
            pulumi.Input[
                Union[
                    WorkforcePoolAccessRestrictionsArgs,
                    WorkforcePoolAccessRestrictionsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        session_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkforcePoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_restrictions: Optional[
            pulumi.Input[
                Union[
                    WorkforcePoolAccessRestrictionsArgs,
                    WorkforcePoolAccessRestrictionsArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        session_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WorkforcePool: ...
    @_builtins.property
    @pulumi.getter(name="accessRestrictions")
    def access_restrictions(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkforcePoolAccessRestrictions]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolId")
    def workforce_pool_id(self) -> pulumi.Output[_builtins.str]: ...
