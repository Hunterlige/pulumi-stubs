import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EntitlementArgs", "Entitlement"]

@pulumi.input_type
class EntitlementArgs:
    def __init__(
        __self__,
        *,
        eligible_users: pulumi.Input[
            Sequence[pulumi.Input[EntitlementEligibleUserArgs]]
        ],
        entitlement_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        max_request_duration: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        privileged_access: pulumi.Input[EntitlementPrivilegedAccessArgs],
        requester_justification_config: pulumi.Input[
            EntitlementRequesterJustificationConfigArgs
        ],
        additional_notification_targets: Optional[
            pulumi.Input[EntitlementAdditionalNotificationTargetsArgs]
        ] = ...,
        approval_workflow: Optional[
            pulumi.Input[EntitlementApprovalWorkflowArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eligibleUsers")
    def eligible_users(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[EntitlementEligibleUserArgs]]]: ...
    @eligible_users.setter
    def eligible_users(
        self, value: pulumi.Input[Sequence[pulumi.Input[EntitlementEligibleUserArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="entitlementId")
    def entitlement_id(self) -> pulumi.Input[_builtins.str]: ...
    @entitlement_id.setter
    def entitlement_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxRequestDuration")
    def max_request_duration(self) -> pulumi.Input[_builtins.str]: ...
    @max_request_duration.setter
    def max_request_duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privilegedAccess")
    def privileged_access(self) -> pulumi.Input[EntitlementPrivilegedAccessArgs]: ...
    @privileged_access.setter
    def privileged_access(
        self, value: pulumi.Input[EntitlementPrivilegedAccessArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requesterJustificationConfig")
    def requester_justification_config(
        self,
    ) -> pulumi.Input[EntitlementRequesterJustificationConfigArgs]: ...
    @requester_justification_config.setter
    def requester_justification_config(
        self, value: pulumi.Input[EntitlementRequesterJustificationConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalNotificationTargets")
    def additional_notification_targets(
        self,
    ) -> Optional[pulumi.Input[EntitlementAdditionalNotificationTargetsArgs]]: ...
    @additional_notification_targets.setter
    def additional_notification_targets(
        self,
        value: Optional[pulumi.Input[EntitlementAdditionalNotificationTargetsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvalWorkflow")
    def approval_workflow(
        self,
    ) -> Optional[pulumi.Input[EntitlementApprovalWorkflowArgs]]: ...
    @approval_workflow.setter
    def approval_workflow(
        self, value: Optional[pulumi.Input[EntitlementApprovalWorkflowArgs]]
    ): ...

@pulumi.input_type
class _EntitlementState:
    def __init__(
        __self__,
        *,
        additional_notification_targets: Optional[
            pulumi.Input[EntitlementAdditionalNotificationTargetsArgs]
        ] = ...,
        approval_workflow: Optional[
            pulumi.Input[EntitlementApprovalWorkflowArgs]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        eligible_users: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntitlementEligibleUserArgs]]]
        ] = ...,
        entitlement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_request_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        privileged_access: Optional[
            pulumi.Input[EntitlementPrivilegedAccessArgs]
        ] = ...,
        requester_justification_config: Optional[
            pulumi.Input[EntitlementRequesterJustificationConfigArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalNotificationTargets")
    def additional_notification_targets(
        self,
    ) -> Optional[pulumi.Input[EntitlementAdditionalNotificationTargetsArgs]]: ...
    @additional_notification_targets.setter
    def additional_notification_targets(
        self,
        value: Optional[pulumi.Input[EntitlementAdditionalNotificationTargetsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvalWorkflow")
    def approval_workflow(
        self,
    ) -> Optional[pulumi.Input[EntitlementApprovalWorkflowArgs]]: ...
    @approval_workflow.setter
    def approval_workflow(
        self, value: Optional[pulumi.Input[EntitlementApprovalWorkflowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eligibleUsers")
    def eligible_users(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EntitlementEligibleUserArgs]]]
    ]: ...
    @eligible_users.setter
    def eligible_users(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntitlementEligibleUserArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="entitlementId")
    def entitlement_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entitlement_id.setter
    def entitlement_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRequestDuration")
    def max_request_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_request_duration.setter
    def max_request_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privilegedAccess")
    def privileged_access(
        self,
    ) -> Optional[pulumi.Input[EntitlementPrivilegedAccessArgs]]: ...
    @privileged_access.setter
    def privileged_access(
        self, value: Optional[pulumi.Input[EntitlementPrivilegedAccessArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requesterJustificationConfig")
    def requester_justification_config(
        self,
    ) -> Optional[pulumi.Input[EntitlementRequesterJustificationConfigArgs]]: ...
    @requester_justification_config.setter
    def requester_justification_config(
        self, value: Optional[pulumi.Input[EntitlementRequesterJustificationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class Entitlement(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_notification_targets: Optional[
            pulumi.Input[
                Union[
                    EntitlementAdditionalNotificationTargetsArgs,
                    EntitlementAdditionalNotificationTargetsArgsDict,
                ]
            ]
        ] = ...,
        approval_workflow: Optional[
            pulumi.Input[
                Union[
                    EntitlementApprovalWorkflowArgs, EntitlementApprovalWorkflowArgsDict
                ]
            ]
        ] = ...,
        eligible_users: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EntitlementEligibleUserArgs, EntitlementEligibleUserArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        entitlement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_request_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        privileged_access: Optional[
            pulumi.Input[
                Union[
                    EntitlementPrivilegedAccessArgs, EntitlementPrivilegedAccessArgsDict
                ]
            ]
        ] = ...,
        requester_justification_config: Optional[
            pulumi.Input[
                Union[
                    EntitlementRequesterJustificationConfigArgs,
                    EntitlementRequesterJustificationConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EntitlementArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_notification_targets: Optional[
            pulumi.Input[
                Union[
                    EntitlementAdditionalNotificationTargetsArgs,
                    EntitlementAdditionalNotificationTargetsArgsDict,
                ]
            ]
        ] = ...,
        approval_workflow: Optional[
            pulumi.Input[
                Union[
                    EntitlementApprovalWorkflowArgs, EntitlementApprovalWorkflowArgsDict
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        eligible_users: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            EntitlementEligibleUserArgs, EntitlementEligibleUserArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        entitlement_id: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_request_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        privileged_access: Optional[
            pulumi.Input[
                Union[
                    EntitlementPrivilegedAccessArgs, EntitlementPrivilegedAccessArgsDict
                ]
            ]
        ] = ...,
        requester_justification_config: Optional[
            pulumi.Input[
                Union[
                    EntitlementRequesterJustificationConfigArgs,
                    EntitlementRequesterJustificationConfigArgsDict,
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Entitlement: ...
    @_builtins.property
    @pulumi.getter(name="additionalNotificationTargets")
    def additional_notification_targets(
        self,
    ) -> pulumi.Output[Optional[outputs.EntitlementAdditionalNotificationTargets]]: ...
    @_builtins.property
    @pulumi.getter(name="approvalWorkflow")
    def approval_workflow(
        self,
    ) -> pulumi.Output[Optional[outputs.EntitlementApprovalWorkflow]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eligibleUsers")
    def eligible_users(
        self,
    ) -> pulumi.Output[Sequence[outputs.EntitlementEligibleUser]]: ...
    @_builtins.property
    @pulumi.getter(name="entitlementId")
    def entitlement_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRequestDuration")
    def max_request_duration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privilegedAccess")
    def privileged_access(
        self,
    ) -> pulumi.Output[outputs.EntitlementPrivilegedAccess]: ...
    @_builtins.property
    @pulumi.getter(name="requesterJustificationConfig")
    def requester_justification_config(
        self,
    ) -> pulumi.Output[outputs.EntitlementRequesterJustificationConfig]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
