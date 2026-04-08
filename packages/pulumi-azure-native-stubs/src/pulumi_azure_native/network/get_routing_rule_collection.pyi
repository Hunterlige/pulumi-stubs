import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRoutingRuleCollectionResult",
    "AwaitableGetRoutingRuleCollectionResult",
    "get_routing_rule_collection",
    "get_routing_rule_collection_output",
]

@pulumi.output_type
class GetRoutingRuleCollectionResult:
    def __init__(
        __self__,
        applies_to=...,
        azure_api_version=...,
        description=...,
        disable_bgp_route_propagation=...,
        etag=...,
        id=...,
        name=...,
        provisioning_state=...,
        resource_guid=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appliesTo")
    def applies_to(
        self,
    ) -> Sequence[outputs.NetworkManagerRoutingGroupItemResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableBgpRoutePropagation")
    def disable_bgp_route_propagation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
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
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRoutingRuleCollectionResult(GetRoutingRuleCollectionResult):
    def __await__(self): ...

def get_routing_rule_collection(
    configuration_name: Optional[_builtins.str] = ...,
    network_manager_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    rule_collection_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoutingRuleCollectionResult: ...
def get_routing_rule_collection_output(
    configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_collection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoutingRuleCollectionResult]: ...
