import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainArgs", "Domain"]

@pulumi.input_type
class DomainArgs:
    def __init__(
        __self__,
        *,
        domain_management: pulumi.Input[Union[_builtins.str, DomainManagement]],
        email_service_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_engagement_tracking: Optional[
            pulumi.Input[Union[_builtins.str, UserEngagementTracking]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainManagement")
    def domain_management(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DomainManagement]]: ...
    @domain_management.setter
    def domain_management(
        self, value: pulumi.Input[Union[_builtins.str, DomainManagement]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailServiceName")
    def email_service_name(self) -> pulumi.Input[_builtins.str]: ...
    @email_service_name.setter
    def email_service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userEngagementTracking")
    def user_engagement_tracking(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, UserEngagementTracking]]]: ...
    @user_engagement_tracking.setter
    def user_engagement_tracking(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, UserEngagementTracking]]],
    ): ...

@pulumi.type_token("azure-native:communication:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_management: Optional[
            pulumi.Input[Union[_builtins.str, DomainManagement]]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        email_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_engagement_tracking: Optional[
            pulumi.Input[Union[_builtins.str, UserEngagementTracking]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Domain: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainManagement")
    def domain_management(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fromSenderDomain")
    def from_sender_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mailFromSenderDomain")
    def mail_from_sender_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userEngagementTracking")
    def user_engagement_tracking(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="verificationRecords")
    def verification_records(
        self,
    ) -> pulumi.Output[outputs.DomainPropertiesResponseVerificationRecords]: ...
    @_builtins.property
    @pulumi.getter(name="verificationStates")
    def verification_states(
        self,
    ) -> pulumi.Output[outputs.DomainPropertiesResponseVerificationStates]: ...
