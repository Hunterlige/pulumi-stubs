import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetShareResult", "AwaitableGetShareResult", "get_share", "get_share_output"]

@pulumi.output_type
class GetShareResult:
    def __init__(
        __self__,
        access_protocol=...,
        azure_api_version=...,
        azure_container_info=...,
        client_access_rights=...,
        data_policy=...,
        description=...,
        id=...,
        monitoring_status=...,
        name=...,
        refresh_details=...,
        share_mappings=...,
        share_status=...,
        system_data=...,
        type=...,
        user_access_rights=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessProtocol")
    def access_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureContainerInfo")
    def azure_container_info(self) -> Optional[outputs.AzureContainerInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="clientAccessRights")
    def client_access_rights(
        self,
    ) -> Optional[Sequence[outputs.ClientAccessRightResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshDetails")
    def refresh_details(self) -> Optional[outputs.RefreshDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shareMappings")
    def share_mappings(self) -> Sequence[outputs.MountPointMapResponse]: ...
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAccessRights")
    def user_access_rights(
        self,
    ) -> Optional[Sequence[outputs.UserAccessRightResponse]]: ...

class AwaitableGetShareResult(GetShareResult):
    def __await__(self): ...

def get_share(
    device_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetShareResult: ...
def get_share_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetShareResult]: ...
