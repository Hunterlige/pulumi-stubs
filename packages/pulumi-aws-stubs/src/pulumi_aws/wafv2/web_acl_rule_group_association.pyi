import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebAclRuleGroupAssociationArgs", "WebAclRuleGroupAssociation"]

@pulumi.input_type
class WebAclRuleGroupAssociationArgs:
    def __init__(
        __self__,
        *,
        priority: pulumi.Input[_builtins.int],
        rule_name: pulumi.Input[_builtins.str],
        web_acl_arn: pulumi.Input[_builtins.str],
        managed_rule_group: Optional[
            pulumi.Input[WebAclRuleGroupAssociationManagedRuleGroupArgs]
        ] = ...,
        override_action: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_group_reference: Optional[
            pulumi.Input[WebAclRuleGroupAssociationRuleGroupReferenceArgs]
        ] = ...,
        timeouts: Optional[pulumi.Input[WebAclRuleGroupAssociationTimeoutsArgs]] = ...,
        visibility_config: Optional[
            pulumi.Input[WebAclRuleGroupAssociationVisibilityConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]: ...
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webAclArn")
    def web_acl_arn(self) -> pulumi.Input[_builtins.str]: ...
    @web_acl_arn.setter
    def web_acl_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedRuleGroup")
    def managed_rule_group(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationManagedRuleGroupArgs]]: ...
    @managed_rule_group.setter
    def managed_rule_group(
        self,
        value: Optional[pulumi.Input[WebAclRuleGroupAssociationManagedRuleGroupArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="overrideAction")
    def override_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @override_action.setter
    def override_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupReference")
    def rule_group_reference(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationRuleGroupReferenceArgs]]: ...
    @rule_group_reference.setter
    def rule_group_reference(
        self,
        value: Optional[pulumi.Input[WebAclRuleGroupAssociationRuleGroupReferenceArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[WebAclRuleGroupAssociationTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationVisibilityConfigArgs]]: ...
    @visibility_config.setter
    def visibility_config(
        self,
        value: Optional[pulumi.Input[WebAclRuleGroupAssociationVisibilityConfigArgs]],
    ): ...

@pulumi.input_type
class _WebAclRuleGroupAssociationState:
    def __init__(
        __self__,
        *,
        managed_rule_group: Optional[
            pulumi.Input[WebAclRuleGroupAssociationManagedRuleGroupArgs]
        ] = ...,
        override_action: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_group_reference: Optional[
            pulumi.Input[WebAclRuleGroupAssociationRuleGroupReferenceArgs]
        ] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[WebAclRuleGroupAssociationTimeoutsArgs]] = ...,
        visibility_config: Optional[
            pulumi.Input[WebAclRuleGroupAssociationVisibilityConfigArgs]
        ] = ...,
        web_acl_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedRuleGroup")
    def managed_rule_group(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationManagedRuleGroupArgs]]: ...
    @managed_rule_group.setter
    def managed_rule_group(
        self,
        value: Optional[pulumi.Input[WebAclRuleGroupAssociationManagedRuleGroupArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="overrideAction")
    def override_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @override_action.setter
    def override_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="ruleGroupReference")
    def rule_group_reference(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationRuleGroupReferenceArgs]]: ...
    @rule_group_reference.setter
    def rule_group_reference(
        self,
        value: Optional[pulumi.Input[WebAclRuleGroupAssociationRuleGroupReferenceArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[WebAclRuleGroupAssociationTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(
        self,
    ) -> Optional[pulumi.Input[WebAclRuleGroupAssociationVisibilityConfigArgs]]: ...
    @visibility_config.setter
    def visibility_config(
        self,
        value: Optional[pulumi.Input[WebAclRuleGroupAssociationVisibilityConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webAclArn")
    def web_acl_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_acl_arn.setter
    def web_acl_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class WebAclRuleGroupAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        managed_rule_group: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationManagedRuleGroupArgs,
                    WebAclRuleGroupAssociationManagedRuleGroupArgsDict,
                ]
            ]
        ] = ...,
        override_action: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_group_reference: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationRuleGroupReferenceArgs,
                    WebAclRuleGroupAssociationRuleGroupReferenceArgsDict,
                ]
            ]
        ] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationTimeoutsArgs,
                    WebAclRuleGroupAssociationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        visibility_config: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationVisibilityConfigArgs,
                    WebAclRuleGroupAssociationVisibilityConfigArgsDict,
                ]
            ]
        ] = ...,
        web_acl_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAclRuleGroupAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        managed_rule_group: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationManagedRuleGroupArgs,
                    WebAclRuleGroupAssociationManagedRuleGroupArgsDict,
                ]
            ]
        ] = ...,
        override_action: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_group_reference: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationRuleGroupReferenceArgs,
                    WebAclRuleGroupAssociationRuleGroupReferenceArgsDict,
                ]
            ]
        ] = ...,
        rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationTimeoutsArgs,
                    WebAclRuleGroupAssociationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        visibility_config: Optional[
            pulumi.Input[
                Union[
                    WebAclRuleGroupAssociationVisibilityConfigArgs,
                    WebAclRuleGroupAssociationVisibilityConfigArgsDict,
                ]
            ]
        ] = ...,
        web_acl_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WebAclRuleGroupAssociation: ...
    @_builtins.property
    @pulumi.getter(name="managedRuleGroup")
    def managed_rule_group(
        self,
    ) -> pulumi.Output[
        Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroup]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="overrideAction")
    def override_action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupReference")
    def rule_group_reference(
        self,
    ) -> pulumi.Output[
        Optional[outputs.WebAclRuleGroupAssociationRuleGroupReference]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.WebAclRuleGroupAssociationTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.WebAclRuleGroupAssociationVisibilityConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="webAclArn")
    def web_acl_arn(self) -> pulumi.Output[_builtins.str]: ...
