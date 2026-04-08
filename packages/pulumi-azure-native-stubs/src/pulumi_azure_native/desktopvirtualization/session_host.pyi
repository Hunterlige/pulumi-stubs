import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SessionHostArgs", "SessionHost"]

@pulumi.input_type
class SessionHostArgs:
    def __init__(
        __self__,
        *,
        host_pool_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        allow_new_session: Optional[pulumi.Input[_builtins.bool]] = ...,
        assigned_user: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        session_host_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostPoolName")
    def host_pool_name(self) -> pulumi.Input[_builtins.str]: ...
    @host_pool_name.setter
    def host_pool_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowNewSession")
    def allow_new_session(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_new_session.setter
    def allow_new_session(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="assignedUser")
    def assigned_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assigned_user.setter
    def assigned_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionHostName")
    def session_host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_host_name.setter
    def session_host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:desktopvirtualization:SessionHost")
class SessionHost(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_new_session: Optional[pulumi.Input[_builtins.bool]] = ...,
        assigned_user: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        session_host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SessionHostArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SessionHost: ...
    @_builtins.property
    @pulumi.getter(name="activeSessions")
    def active_sessions(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowNewSession")
    def allow_new_session(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="assignedUser")
    def assigned_user(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disconnectedSessions")
    def disconnected_sessions(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastHeartBeat")
    def last_heart_beat(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastSessionHostUpdateTime")
    def last_session_host_update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pendingSessions")
    def pending_sessions(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionHostConfiguration")
    def session_host_configuration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionHostHealthCheckResults")
    def session_host_health_check_results(
        self,
    ) -> pulumi.Output[Sequence[outputs.SessionHostHealthCheckReportResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sessions(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusTimestamp")
    def status_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sxSStackVersion")
    def sx_s_stack_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateErrorMessage")
    def update_error_message(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateState")
    def update_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> pulumi.Output[_builtins.str]: ...
