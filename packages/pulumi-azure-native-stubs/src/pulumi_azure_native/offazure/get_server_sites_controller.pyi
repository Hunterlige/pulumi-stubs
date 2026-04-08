import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerSitesControllerResult",
    "AwaitableGetServerSitesControllerResult",
    "get_server_sites_controller",
    "get_server_sites_controller_output",
]

@pulumi.output_type
class GetServerSitesControllerResult:
    def __init__(
        __self__,
        agent_details=...,
        appliance_name=...,
        azure_api_version=...,
        discovery_solution_id=...,
        id=...,
        location=...,
        master_site_id=...,
        name=...,
        provisioning_state=...,
        service_endpoint=...,
        service_principal_identity_details=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Optional[outputs.SiteAgentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoverySolutionId")
    def discovery_solution_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="masterSiteId")
    def master_site_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalIdentityDetails")
    def service_principal_identity_details(
        self,
    ) -> Optional[outputs.SiteSpnPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerSitesControllerResult(GetServerSitesControllerResult):
    def __await__(self): ...

def get_server_sites_controller(
    resource_group_name: Optional[_builtins.str] = ...,
    site_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerSitesControllerResult: ...
def get_server_sites_controller_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    site_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerSitesControllerResult]: ...
