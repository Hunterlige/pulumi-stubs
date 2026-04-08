import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListManagedClusterAccessProfileResult",
    "AwaitableListManagedClusterAccessProfileResult",
    "list_managed_cluster_access_profile",
    "list_managed_cluster_access_profile_output",
]

@pulumi.output_type
class ListManagedClusterAccessProfileResult:
    def __init__(
        __self__, id=..., kube_config=..., location=..., name=..., tags=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubeConfig")
    def kube_config(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableListManagedClusterAccessProfileResult(
    ListManagedClusterAccessProfileResult
):
    def __await__(self): ...

def list_managed_cluster_access_profile(
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    role_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListManagedClusterAccessProfileResult: ...
def list_managed_cluster_access_profile_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    role_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListManagedClusterAccessProfileResult]: ...
