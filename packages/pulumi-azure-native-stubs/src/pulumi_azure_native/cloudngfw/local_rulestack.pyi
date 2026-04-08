import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LocalRulestackArgs", "LocalRulestack"]

@pulumi.input_type
class LocalRulestackArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        associated_subscriptions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_mode: Optional[pulumi.Input[Union[_builtins.str, DefaultMode]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[AzureResourceManagerManagedIdentityPropertiesArgs]
        ] = ...,
        local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        min_app_id_version: Optional[pulumi.Input[_builtins.str]] = ...,
        pan_etag: Optional[pulumi.Input[_builtins.str]] = ...,
        pan_location: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]] = ...,
        security_services: Optional[pulumi.Input[SecurityServicesArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @associated_subscriptions.setter
    def associated_subscriptions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DefaultMode]]]: ...
    @default_mode.setter
    def default_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DefaultMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[pulumi.Input[AzureResourceManagerManagedIdentityPropertiesArgs]]: ...
    @identity.setter
    def identity(
        self,
        value: Optional[
            pulumi.Input[AzureResourceManagerManagedIdentityPropertiesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localRulestackName")
    def local_rulestack_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_rulestack_name.setter
    def local_rulestack_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_app_id_version.setter
    def min_app_id_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pan_etag.setter
    def pan_etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pan_location.setter
    def pan_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[Union[_builtins.str, ScopeType]]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]]): ...
    @_builtins.property
    @pulumi.getter(name="securityServices")
    def security_services(self) -> Optional[pulumi.Input[SecurityServicesArgs]]: ...
    @security_services.setter
    def security_services(
        self, value: Optional[pulumi.Input[SecurityServicesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:cloudngfw:LocalRulestack")
class LocalRulestack(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        associated_subscriptions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_mode: Optional[pulumi.Input[Union[_builtins.str, DefaultMode]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    AzureResourceManagerManagedIdentityPropertiesArgs,
                    AzureResourceManagerManagedIdentityPropertiesArgsDict,
                ]
            ]
        ] = ...,
        local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        min_app_id_version: Optional[pulumi.Input[_builtins.str]] = ...,
        pan_etag: Optional[pulumi.Input[_builtins.str]] = ...,
        pan_location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[Union[_builtins.str, ScopeType]]] = ...,
        security_services: Optional[
            pulumi.Input[Union[SecurityServicesArgs, SecurityServicesArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LocalRulestackArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> LocalRulestack: ...
    @_builtins.property
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AzureResourceManagerManagedIdentityPropertiesResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityServices")
    def security_services(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityServicesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
