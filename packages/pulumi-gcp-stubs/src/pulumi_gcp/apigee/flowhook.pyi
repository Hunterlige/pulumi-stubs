import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FlowhookArgs", "Flowhook"]

@pulumi.input_type
class FlowhookArgs:
    def __init__(
        __self__,
        *,
        environment: pulumi.Input[_builtins.str],
        flow_hook_point: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        sharedflow: pulumi.Input[_builtins.str],
        continue_on_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Input[_builtins.str]: ...
    @environment.setter
    def environment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="flowHookPoint")
    def flow_hook_point(self) -> pulumi.Input[_builtins.str]: ...
    @flow_hook_point.setter
    def flow_hook_point(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sharedflow(self) -> pulumi.Input[_builtins.str]: ...
    @sharedflow.setter
    def sharedflow(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="continueOnError")
    def continue_on_error(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_error.setter
    def continue_on_error(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FlowhookState:
    def __init__(
        __self__,
        *,
        continue_on_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        flow_hook_point: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sharedflow: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="continueOnError")
    def continue_on_error(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continue_on_error.setter
    def continue_on_error(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flowHookPoint")
    def flow_hook_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flow_hook_point.setter
    def flow_hook_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sharedflow(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sharedflow.setter
    def sharedflow(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:apigee/flowhook:Flowhook")
class Flowhook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        continue_on_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        flow_hook_point: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sharedflow: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FlowhookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        continue_on_error: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        flow_hook_point: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sharedflow: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Flowhook: ...
    @_builtins.property
    @pulumi.getter(name="continueOnError")
    def continue_on_error(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flowHookPoint")
    def flow_hook_point(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sharedflow(self) -> pulumi.Output[_builtins.str]: ...
