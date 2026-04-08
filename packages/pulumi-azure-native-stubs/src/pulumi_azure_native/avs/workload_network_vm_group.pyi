import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkloadNetworkVMGroupArgs", "WorkloadNetworkVMGroup"]

@pulumi.input_type
class WorkloadNetworkVMGroupArgs:
    def __init__(
        __self__,
        *,
        private_cloud_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        revision: Optional[pulumi.Input[_builtins.float]] = ...,
        vm_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[_builtins.str]: ...
    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def members(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @members.setter
    def members(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="vmGroupId")
    def vm_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_group_id.setter
    def vm_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:avs:WorkloadNetworkVMGroup")
class WorkloadNetworkVMGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.float]] = ...,
        vm_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkloadNetworkVMGroupArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkloadNetworkVMGroup: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
