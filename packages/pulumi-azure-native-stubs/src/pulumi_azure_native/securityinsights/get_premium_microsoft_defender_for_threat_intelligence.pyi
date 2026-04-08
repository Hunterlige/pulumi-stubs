import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class GetPremiumMicrosoftDefenderForThreatIntelligenceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_types=...,
        etag=...,
        id=...,
        kind=...,
        lookback_period=...,
        name=...,
        required_skus_present=...,
        system_data=...,
        tenant_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> outputs.PremiumMdtiDataConnectorDataTypesResponse: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lookbackPeriod")
    def lookback_period(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiredSKUsPresent")
    def required_skus_present(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPremiumMicrosoftDefenderForThreatIntelligenceResult(
    GetPremiumMicrosoftDefenderForThreatIntelligenceResult
):
    def __await__(self): ...

def get_premium_microsoft_defender_for_threat_intelligence(
    data_connector_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPremiumMicrosoftDefenderForThreatIntelligenceResult: ...
def get_premium_microsoft_defender_for_threat_intelligence_output(
    data_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPremiumMicrosoftDefenderForThreatIntelligenceResult]: ...
