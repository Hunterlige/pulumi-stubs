import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKustoPoolResult",
    "AwaitableGetKustoPoolResult",
    "get_kusto_pool",
    "get_kusto_pool_output",
]

@pulumi.output_type
class GetKustoPoolResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_ingestion_uri=...,
        enable_purge=...,
        enable_streaming_ingest=...,
        etag=...,
        id=...,
        language_extensions=...,
        location=...,
        name=...,
        optimized_autoscale=...,
        provisioning_state=...,
        sku=...,
        state=...,
        state_reason=...,
        system_data=...,
        tags=...,
        type=...,
        uri=...,
        workspace_uid=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataIngestionUri")
    def data_ingestion_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enablePurge")
    def enable_purge(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableStreamingIngest")
    def enable_streaming_ingest(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="languageExtensions")
    def language_extensions(self) -> outputs.LanguageExtensionsListResponse: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="optimizedAutoscale")
    def optimized_autoscale(self) -> Optional[outputs.OptimizedAutoscaleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.AzureSkuResponse: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceUID")
    def workspace_uid(self) -> Optional[_builtins.str]: ...

class AwaitableGetKustoPoolResult(GetKustoPoolResult):
    def __await__(self): ...

def get_kusto_pool(
    kusto_pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKustoPoolResult: ...
def get_kusto_pool_output(
    kusto_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKustoPoolResult]: ...
