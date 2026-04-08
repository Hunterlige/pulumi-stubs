import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatabaseAdvisorArgs", "DatabaseAdvisor"]

@pulumi.input_type
class DatabaseAdvisorArgs:
    def __init__(
        __self__,
        *,
        auto_execute_status: pulumi.Input[AutoExecuteStatus],
        database_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        server_name: pulumi.Input[_builtins.str],
        advisor_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoExecuteStatus")
    def auto_execute_status(self) -> pulumi.Input[AutoExecuteStatus]: ...
    @auto_execute_status.setter
    def auto_execute_status(self, value: pulumi.Input[AutoExecuteStatus]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="advisorName")
    def advisor_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @advisor_name.setter
    def advisor_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:sql:DatabaseAdvisor")
class DatabaseAdvisor(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advisor_name: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_execute_status: Optional[pulumi.Input[AutoExecuteStatus]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatabaseAdvisorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DatabaseAdvisor: ...
    @_builtins.property
    @pulumi.getter(name="advisorStatus")
    def advisor_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoExecuteStatus")
    def auto_execute_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoExecuteStatusInheritedFrom")
    def auto_execute_status_inherited_from(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recommendationsStatus")
    def recommendations_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recommendedActions")
    def recommended_actions(
        self,
    ) -> pulumi.Output[Sequence[outputs.RecommendedActionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
