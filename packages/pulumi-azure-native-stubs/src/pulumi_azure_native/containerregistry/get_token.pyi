import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetTokenResult", "AwaitableGetTokenResult", "get_token", "get_token_output"]

@pulumi.output_type
class GetTokenResult:
    def __init__(
        __self__,
        azure_api_version=...,
        creation_date=...,
        credentials=...,
        id=...,
        name=...,
        provisioning_state=...,
        scope_map_id=...,
        status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.TokenCredentialsPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scopeMapId")
    def scope_map_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTokenResult(GetTokenResult):
    def __await__(self): ...

def get_token(
    registry_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    token_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTokenResult: ...
def get_token_output(
    registry_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    token_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTokenResult]: ...
