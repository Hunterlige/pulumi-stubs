import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRestApiPollerDataConnectorResult",
    "AwaitableGetRestApiPollerDataConnectorResult",
    "get_rest_api_poller_data_connector",
    "get_rest_api_poller_data_connector_output",
]

@pulumi.output_type
class GetRestApiPollerDataConnectorResult:
    def __init__(
        __self__,
        add_on_attributes=...,
        auth=...,
        azure_api_version=...,
        connector_definition_name=...,
        data_type=...,
        dcr_config=...,
        etag=...,
        id=...,
        is_active=...,
        kind=...,
        name=...,
        paging=...,
        request=...,
        response=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addOnAttributes")
    def add_on_attributes(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorDefinitionName")
    def connector_definition_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dcrConfig")
    def dcr_config(self) -> Optional[outputs.DCRConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def paging(self) -> Optional[outputs.RestApiPollerRequestPagingConfigResponse]: ...
    @_builtins.property
    @pulumi.getter
    def request(self) -> outputs.RestApiPollerRequestConfigResponse: ...
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.CcpResponseConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRestApiPollerDataConnectorResult(GetRestApiPollerDataConnectorResult):
    def __await__(self): ...

def get_rest_api_poller_data_connector(
    data_connector_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRestApiPollerDataConnectorResult: ...
def get_rest_api_poller_data_connector_output(
    data_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRestApiPollerDataConnectorResult]: ...
