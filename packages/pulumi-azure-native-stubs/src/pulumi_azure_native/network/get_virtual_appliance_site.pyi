import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualApplianceSiteResult",
    "AwaitableGetVirtualApplianceSiteResult",
    "get_virtual_appliance_site",
    "get_virtual_appliance_site_output",
]

@pulumi.output_type
class GetVirtualApplianceSiteResult:
    def __init__(
        __self__,
        address_prefix=...,
        azure_api_version=...,
        etag=...,
        id=...,
        name=...,
        o365_policy=...,
        provisioning_state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="o365Policy")
    def o365_policy(self) -> Optional[outputs.Office365PolicyPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVirtualApplianceSiteResult(GetVirtualApplianceSiteResult):
    def __await__(self): ...

def get_virtual_appliance_site(
    network_virtual_appliance_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    site_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualApplianceSiteResult: ...
def get_virtual_appliance_site_output(
    network_virtual_appliance_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualApplianceSiteResult]: ...
