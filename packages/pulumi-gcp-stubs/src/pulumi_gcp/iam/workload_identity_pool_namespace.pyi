import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkloadIdentityPoolNamespaceArgs", "WorkloadIdentityPoolNamespace"]

@pulumi.input_type
class WorkloadIdentityPoolNamespaceArgs:
    def __init__(
        __self__,
        *,
        workload_identity_pool_id: pulumi.Input[_builtins.str],
        workload_identity_pool_namespace_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> pulumi.Input[_builtins.str]: ...
    @workload_identity_pool_id.setter
    def workload_identity_pool_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolNamespaceId")
    def workload_identity_pool_namespace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workload_identity_pool_namespace_id.setter
    def workload_identity_pool_namespace_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _WorkloadIdentityPoolNamespaceState:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_services: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkloadIdentityPoolNamespaceOwnerServiceArgs]]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_namespace_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerServices")
    def owner_services(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[WorkloadIdentityPoolNamespaceOwnerServiceArgs]]
        ]
    ]: ...
    @owner_services.setter
    def owner_services(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkloadIdentityPoolNamespaceOwnerServiceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_identity_pool_id.setter
    def workload_identity_pool_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolNamespaceId")
    def workload_identity_pool_namespace_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_identity_pool_namespace_id.setter
    def workload_identity_pool_namespace_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class WorkloadIdentityPoolNamespace(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_namespace_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkloadIdentityPoolNamespaceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner_services: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadIdentityPoolNamespaceOwnerServiceArgs,
                            WorkloadIdentityPoolNamespaceOwnerServiceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_namespace_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> WorkloadIdentityPoolNamespace: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerServices")
    def owner_services(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkloadIdentityPoolNamespaceOwnerService]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolNamespaceId")
    def workload_identity_pool_namespace_id(self) -> pulumi.Output[_builtins.str]: ...
