import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RulesEngineArgs", "RulesEngine"]

@pulumi.input_type
class RulesEngineArgs:
    def __init__(
        __self__,
        *,
        front_door_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[RulesEngineRuleArgs]]]
        ] = ...,
        rules_engine_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frontDoorName")
    def front_door_name(self) -> pulumi.Input[_builtins.str]: ...
    @front_door_name.setter
    def front_door_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RulesEngineRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RulesEngineRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rulesEngineName")
    def rules_engine_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rules_engine_name.setter
    def rules_engine_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:frontdoor:RulesEngine")
class RulesEngine(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        front_door_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[RulesEngineRuleArgs, RulesEngineRuleArgsDict]]
                ]
            ]
        ] = ...,
        rules_engine_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RulesEngineArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RulesEngine: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RulesEngineRuleResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
