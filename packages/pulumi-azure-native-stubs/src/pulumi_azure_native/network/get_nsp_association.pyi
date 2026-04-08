import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNspAssociationResult",
    "AwaitableGetNspAssociationResult",
    "get_nsp_association",
    "get_nsp_association_output",
]

@pulumi.output_type
class GetNspAssociationResult:
    def __init__(
        __self__,
        access_mode=...,
        azure_api_version=...,
        has_provisioning_issues=...,
        id=...,
        location=...,
        name=...,
        private_link_resource=...,
        profile=...,
        provisioning_state=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hasProvisioningIssues")
    def has_provisioning_issues(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResource")
    def private_link_resource(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetNspAssociationResult(GetNspAssociationResult):
    def __await__(self): ...

def get_nsp_association(
    association_name: Optional[_builtins.str] = ...,
    network_security_perimeter_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNspAssociationResult: ...
def get_nsp_association_output(
    association_name: Optional[pulumi.Input[_builtins.str]] = ...,
    network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNspAssociationResult]: ...
