import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["V2PolicyOrchestratorForFolderArgs", "V2PolicyOrchestratorForFolder"]

@pulumi.input_type
class V2PolicyOrchestratorForFolderArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        folder_id: pulumi.Input[_builtins.str],
        orchestrated_resource: pulumi.Input[
            V2PolicyOrchestratorForFolderOrchestratedResourceArgs
        ],
        policy_orchestrator_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        orchestration_scope: Optional[
            pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationScopeArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Input[_builtins.str]: ...
    @folder_id.setter
    def folder_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orchestratedResource")
    def orchestrated_resource(
        self,
    ) -> pulumi.Input[V2PolicyOrchestratorForFolderOrchestratedResourceArgs]: ...
    @orchestrated_resource.setter
    def orchestrated_resource(
        self, value: pulumi.Input[V2PolicyOrchestratorForFolderOrchestratedResourceArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyOrchestratorId")
    def policy_orchestrator_id(self) -> pulumi.Input[_builtins.str]: ...
    @policy_orchestrator_id.setter
    def policy_orchestrator_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="orchestrationScope")
    def orchestration_scope(
        self,
    ) -> Optional[
        pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationScopeArgs]
    ]: ...
    @orchestration_scope.setter
    def orchestration_scope(
        self,
        value: Optional[
            pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationScopeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _V2PolicyOrchestratorForFolderState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        orchestrated_resource: Optional[
            pulumi.Input[V2PolicyOrchestratorForFolderOrchestratedResourceArgs]
        ] = ...,
        orchestration_scope: Optional[
            pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationScopeArgs]
        ] = ...,
        orchestration_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationStateArgs]
                ]
            ]
        ] = ...,
        policy_orchestrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orchestratedResource")
    def orchestrated_resource(
        self,
    ) -> Optional[
        pulumi.Input[V2PolicyOrchestratorForFolderOrchestratedResourceArgs]
    ]: ...
    @orchestrated_resource.setter
    def orchestrated_resource(
        self,
        value: Optional[
            pulumi.Input[V2PolicyOrchestratorForFolderOrchestratedResourceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="orchestrationScope")
    def orchestration_scope(
        self,
    ) -> Optional[
        pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationScopeArgs]
    ]: ...
    @orchestration_scope.setter
    def orchestration_scope(
        self,
        value: Optional[
            pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationScopeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="orchestrationStates")
    def orchestration_states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationStateArgs]]
        ]
    ]: ...
    @orchestration_states.setter
    def orchestration_states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[V2PolicyOrchestratorForFolderOrchestrationStateArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyOrchestratorId")
    def policy_orchestrator_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_orchestrator_id.setter
    def policy_orchestrator_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
class V2PolicyOrchestratorForFolder(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        orchestrated_resource: Optional[
            pulumi.Input[
                Union[
                    V2PolicyOrchestratorForFolderOrchestratedResourceArgs,
                    V2PolicyOrchestratorForFolderOrchestratedResourceArgsDict,
                ]
            ]
        ] = ...,
        orchestration_scope: Optional[
            pulumi.Input[
                Union[
                    V2PolicyOrchestratorForFolderOrchestrationScopeArgs,
                    V2PolicyOrchestratorForFolderOrchestrationScopeArgsDict,
                ]
            ]
        ] = ...,
        policy_orchestrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: V2PolicyOrchestratorForFolderArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        orchestrated_resource: Optional[
            pulumi.Input[
                Union[
                    V2PolicyOrchestratorForFolderOrchestratedResourceArgs,
                    V2PolicyOrchestratorForFolderOrchestratedResourceArgsDict,
                ]
            ]
        ] = ...,
        orchestration_scope: Optional[
            pulumi.Input[
                Union[
                    V2PolicyOrchestratorForFolderOrchestrationScopeArgs,
                    V2PolicyOrchestratorForFolderOrchestrationScopeArgsDict,
                ]
            ]
        ] = ...,
        orchestration_states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2PolicyOrchestratorForFolderOrchestrationStateArgs,
                            V2PolicyOrchestratorForFolderOrchestrationStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        policy_orchestrator_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> V2PolicyOrchestratorForFolder: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orchestratedResource")
    def orchestrated_resource(
        self,
    ) -> pulumi.Output[outputs.V2PolicyOrchestratorForFolderOrchestratedResource]: ...
    @_builtins.property
    @pulumi.getter(name="orchestrationScope")
    def orchestration_scope(
        self,
    ) -> pulumi.Output[
        Optional[outputs.V2PolicyOrchestratorForFolderOrchestrationScope]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="orchestrationStates")
    def orchestration_states(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.V2PolicyOrchestratorForFolderOrchestrationState]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="policyOrchestratorId")
    def policy_orchestrator_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
