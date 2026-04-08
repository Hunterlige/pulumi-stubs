import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKubernetesClusterFeatureResult",
    "AwaitableGetKubernetesClusterFeatureResult",
    "get_kubernetes_cluster_feature",
    "get_kubernetes_cluster_feature_output",
]

@pulumi.output_type
class GetKubernetesClusterFeatureResult:
    def __init__(
        __self__,
        availability_lifecycle=...,
        azure_api_version=...,
        detailed_status=...,
        detailed_status_message=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        options=...,
        provisioning_state=...,
        required=...,
        system_data=...,
        tags=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityLifecycle")
    def availability_lifecycle(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str: ...
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
    @pulumi.getter
    def options(self) -> Optional[Sequence[outputs.StringKeyValuePairResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.str: ...
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
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetKubernetesClusterFeatureResult(GetKubernetesClusterFeatureResult):
    def __await__(self): ...

def get_kubernetes_cluster_feature(
    feature_name: Optional[_builtins.str] = ...,
    kubernetes_cluster_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKubernetesClusterFeatureResult: ...
def get_kubernetes_cluster_feature_output(
    feature_name: Optional[pulumi.Input[_builtins.str]] = ...,
    kubernetes_cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKubernetesClusterFeatureResult]: ...
