import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OsPolicyAssignmentArgs", "OsPolicyAssignment"]

@pulumi.input_type
class OsPolicyAssignmentArgs:
    def __init__(
        __self__,
        *,
        instance_filter: pulumi.Input[OsPolicyAssignmentInstanceFilterArgs],
        location: pulumi.Input[_builtins.str],
        os_policies: pulumi.Input[
            Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyArgs]]
        ],
        rollout: pulumi.Input[OsPolicyAssignmentRolloutArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_await_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(self) -> pulumi.Input[OsPolicyAssignmentInstanceFilterArgs]: ...
    @instance_filter.setter
    def instance_filter(
        self, value: pulumi.Input[OsPolicyAssignmentInstanceFilterArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyArgs]]]: ...
    @os_policies.setter
    def os_policies(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rollout(self) -> pulumi.Input[OsPolicyAssignmentRolloutArgs]: ...
    @rollout.setter
    def rollout(self, value: pulumi.Input[OsPolicyAssignmentRolloutArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipAwaitRollout")
    def skip_await_rollout(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_await_rollout.setter
    def skip_await_rollout(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _OsPolicyAssignmentState:
    def __init__(
        __self__,
        *,
        baseline: Optional[pulumi.Input[_builtins.bool]] = ...,
        deleted: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_filter: Optional[
            pulumi.Input[OsPolicyAssignmentInstanceFilterArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyArgs]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision_create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout: Optional[pulumi.Input[OsPolicyAssignmentRolloutArgs]] = ...,
        rollout_state: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_await_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @baseline.setter
    def baseline(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deleted.setter
    def deleted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> Optional[pulumi.Input[OsPolicyAssignmentInstanceFilterArgs]]: ...
    @instance_filter.setter
    def instance_filter(
        self, value: Optional[pulumi.Input[OsPolicyAssignmentInstanceFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyArgs]]]
    ]: ...
    @os_policies.setter
    def os_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[OsPolicyAssignmentOsPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_create_time.setter
    def revision_create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_id.setter
    def revision_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rollout(self) -> Optional[pulumi.Input[OsPolicyAssignmentRolloutArgs]]: ...
    @rollout.setter
    def rollout(self, value: Optional[pulumi.Input[OsPolicyAssignmentRolloutArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rollout_state.setter
    def rollout_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipAwaitRollout")
    def skip_await_rollout(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_await_rollout.setter
    def skip_await_rollout(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:osconfig/osPolicyAssignment:OsPolicyAssignment")
class OsPolicyAssignment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_filter: Optional[
            pulumi.Input[
                Union[
                    OsPolicyAssignmentInstanceFilterArgs,
                    OsPolicyAssignmentInstanceFilterArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            OsPolicyAssignmentOsPolicyArgs,
                            OsPolicyAssignmentOsPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout: Optional[
            pulumi.Input[
                Union[OsPolicyAssignmentRolloutArgs, OsPolicyAssignmentRolloutArgsDict]
            ]
        ] = ...,
        skip_await_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OsPolicyAssignmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        baseline: Optional[pulumi.Input[_builtins.bool]] = ...,
        deleted: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_filter: Optional[
            pulumi.Input[
                Union[
                    OsPolicyAssignmentInstanceFilterArgs,
                    OsPolicyAssignmentInstanceFilterArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            OsPolicyAssignmentOsPolicyArgs,
                            OsPolicyAssignmentOsPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision_create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_id: Optional[pulumi.Input[_builtins.str]] = ...,
        rollout: Optional[
            pulumi.Input[
                Union[OsPolicyAssignmentRolloutArgs, OsPolicyAssignmentRolloutArgsDict]
            ]
        ] = ...,
        rollout_state: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_await_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> OsPolicyAssignment: ...
    @_builtins.property
    @pulumi.getter
    def baseline(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceFilter")
    def instance_filter(
        self,
    ) -> pulumi.Output[outputs.OsPolicyAssignmentInstanceFilter]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osPolicies")
    def os_policies(
        self,
    ) -> pulumi.Output[Sequence[outputs.OsPolicyAssignmentOsPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="revisionCreateTime")
    def revision_create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rollout(self) -> pulumi.Output[outputs.OsPolicyAssignmentRollout]: ...
    @_builtins.property
    @pulumi.getter(name="rolloutState")
    def rollout_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipAwaitRollout")
    def skip_await_rollout(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
