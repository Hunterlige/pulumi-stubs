import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetAddonResult", "AwaitableGetAddonResult", "get_addon", "get_addon_output"]

@pulumi.output_type
class GetAddonResult:
    def __init__(
        __self__,
        addon_name=...,
        addon_version=...,
        arn=...,
        cluster_name=...,
        configuration_values=...,
        created_at=...,
        id=...,
        modified_at=...,
        pod_identity_associations=...,
        region=...,
        service_account_role_arn=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configurationValues")
    def configuration_values(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="podIdentityAssociations")
    def pod_identity_associations(
        self,
    ) -> Sequence[outputs.GetAddonPodIdentityAssociationResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetAddonResult(GetAddonResult):
    def __await__(self): ...

def get_addon(
    addon_name: Optional[_builtins.str] = ...,
    cluster_name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAddonResult: ...
def get_addon_output(
    addon_name: Optional[pulumi.Input[_builtins.str]] = ...,
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAddonResult]: ...
