import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectorResult",
    "AwaitableGetConnectorResult",
    "get_connector",
    "get_connector_output",
]

@pulumi.output_type
class GetConnectorResult:
    def __init__(
        __self__,
        azure_api_version=...,
        connector_basic_info=...,
        connector_service_type_info=...,
        id=...,
        name=...,
        partner_connector_info=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorBasicInfo")
    def connector_basic_info(self) -> Optional[outputs.ConnectorInfoBaseResponse]: ...
    @_builtins.property
    @pulumi.getter(name="connectorServiceTypeInfo")
    def connector_service_type_info(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerConnectorInfo")
    def partner_connector_info(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConnectorResult(GetConnectorResult):
    def __await__(self): ...

def get_connector(
    cluster_id: Optional[_builtins.str] = ...,
    connector_name: Optional[_builtins.str] = ...,
    environment_id: Optional[_builtins.str] = ...,
    organization_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectorResult: ...
def get_connector_output(
    cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    organization_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectorResult]: ...
