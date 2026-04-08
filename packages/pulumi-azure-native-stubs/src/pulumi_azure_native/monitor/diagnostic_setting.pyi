import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DiagnosticSettingArgs", "DiagnosticSetting"]

@pulumi.input_type
class DiagnosticSettingArgs:
    def __init__(
        __self__,
        *,
        resource_uri: pulumi.Input[_builtins.str],
        event_hub_authorization_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        event_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        log_analytics_destination_type: Optional[pulumi.Input[_builtins.str]] = ...,
        logs: Optional[pulumi.Input[Sequence[pulumi.Input[LogSettingsArgs]]]] = ...,
        marketplace_partner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricSettingsArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_bus_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_hub_authorization_rule_id.setter
    def event_hub_authorization_rule_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_hub_name.setter
    def event_hub_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsDestinationType")
    def log_analytics_destination_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_analytics_destination_type.setter
    def log_analytics_destination_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def logs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LogSettingsArgs]]]]: ...
    @logs.setter
    def logs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LogSettingsArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="marketplacePartnerId")
    def marketplace_partner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @marketplace_partner_id.setter
    def marketplace_partner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricSettingsArgs]]]]: ...
    @metrics.setter
    def metrics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricSettingsArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_bus_rule_id.setter
    def service_bus_rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:monitor:DiagnosticSetting")
class DiagnosticSetting(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        event_hub_authorization_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        event_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        log_analytics_destination_type: Optional[pulumi.Input[_builtins.str]] = ...,
        logs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[LogSettingsArgs, LogSettingsArgsDict]]]
            ]
        ] = ...,
        marketplace_partner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[MetricSettingsArgs, MetricSettingsArgsDict]]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        service_bus_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DiagnosticSettingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DiagnosticSetting: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsDestinationType")
    def log_analytics_destination_type(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def logs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.LogSettingsResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="marketplacePartnerId")
    def marketplace_partner_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MetricSettingsResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
