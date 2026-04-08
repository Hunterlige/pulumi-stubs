import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PimRoleEligibilityScheduleArgs", "PimRoleEligibilitySchedule"]

@pulumi.input_type
class PimRoleEligibilityScheduleArgs:
    def __init__(
        __self__,
        *,
        principal_id: pulumi.Input[_builtins.str],
        role_definition_id: pulumi.Input[_builtins.str],
        scope: pulumi.Input[_builtins.str],
        condition: Optional[pulumi.Input[_builtins.str]] = ...,
        condition_version: Optional[pulumi.Input[_builtins.str]] = ...,
        justification: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_info: Optional[
            pulumi.Input[RoleEligibilityScheduleRequestPropertiesScheduleInfoArgs]
        ] = ...,
        target_role_eligibility_schedule_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_role_eligibility_schedule_instance_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ticket_info: Optional[
            pulumi.Input[RoleEligibilityScheduleRequestPropertiesTicketInfoArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]: ...
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[_builtins.str]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="conditionVersion")
    def condition_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition_version.setter
    def condition_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @justification.setter
    def justification(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(
        self,
    ) -> Optional[
        pulumi.Input[RoleEligibilityScheduleRequestPropertiesScheduleInfoArgs]
    ]: ...
    @schedule_info.setter
    def schedule_info(
        self,
        value: Optional[
            pulumi.Input[RoleEligibilityScheduleRequestPropertiesScheduleInfoArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetRoleEligibilityScheduleId")
    def target_role_eligibility_schedule_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_role_eligibility_schedule_id.setter
    def target_role_eligibility_schedule_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetRoleEligibilityScheduleInstanceId")
    def target_role_eligibility_schedule_instance_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_role_eligibility_schedule_instance_id.setter
    def target_role_eligibility_schedule_instance_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ticketInfo")
    def ticket_info(
        self,
    ) -> Optional[
        pulumi.Input[RoleEligibilityScheduleRequestPropertiesTicketInfoArgs]
    ]: ...
    @ticket_info.setter
    def ticket_info(
        self,
        value: Optional[
            pulumi.Input[RoleEligibilityScheduleRequestPropertiesTicketInfoArgs]
        ],
    ): ...

@pulumi.type_token(...)
class PimRoleEligibilitySchedule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[pulumi.Input[_builtins.str]] = ...,
        condition_version: Optional[pulumi.Input[_builtins.str]] = ...,
        justification: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_info: Optional[
            pulumi.Input[
                Union[
                    RoleEligibilityScheduleRequestPropertiesScheduleInfoArgs,
                    RoleEligibilityScheduleRequestPropertiesScheduleInfoArgsDict,
                ]
            ]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        target_role_eligibility_schedule_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        target_role_eligibility_schedule_instance_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ticket_info: Optional[
            pulumi.Input[
                Union[
                    RoleEligibilityScheduleRequestPropertiesTicketInfoArgs,
                    RoleEligibilityScheduleRequestPropertiesTicketInfoArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PimRoleEligibilityScheduleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PimRoleEligibilitySchedule: ...
    @_builtins.property
    @pulumi.getter(name="approvalId")
    def approval_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="conditionVersion")
    def condition_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expandedProperties")
    def expanded_properties(
        self,
    ) -> pulumi.Output[outputs.ExpandedPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def justification(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestType")
    def request_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requestorId")
    def requestor_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RoleEligibilityScheduleRequestPropertiesResponseScheduleInfo]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetRoleEligibilityScheduleId")
    def target_role_eligibility_schedule_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetRoleEligibilityScheduleInstanceId")
    def target_role_eligibility_schedule_instance_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ticketInfo")
    def ticket_info(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RoleEligibilityScheduleRequestPropertiesResponseTicketInfo]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
