import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSapDiscoverySiteResult",
    "AwaitableGetSapDiscoverySiteResult",
    "get_sap_discovery_site",
    "get_sap_discovery_site_output",
]

@pulumi.output_type
class GetSapDiscoverySiteResult:
    def __init__(
        __self__,
        azure_api_version=...,
        errors=...,
        extended_location=...,
        id=...,
        location=...,
        master_site_id=...,
        migrate_project_id=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.SAPMigrateErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="masterSiteId")
    def master_site_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrateProjectId")
    def migrate_project_id(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSapDiscoverySiteResult(GetSapDiscoverySiteResult):
    def __await__(self): ...

def get_sap_discovery_site(
    resource_group_name: Optional[_builtins.str] = ...,
    sap_discovery_site_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSapDiscoverySiteResult: ...
def get_sap_discovery_site_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    sap_discovery_site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSapDiscoverySiteResult]: ...
