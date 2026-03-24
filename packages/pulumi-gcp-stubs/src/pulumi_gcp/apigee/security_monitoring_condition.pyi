import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityMonitoringConditionArgs", "SecurityMonitoringCondition"]

@pulumi.input_type
class SecurityMonitoringConditionArgs:
    def __init__(
        __self__,
        *,
        condition_id: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        profile: pulumi.Input[_builtins.str],
        scope: pulumi.Input[_builtins.str],
        include_all_resources: Optional[
            pulumi.Input[SecurityMonitoringConditionIncludeAllResourcesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionId")
    def condition_id(self) -> pulumi.Input[_builtins.str]: ...
    @condition_id.setter
    def condition_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> pulumi.Input[_builtins.str]: ...
    @profile.setter
    def profile(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includeAllResources")
    def include_all_resources(
        self,
    ) -> Optional[pulumi.Input[SecurityMonitoringConditionIncludeAllResourcesArgs]]: ...
    @include_all_resources.setter
    def include_all_resources(
        self,
        value: Optional[
            pulumi.Input[SecurityMonitoringConditionIncludeAllResourcesArgs]
        ],
    ): ...

@pulumi.input_type
class _SecurityMonitoringConditionState:
    def __init__(
        __self__,
        *,
        condition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        include_all_resources: Optional[
            pulumi.Input[SecurityMonitoringConditionIncludeAllResourcesArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        total_deployed_resources: Optional[pulumi.Input[_builtins.int]] = ...,
        total_monitored_resources: Optional[pulumi.Input[_builtins.int]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionId")
    def condition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition_id.setter
    def condition_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includeAllResources")
    def include_all_resources(
        self,
    ) -> Optional[pulumi.Input[SecurityMonitoringConditionIncludeAllResourcesArgs]]: ...
    @include_all_resources.setter
    def include_all_resources(
        self,
        value: Optional[
            pulumi.Input[SecurityMonitoringConditionIncludeAllResourcesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="totalDeployedResources")
    def total_deployed_resources(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_deployed_resources.setter
    def total_deployed_resources(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="totalMonitoredResources")
    def total_monitored_resources(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_monitored_resources.setter
    def total_monitored_resources(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class SecurityMonitoringCondition(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        include_all_resources: Optional[
            pulumi.Input[
                Union[
                    SecurityMonitoringConditionIncludeAllResourcesArgs,
                    SecurityMonitoringConditionIncludeAllResourcesArgsDict,
                ]
            ]
        ] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityMonitoringConditionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        include_all_resources: Optional[
            pulumi.Input[
                Union[
                    SecurityMonitoringConditionIncludeAllResourcesArgs,
                    SecurityMonitoringConditionIncludeAllResourcesArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        total_deployed_resources: Optional[pulumi.Input[_builtins.int]] = ...,
        total_monitored_resources: Optional[pulumi.Input[_builtins.int]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecurityMonitoringCondition: ...
    @_builtins.property
    @pulumi.getter(name="conditionId")
    def condition_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeAllResources")
    def include_all_resources(
        self,
    ) -> pulumi.Output[
        Optional[outputs.SecurityMonitoringConditionIncludeAllResources]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totalDeployedResources")
    def total_deployed_resources(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalMonitoredResources")
    def total_monitored_resources(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
