import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentArgs", "Agent"]

@pulumi.input_type
class AgentArgs:
    def __init__(
        __self__,
        *,
        arc_resource_id: pulumi.Input[_builtins.str],
        arc_vm_uuid: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        storage_mover_name: pulumi.Input[_builtins.str],
        agent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        upload_limit_schedule: Optional[pulumi.Input[UploadLimitScheduleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="arcResourceId")
    def arc_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @arc_resource_id.setter
    def arc_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="arcVmUuid")
    def arc_vm_uuid(self) -> pulumi.Input[_builtins.str]: ...
    @arc_vm_uuid.setter
    def arc_vm_uuid(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageMoverName")
    def storage_mover_name(self) -> pulumi.Input[_builtins.str]: ...
    @storage_mover_name.setter
    def storage_mover_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_name.setter
    def agent_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uploadLimitSchedule")
    def upload_limit_schedule(
        self,
    ) -> Optional[pulumi.Input[UploadLimitScheduleArgs]]: ...
    @upload_limit_schedule.setter
    def upload_limit_schedule(
        self, value: Optional[pulumi.Input[UploadLimitScheduleArgs]]
    ): ...

@pulumi.type_token("azure-native:storagemover:Agent")
class Agent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        arc_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arc_vm_uuid: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_mover_name: Optional[pulumi.Input[_builtins.str]] = ...,
        upload_limit_schedule: Optional[
            pulumi.Input[Union[UploadLimitScheduleArgs, UploadLimitScheduleArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AgentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Agent: ...
    @_builtins.property
    @pulumi.getter(name="agentStatus")
    def agent_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="arcResourceId")
    def arc_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="arcVmUuid")
    def arc_vm_uuid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(
        self,
    ) -> pulumi.Output[outputs.AgentPropertiesErrorDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastStatusUpdate")
    def last_status_update(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localIPAddress")
    def local_ip_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryInMB")
    def memory_in_mb(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfCores")
    def number_of_cores(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uploadLimitSchedule")
    def upload_limit_schedule(
        self,
    ) -> pulumi.Output[Optional[outputs.UploadLimitScheduleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="uptimeInSeconds")
    def uptime_in_seconds(self) -> pulumi.Output[_builtins.float]: ...
