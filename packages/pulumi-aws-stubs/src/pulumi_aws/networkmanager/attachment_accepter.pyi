import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AttachmentAccepterArgs", "AttachmentAccepter"]

@pulumi.input_type
class AttachmentAccepterArgs:
    def __init__(
        __self__,
        *,
        attachment_id: pulumi.Input[_builtins.str],
        attachment_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Input[_builtins.str]: ...
    @attachment_id.setter
    def attachment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Input[_builtins.str]: ...
    @attachment_type.setter
    def attachment_type(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _AttachmentAccepterState:
    def __init__(
        __self__,
        *,
        attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        attachment_policy_rule_number: Optional[pulumi.Input[_builtins.int]] = ...,
        attachment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_location: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        segment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @attachment_policy_rule_number.setter
    def attachment_policy_rule_number(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attachment_type.setter
    def attachment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_arn.setter
    def core_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_network_id.setter
    def core_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_location.setter
    def edge_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @edge_locations.setter
    def edge_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @segment_name.setter
    def segment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class AttachmentAccepter(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        attachment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AttachmentAccepterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        attachment_policy_rule_number: Optional[pulumi.Input[_builtins.int]] = ...,
        attachment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        core_network_id: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_location: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        segment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AttachmentAccepter: ...
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="attachmentPolicyRuleNumber")
    def attachment_policy_rule_number(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="edgeLocations")
    def edge_locations(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="segmentName")
    def segment_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
