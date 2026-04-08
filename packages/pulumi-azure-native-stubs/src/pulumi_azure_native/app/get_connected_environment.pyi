import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectedEnvironmentResult",
    "AwaitableGetConnectedEnvironmentResult",
    "get_connected_environment",
    "get_connected_environment_output",
]

@pulumi.output_type
class GetConnectedEnvironmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        custom_domain_configuration=...,
        dapr_ai_connection_string=...,
        default_domain=...,
        deployment_errors=...,
        extended_location=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        static_ip=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(
        self,
    ) -> Optional[outputs.CustomDomainConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> _builtins.str: ...
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
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConnectedEnvironmentResult(GetConnectedEnvironmentResult):
    def __await__(self): ...

def get_connected_environment(
    connected_environment_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectedEnvironmentResult: ...
def get_connected_environment_output(
    connected_environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectedEnvironmentResult]: ...
