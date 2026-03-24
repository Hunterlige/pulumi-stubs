import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "WorkloadIdentityPoolManagedIdentityArgs",
    "WorkloadIdentityPoolManagedIdentity",
]

@pulumi.input_type
class WorkloadIdentityPoolManagedIdentityArgs:
    def __init__(
        __self__,
        *,
        workload_identity_pool_id: pulumi.Input[_builtins.str],
        workload_identity_pool_managed_identity_id: pulumi.Input[_builtins.str],
        workload_identity_pool_namespace_id: pulumi.Input[_builtins.str],
        attestation_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WorkloadIdentityPoolManagedIdentityAttestationRuleArgs]
                ]
            ]
        ] = ...,
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
    @pulumi.getter(name="workloadIdentityPoolManagedIdentityId")
    def workload_identity_pool_managed_identity_id(
        self,
    ) -> pulumi.Input[_builtins.str]: ...
    @workload_identity_pool_managed_identity_id.setter
    def workload_identity_pool_managed_identity_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolNamespaceId")
    def workload_identity_pool_namespace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workload_identity_pool_namespace_id.setter
    def workload_identity_pool_namespace_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="attestationRules")
    def attestation_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[WorkloadIdentityPoolManagedIdentityAttestationRuleArgs]
            ]
        ]
    ]: ...
    @attestation_rules.setter
    def attestation_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WorkloadIdentityPoolManagedIdentityAttestationRuleArgs]
                ]
            ]
        ],
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
class _WorkloadIdentityPoolManagedIdentityState:
    def __init__(
        __self__,
        *,
        attestation_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WorkloadIdentityPoolManagedIdentityAttestationRuleArgs]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_managed_identity_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        workload_identity_pool_namespace_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attestationRules")
    def attestation_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[WorkloadIdentityPoolManagedIdentityAttestationRuleArgs]
            ]
        ]
    ]: ...
    @attestation_rules.setter
    def attestation_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WorkloadIdentityPoolManagedIdentityAttestationRuleArgs]
                ]
            ]
        ],
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="workloadIdentityPoolManagedIdentityId")
    def workload_identity_pool_managed_identity_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload_identity_pool_managed_identity_id.setter
    def workload_identity_pool_managed_identity_id(
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
class WorkloadIdentityPoolManagedIdentity(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        attestation_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadIdentityPoolManagedIdentityAttestationRuleArgs,
                            WorkloadIdentityPoolManagedIdentityAttestationRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_managed_identity_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        workload_identity_pool_namespace_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkloadIdentityPoolManagedIdentityArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        attestation_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadIdentityPoolManagedIdentityAttestationRuleArgs,
                            WorkloadIdentityPoolManagedIdentityAttestationRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload_identity_pool_managed_identity_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        workload_identity_pool_namespace_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> WorkloadIdentityPoolManagedIdentity: ...
    @_builtins.property
    @pulumi.getter(name="attestationRules")
    def attestation_rules(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.WorkloadIdentityPoolManagedIdentityAttestationRule]]
    ]: ...
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
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolId")
    def workload_identity_pool_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolManagedIdentityId")
    def workload_identity_pool_managed_identity_id(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workloadIdentityPoolNamespaceId")
    def workload_identity_pool_namespace_id(self) -> pulumi.Output[_builtins.str]: ...
