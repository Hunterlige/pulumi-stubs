import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHcxEnterpriseSiteResult",
    "AwaitableGetHcxEnterpriseSiteResult",
    "get_hcx_enterprise_site",
    "get_hcx_enterprise_site_output",
]

@pulumi.output_type
class GetHcxEnterpriseSiteResult:
    def __init__(
        __self__,
        activation_key=...,
        azure_api_version=...,
        id=...,
        name=...,
        provisioning_state=...,
        status=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
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
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetHcxEnterpriseSiteResult(GetHcxEnterpriseSiteResult):
    def __await__(self): ...

def get_hcx_enterprise_site(
    hcx_enterprise_site_name: Optional[_builtins.str] = ...,
    private_cloud_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetHcxEnterpriseSiteResult: ...
def get_hcx_enterprise_site_output(
    hcx_enterprise_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHcxEnterpriseSiteResult]: ...
