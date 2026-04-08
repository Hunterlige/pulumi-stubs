import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReachabilityAnalysisIntentArgs", "ReachabilityAnalysisIntent"]

@pulumi.input_type
class ReachabilityAnalysisIntentArgs:
    def __init__(
        __self__,
        *,
        network_manager_name: pulumi.Input[_builtins.str],
        properties: pulumi.Input[ReachabilityAnalysisIntentPropertiesArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        reachability_analysis_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[ReachabilityAnalysisIntentPropertiesArgs]: ...
    @properties.setter
    def properties(
        self, value: pulumi.Input[ReachabilityAnalysisIntentPropertiesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="reachabilityAnalysisIntentName")
    def reachability_analysis_intent_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reachability_analysis_intent_name.setter
    def reachability_analysis_intent_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:network:ReachabilityAnalysisIntent")
class ReachabilityAnalysisIntent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        network_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    ReachabilityAnalysisIntentPropertiesArgs,
                    ReachabilityAnalysisIntentPropertiesArgsDict,
                ]
            ]
        ] = ...,
        reachability_analysis_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReachabilityAnalysisIntentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ReachabilityAnalysisIntent: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.ReachabilityAnalysisIntentPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
