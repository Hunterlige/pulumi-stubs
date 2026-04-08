import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCIAMTenantResult",
    "AwaitableGetCIAMTenantResult",
    "get_ciam_tenant",
    "get_ciam_tenant_output",
]

@pulumi.output_type
class GetCIAMTenantResult:
    def __init__(
        __self__,
        azure_api_version=...,
        billing_type=...,
        create_tenant_properties=...,
        domain_name=...,
        effective_start_date_utc=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        sku=...,
        system_data=...,
        tags=...,
        tenant_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTenantProperties")
    def create_tenant_properties(
        self,
    ) -> outputs.CreateCIAMTenantPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveStartDateUtc")
    def effective_start_date_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
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
    @pulumi.getter
    def sku(self) -> outputs.CIAMResourceSKUResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCIAMTenantResult(GetCIAMTenantResult):
    def __await__(self): ...

def get_ciam_tenant(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCIAMTenantResult: ...
def get_ciam_tenant_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCIAMTenantResult]: ...
