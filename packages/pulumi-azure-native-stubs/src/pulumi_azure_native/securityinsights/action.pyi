import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ActionArgs", "Action"]

@pulumi.input_type
class ActionArgs:
    def __init__(
        __self__,
        *,
        logic_app_resource_id: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        rule_id: pulumi.Input[_builtins.str],
        trigger_uri: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        action_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @logic_app_resource_id.setter
    def logic_app_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[_builtins.str]: ...
    @rule_id.setter
    def rule_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="triggerUri")
    def trigger_uri(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_uri.setter
    def trigger_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_id.setter
    def action_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:securityinsights:Action")
class Action(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action_id: Optional[pulumi.Input[_builtins.str]] = ...,
        logic_app_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ActionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Action: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
