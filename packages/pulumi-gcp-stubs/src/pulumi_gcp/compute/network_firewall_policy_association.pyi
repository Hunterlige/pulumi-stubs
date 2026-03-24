import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkFirewallPolicyAssociationArgs", "NetworkFirewallPolicyAssociation"]

@pulumi.input_type
class NetworkFirewallPolicyAssociationArgs:
    def __init__(
        __self__,
        *,
        attachment_target: pulumi.Input[_builtins.str],
        firewall_policy: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentTarget")
    def attachment_target(self) -> pulumi.Input[_builtins.str]: ...
    @attachment_target.setter
    def attachment_target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Input[_builtins.str]: ...
    @firewall_policy.setter
    def firewall_policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NetworkFirewallPolicyAssociationState:
    def __init__(
        __self__,
        *,
        attachment_target: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        short_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentTarget")
    def attachment_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attachment_target.setter
    def attachment_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @firewall_policy.setter
    def firewall_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @short_name.setter
    def short_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class NetworkFirewallPolicyAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        attachment_target: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkFirewallPolicyAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        attachment_target: Optional[pulumi.Input[_builtins.str]] = ...,
        firewall_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        short_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NetworkFirewallPolicyAssociation: ...
    @_builtins.property
    @pulumi.getter(name="attachmentTarget")
    def attachment_target(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> pulumi.Output[_builtins.str]: ...
