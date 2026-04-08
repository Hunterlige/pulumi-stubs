import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCloudConnectorResult",
    "AwaitableGetCloudConnectorResult",
    "get_cloud_connector",
    "get_cloud_connector_output",
]

@pulumi.output_type
class GetCloudConnectorResult:
    def __init__(
        __self__,
        azure_api_version=...,
        billing_model=...,
        collection_info=...,
        created_on=...,
        credentials_key=...,
        days_trial_remaining=...,
        default_management_group_id=...,
        display_name=...,
        external_billing_account_id=...,
        id=...,
        kind=...,
        modified_on=...,
        name=...,
        provider_billing_account_display_name=...,
        provider_billing_account_id=...,
        report_id=...,
        status=...,
        subscription_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collectionInfo")
    def collection_info(self) -> outputs.ConnectorCollectionInfoResponse: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialsKey")
    def credentials_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="daysTrialRemaining")
    def days_trial_remaining(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="defaultManagementGroupId")
    def default_management_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalBillingAccountId")
    def external_billing_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="providerBillingAccountDisplayName")
    def provider_billing_account_display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="providerBillingAccountId")
    def provider_billing_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reportId")
    def report_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCloudConnectorResult(GetCloudConnectorResult):
    def __await__(self): ...

def get_cloud_connector(
    connector_name: Optional[_builtins.str] = ...,
    expand: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCloudConnectorResult: ...
def get_cloud_connector_output(
    connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCloudConnectorResult]: ...
