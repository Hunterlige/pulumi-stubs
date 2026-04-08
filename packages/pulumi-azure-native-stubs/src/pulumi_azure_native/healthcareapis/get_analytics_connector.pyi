import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAnalyticsConnectorResult",
    "AwaitableGetAnalyticsConnectorResult",
    "get_analytics_connector",
    "get_analytics_connector_output",
]

@pulumi.output_type
class GetAnalyticsConnectorResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_destination_configuration=...,
        data_mapping_configuration=...,
        data_source_configuration=...,
        etag=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataDestinationConfiguration")
    def data_destination_configuration(
        self,
    ) -> outputs.AnalyticsConnectorDataLakeDataDestinationResponse: ...
    @_builtins.property
    @pulumi.getter(name="dataMappingConfiguration")
    def data_mapping_configuration(
        self,
    ) -> outputs.AnalyticsConnectorFhirToParquetMappingResponse: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(
        self,
    ) -> outputs.AnalyticsConnectorFhirServiceDataSourceResponse: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ServiceManagedIdentityResponseIdentity]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAnalyticsConnectorResult(GetAnalyticsConnectorResult):
    def __await__(self): ...

def get_analytics_connector(
    analytics_connector_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAnalyticsConnectorResult: ...
def get_analytics_connector_output(
    analytics_connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAnalyticsConnectorResult]: ...
