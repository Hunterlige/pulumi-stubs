import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EnvironmentApiRevisionDeploymentArgs", "EnvironmentApiRevisionDeployment"]

@pulumi.input_type
class EnvironmentApiRevisionDeploymentArgs:
    def __init__(
        __self__,
        *,
        api: pulumi.Input[_builtins.str],
        environment: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        revision: pulumi.Input[_builtins.int],
        override: Optional[pulumi.Input[_builtins.bool]] = ...,
        sequenced_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> pulumi.Input[_builtins.str]: ...
    @api.setter
    def api(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Input[_builtins.str]: ...
    @environment.setter
    def environment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Input[_builtins.int]: ...
    @revision.setter
    def revision(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override.setter
    def override(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sequencedRollout")
    def sequenced_rollout(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sequenced_rollout.setter
    def sequenced_rollout(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EnvironmentApiRevisionDeploymentState:
    def __init__(
        __self__,
        *,
        api: Optional[pulumi.Input[_builtins.str]] = ...,
        basepaths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        deploy_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        override: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
        sequenced_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api.setter
    def api(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def basepaths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @basepaths.setter
    def basepaths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deployStartTime")
    def deploy_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deploy_start_time.setter
    def deploy_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override.setter
    def override(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sequencedRollout")
    def sequenced_rollout(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sequenced_rollout.setter
    def sequenced_rollout(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class EnvironmentApiRevisionDeployment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        override: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
        sequenced_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EnvironmentApiRevisionDeploymentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api: Optional[pulumi.Input[_builtins.str]] = ...,
        basepaths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        deploy_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        override: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
        sequenced_rollout: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EnvironmentApiRevisionDeployment: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def basepaths(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deployStartTime")
    def deploy_start_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sequencedRollout")
    def sequenced_rollout(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
