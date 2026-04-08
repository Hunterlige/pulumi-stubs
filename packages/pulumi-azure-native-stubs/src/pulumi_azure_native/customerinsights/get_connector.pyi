import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

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
        connector_id=...,
        connector_name=...,
        connector_properties=...,
        connector_type=...,
        created=...,
        description=...,
        display_name=...,
        id=...,
        is_internal=...,
        last_modified=...,
        name=...,
        state=...,
        tenant_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorProperties")
    def connector_properties(self) -> Mapping[str, Any]: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConnectorResult(GetConnectorResult):
    def __await__(self): ...

def get_connector(
    connector_name: Optional[_builtins.str] = ...,
    hub_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectorResult: ...
def get_connector_output(
    connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectorResult]: ...
