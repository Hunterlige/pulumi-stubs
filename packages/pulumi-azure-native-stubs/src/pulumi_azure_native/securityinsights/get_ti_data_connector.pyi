import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTIDataConnectorResult",
    "AwaitableGetTIDataConnectorResult",
    "get_ti_data_connector",
    "get_ti_data_connector_output",
]

@pulumi.output_type
class GetTIDataConnectorResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_types=...,
        etag=...,
        id=...,
        kind=...,
        name=...,
        system_data=...,
        tenant_id=...,
        tip_lookback_period=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> outputs.TIDataConnectorDataTypesResponse: ...
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
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tipLookbackPeriod")
    def tip_lookback_period(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTIDataConnectorResult(GetTIDataConnectorResult):
    def __await__(self): ...

def get_ti_data_connector(
    data_connector_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTIDataConnectorResult: ...
def get_ti_data_connector_output(
    data_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTIDataConnectorResult]: ...
