import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSapInstanceResult",
    "AwaitableGetSapInstanceResult",
    "get_sap_instance",
    "get_sap_instance_output",
]

@pulumi.output_type
class GetSapInstanceResult:
    def __init__(
        __self__,
        application=...,
        azure_api_version=...,
        environment=...,
        errors=...,
        id=...,
        landscape_sid=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        system_sid=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.SAPMigrateErrorResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="landscapeSid")
    def landscape_sid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
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
    @pulumi.getter(name="systemSid")
    def system_sid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSapInstanceResult(GetSapInstanceResult):
    def __await__(self): ...

def get_sap_instance(
    resource_group_name: Optional[_builtins.str] = ...,
    sap_discovery_site_name: Optional[_builtins.str] = ...,
    sap_instance_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSapInstanceResult: ...
def get_sap_instance_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sap_discovery_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sap_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSapInstanceResult]: ...
