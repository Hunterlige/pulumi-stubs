import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTrafficControllerInterfaceResult",
    "AwaitableGetTrafficControllerInterfaceResult",
    "get_traffic_controller_interface",
    "get_traffic_controller_interface_output",
]

@pulumi.output_type
class GetTrafficControllerInterfaceResult:
    def __init__(
        __self__,
        associations=...,
        azure_api_version=...,
        configuration_endpoints=...,
        frontends=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        security_policies=...,
        security_policy_configurations=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def associations(self) -> Sequence[outputs.ResourceIdResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationEndpoints")
    def configuration_endpoints(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def frontends(self) -> Sequence[outputs.ResourceIdResponse]: ...
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
    @pulumi.getter(name="securityPolicies")
    def security_policies(self) -> Sequence[outputs.ResourceIdResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyConfigurations")
    def security_policy_configurations(
        self,
    ) -> Optional[outputs.SecurityPolicyConfigurationsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTrafficControllerInterfaceResult(GetTrafficControllerInterfaceResult):
    def __await__(self): ...

def get_traffic_controller_interface(
    resource_group_name: Optional[_builtins.str] = ...,
    traffic_controller_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTrafficControllerInterfaceResult: ...
def get_traffic_controller_interface_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    traffic_controller_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTrafficControllerInterfaceResult]: ...
