import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAzureTrafficCollectorResult",
    "AwaitableGetAzureTrafficCollectorResult",
    "get_azure_traffic_collector",
    "get_azure_traffic_collector_output",
]

@pulumi.output_type
class GetAzureTrafficCollectorResult:
    def __init__(
        __self__,
        azure_api_version=...,
        collector_policies=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        virtual_hub=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="collectorPolicies")
    def collector_policies(self) -> Sequence[outputs.ResourceReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[outputs.ResourceReferenceResponse]: ...

class AwaitableGetAzureTrafficCollectorResult(GetAzureTrafficCollectorResult):
    def __await__(self): ...

def get_azure_traffic_collector(
    azure_traffic_collector_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAzureTrafficCollectorResult: ...
def get_azure_traffic_collector_output(
    azure_traffic_collector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAzureTrafficCollectorResult]: ...
