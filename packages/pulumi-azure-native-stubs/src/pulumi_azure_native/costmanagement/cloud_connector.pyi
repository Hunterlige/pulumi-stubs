import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CloudConnectorArgs", "CloudConnector"]

@pulumi.input_type
class CloudConnectorArgs:
    def __init__(
        __self__,
        *,
        billing_model: Optional[
            pulumi.Input[Union[_builtins.str, ConnectorBillingModel]]
        ] = ...,
        connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials_key: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        default_management_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        report_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingModel")
    def billing_model(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectorBillingModel]]]: ...
    @billing_model.setter
    def billing_model(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectorBillingModel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsKey")
    def credentials_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credentials_key.setter
    def credentials_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialsSecret")
    def credentials_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credentials_secret.setter
    def credentials_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultManagementGroupId")
    def default_management_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_management_group_id.setter
    def default_management_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reportId")
    def report_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @report_id.setter
    def report_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:costmanagement:CloudConnector")
class CloudConnector(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_model: Optional[
            pulumi.Input[Union[_builtins.str, ConnectorBillingModel]]
        ] = ...,
        connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials_key: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        default_management_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        report_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[CloudConnectorArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CloudConnector: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="collectionInfo")
    def collection_info(
        self,
    ) -> pulumi.Output[outputs.ConnectorCollectionInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialsKey")
    def credentials_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="daysTrialRemaining")
    def days_trial_remaining(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="defaultManagementGroupId")
    def default_management_group_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="externalBillingAccountId")
    def external_billing_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerBillingAccountDisplayName")
    def provider_billing_account_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerBillingAccountId")
    def provider_billing_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reportId")
    def report_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
