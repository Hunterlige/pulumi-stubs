import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionNetworkEndpointGroupResult",
    "AwaitableGetRegionNetworkEndpointGroupResult",
    "get_region_network_endpoint_group",
    "get_region_network_endpoint_group_output",
]

@pulumi.output_type
class GetRegionNetworkEndpointGroupResult:
    def __init__(
        __self__,
        app_engines=...,
        cloud_functions=...,
        cloud_runs=...,
        description=...,
        id=...,
        name=...,
        network=...,
        network_endpoint_type=...,
        project=...,
        psc_datas=...,
        psc_target_service=...,
        region=...,
        self_link=...,
        serverless_deployments=...,
        subnetwork=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngines")
    def app_engines(
        self,
    ) -> Sequence[outputs.GetRegionNetworkEndpointGroupAppEngineResult]: ...
    @_builtins.property
    @pulumi.getter(name="cloudFunctions")
    def cloud_functions(
        self,
    ) -> Sequence[outputs.GetRegionNetworkEndpointGroupCloudFunctionResult]: ...
    @_builtins.property
    @pulumi.getter(name="cloudRuns")
    def cloud_runs(
        self,
    ) -> Sequence[outputs.GetRegionNetworkEndpointGroupCloudRunResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscDatas")
    def psc_datas(
        self,
    ) -> Sequence[outputs.GetRegionNetworkEndpointGroupPscDataResult]: ...
    @_builtins.property
    @pulumi.getter(name="pscTargetService")
    def psc_target_service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverlessDeployments")
    def serverless_deployments(
        self,
    ) -> Sequence[outputs.GetRegionNetworkEndpointGroupServerlessDeploymentResult]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...

class AwaitableGetRegionNetworkEndpointGroupResult(GetRegionNetworkEndpointGroupResult):
    def __await__(self): ...

def get_region_network_endpoint_group(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    self_link: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionNetworkEndpointGroupResult: ...
def get_region_network_endpoint_group_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionNetworkEndpointGroupResult]: ...
