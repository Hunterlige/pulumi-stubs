import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RoutingRuleArgs", "RoutingRule"]

@pulumi.input_type
class RoutingRuleArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[RoutingRuleActionArgs]]],
        conditions: pulumi.Input[Sequence[pulumi.Input[RoutingRuleConditionArgs]]],
        domain_name: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[RoutingRuleActionArgs]]]: ...
    @actions.setter
    def actions(
        self, value: pulumi.Input[Sequence[pulumi.Input[RoutingRuleActionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[RoutingRuleConditionArgs]]]: ...
    @conditions.setter
    def conditions(
        self, value: pulumi.Input[Sequence[pulumi.Input[RoutingRuleConditionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _RoutingRuleState:
    def __init__(
        __self__,
        *,
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingRuleActionArgs]]]
        ] = ...,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingRuleConditionArgs]]]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoutingRuleActionArgs]]]]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RoutingRuleActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoutingRuleConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RoutingRuleConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingRuleArn")
    def routing_rule_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_rule_arn.setter
    def routing_rule_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingRuleId")
    def routing_rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_rule_id.setter
    def routing_rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:apigatewayv2/routingRule:RoutingRule")
class RoutingRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RoutingRuleActionArgs, RoutingRuleActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RoutingRuleConditionArgs, RoutingRuleConditionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RoutingRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RoutingRuleActionArgs, RoutingRuleActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RoutingRuleConditionArgs, RoutingRuleConditionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RoutingRule: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[outputs.RoutingRuleAction]]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.RoutingRuleCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingRuleArn")
    def routing_rule_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingRuleId")
    def routing_rule_id(self) -> pulumi.Output[_builtins.str]: ...
