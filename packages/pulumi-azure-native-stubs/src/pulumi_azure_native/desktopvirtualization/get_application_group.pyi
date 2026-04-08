import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationGroupResult",
    "AwaitableGetApplicationGroupResult",
    "get_application_group",
    "get_application_group_output",
]

@pulumi.output_type
class GetApplicationGroupResult:
    def __init__(
        __self__,
        application_group_type=...,
        azure_api_version=...,
        cloud_pc_resource=...,
        description=...,
        etag=...,
        friendly_name=...,
        host_pool_arm_path=...,
        id=...,
        identity=...,
        kind=...,
        location=...,
        managed_by=...,
        name=...,
        object_id=...,
        plan=...,
        show_in_feed=...,
        sku=...,
        system_data=...,
        tags=...,
        type=...,
        workspace_arm_path=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGroupType")
    def application_group_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudPcResource")
    def cloud_pc_resource(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[outputs.ResourceModelWithAllowedPropertySetResponseIdentity]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def plan(
        self,
    ) -> Optional[outputs.ResourceModelWithAllowedPropertySetResponsePlan]: ...
    @_builtins.property
    @pulumi.getter(name="showInFeed")
    def show_in_feed(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def sku(
        self,
    ) -> Optional[outputs.ResourceModelWithAllowedPropertySetResponseSku]: ...
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
    @pulumi.getter(name="workspaceArmPath")
    def workspace_arm_path(self) -> _builtins.str: ...

class AwaitableGetApplicationGroupResult(GetApplicationGroupResult):
    def __await__(self): ...

def get_application_group(
    application_group_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationGroupResult: ...
def get_application_group_output(
    application_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationGroupResult]: ...
