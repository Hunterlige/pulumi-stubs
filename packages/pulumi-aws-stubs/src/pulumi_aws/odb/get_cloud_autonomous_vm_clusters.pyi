import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCloudAutonomousVmClustersResult",
    "AwaitableGetCloudAutonomousVmClustersResult",
    "get_cloud_autonomous_vm_clusters",
    "get_cloud_autonomous_vm_clusters_output",
]

@pulumi.output_type
class GetCloudAutonomousVmClustersResult:
    def __init__(
        __self__, cloud_autonomous_vm_clusters=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudAutonomousVmClusters")
    def cloud_autonomous_vm_clusters(
        self,
    ) -> Sequence[
        outputs.GetCloudAutonomousVmClustersCloudAutonomousVmClusterResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetCloudAutonomousVmClustersResult(GetCloudAutonomousVmClustersResult):
    def __await__(self): ...

def get_cloud_autonomous_vm_clusters(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetCloudAutonomousVmClustersResult: ...
def get_cloud_autonomous_vm_clusters_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCloudAutonomousVmClustersResult]: ...
