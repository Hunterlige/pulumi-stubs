import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRoutePolicyResult",
    "AwaitableGetRoutePolicyResult",
    "get_route_policy",
    "get_route_policy_output",
]

@pulumi.output_type
class GetRoutePolicyResult:
    def __init__(
        __self__,
        address_family_type=...,
        administrative_state=...,
        annotation=...,
        azure_api_version=...,
        configuration_state=...,
        default_action=...,
        id=...,
        location=...,
        name=...,
        network_fabric_id=...,
        provisioning_state=...,
        statements=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressFamilyType")
    def address_family_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def statements(
        self,
    ) -> Sequence[outputs.RoutePolicyStatementPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRoutePolicyResult(GetRoutePolicyResult):
    def __await__(self): ...

def get_route_policy(
    resource_group_name: Optional[_builtins.str] = ...,
    route_policy_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoutePolicyResult: ...
def get_route_policy_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    route_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoutePolicyResult]: ...
