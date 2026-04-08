import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTableServicePropertiesResult",
    "AwaitableGetTableServicePropertiesResult",
    "get_table_service_properties",
    "get_table_service_properties_output",
]

@pulumi.output_type
class GetTableServicePropertiesResult:
    def __init__(
        __self__, azure_api_version=..., cors=..., id=..., name=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[outputs.CorsRulesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTableServicePropertiesResult(GetTableServicePropertiesResult):
    def __await__(self): ...

def get_table_service_properties(
    account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    table_service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTableServicePropertiesResult: ...
def get_table_service_properties_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    table_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTableServicePropertiesResult]: ...
