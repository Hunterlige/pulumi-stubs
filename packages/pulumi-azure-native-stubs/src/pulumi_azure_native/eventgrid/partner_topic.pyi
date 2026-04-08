import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PartnerTopicArgs", "PartnerTopic"]

@pulumi.input_type
class PartnerTopicArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        activation_state: Optional[
            pulumi.Input[Union[_builtins.str, PartnerTopicActivationState]]
        ] = ...,
        event_type_info: Optional[pulumi.Input[EventTypeInfoArgs]] = ...,
        expiration_time_if_not_activated_utc: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        identity: Optional[pulumi.Input[IdentityInfoArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        message_for_activation: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_registration_immutable_id: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_topic_friendly_description: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="activationState")
    def activation_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PartnerTopicActivationState]]]: ...
    @activation_state.setter
    def activation_state(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PartnerTopicActivationState]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> Optional[pulumi.Input[EventTypeInfoArgs]]: ...
    @event_type_info.setter
    def event_type_info(self, value: Optional[pulumi.Input[EventTypeInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration_time_if_not_activated_utc.setter
    def expiration_time_if_not_activated_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityInfoArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_for_activation.setter
    def message_for_activation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_registration_immutable_id.setter
    def partner_registration_immutable_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerTopicFriendlyDescription")
    def partner_topic_friendly_description(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_topic_friendly_description.setter
    def partner_topic_friendly_description(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerTopicName")
    def partner_topic_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_topic_name.setter
    def partner_topic_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:eventgrid:PartnerTopic")
class PartnerTopic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        activation_state: Optional[
            pulumi.Input[Union[_builtins.str, PartnerTopicActivationState]]
        ] = ...,
        event_type_info: Optional[
            pulumi.Input[Union[EventTypeInfoArgs, EventTypeInfoArgsDict]]
        ] = ...,
        expiration_time_if_not_activated_utc: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        identity: Optional[
            pulumi.Input[Union[IdentityInfoArgs, IdentityInfoArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        message_for_activation: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_registration_immutable_id: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_topic_friendly_description: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_topic_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PartnerTopicArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PartnerTopic: ...
    @_builtins.property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(
        self,
    ) -> pulumi.Output[Optional[outputs.EventTypeInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="partnerTopicFriendlyDescription")
    def partner_topic_friendly_description(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
