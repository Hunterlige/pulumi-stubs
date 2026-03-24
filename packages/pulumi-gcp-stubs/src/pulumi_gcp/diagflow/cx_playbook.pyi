import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CxPlaybookArgs", "CxPlaybook"]

@pulumi.input_type
class CxPlaybookArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        goal: pulumi.Input[_builtins.str],
        instruction: Optional[pulumi.Input[CxPlaybookInstructionArgs]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[CxPlaybookLlmModelSettingsArgs]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        playbook_type: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def goal(self) -> pulumi.Input[_builtins.str]: ...
    @goal.setter
    def goal(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> Optional[pulumi.Input[CxPlaybookInstructionArgs]]: ...
    @instruction.setter
    def instruction(self, value: Optional[pulumi.Input[CxPlaybookInstructionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> Optional[pulumi.Input[CxPlaybookLlmModelSettingsArgs]]: ...
    @llm_model_settings.setter
    def llm_model_settings(
        self, value: Optional[pulumi.Input[CxPlaybookLlmModelSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="playbookType")
    def playbook_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @playbook_type.setter
    def playbook_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="referencedTools")
    def referenced_tools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @referenced_tools.setter
    def referenced_tools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _CxPlaybookState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        goal: Optional[pulumi.Input[_builtins.str]] = ...,
        instruction: Optional[pulumi.Input[CxPlaybookInstructionArgs]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[CxPlaybookLlmModelSettingsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        playbook_type: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_flows: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        referenced_playbooks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        referenced_tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        token_count: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def goal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @goal.setter
    def goal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> Optional[pulumi.Input[CxPlaybookInstructionArgs]]: ...
    @instruction.setter
    def instruction(self, value: Optional[pulumi.Input[CxPlaybookInstructionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> Optional[pulumi.Input[CxPlaybookLlmModelSettingsArgs]]: ...
    @llm_model_settings.setter
    def llm_model_settings(
        self, value: Optional[pulumi.Input[CxPlaybookLlmModelSettingsArgs]]
    ): ...
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
    @pulumi.getter(name="playbookType")
    def playbook_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @playbook_type.setter
    def playbook_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="referencedFlows")
    def referenced_flows(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @referenced_flows.setter
    def referenced_flows(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="referencedPlaybooks")
    def referenced_playbooks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @referenced_playbooks.setter
    def referenced_playbooks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="referencedTools")
    def referenced_tools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @referenced_tools.setter
    def referenced_tools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenCount")
    def token_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_count.setter
    def token_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:diagflow/cxPlaybook:CxPlaybook")
class CxPlaybook(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        goal: Optional[pulumi.Input[_builtins.str]] = ...,
        instruction: Optional[
            pulumi.Input[
                Union[CxPlaybookInstructionArgs, CxPlaybookInstructionArgsDict]
            ]
        ] = ...,
        llm_model_settings: Optional[
            pulumi.Input[
                Union[
                    CxPlaybookLlmModelSettingsArgs, CxPlaybookLlmModelSettingsArgsDict
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        playbook_type: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CxPlaybookArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        goal: Optional[pulumi.Input[_builtins.str]] = ...,
        instruction: Optional[
            pulumi.Input[
                Union[CxPlaybookInstructionArgs, CxPlaybookInstructionArgsDict]
            ]
        ] = ...,
        llm_model_settings: Optional[
            pulumi.Input[
                Union[
                    CxPlaybookLlmModelSettingsArgs, CxPlaybookLlmModelSettingsArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        playbook_type: Optional[pulumi.Input[_builtins.str]] = ...,
        referenced_flows: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        referenced_playbooks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        referenced_tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        token_count: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CxPlaybook: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def goal(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> pulumi.Output[Optional[outputs.CxPlaybookInstruction]]: ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxPlaybookLlmModelSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="playbookType")
    def playbook_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="referencedFlows")
    def referenced_flows(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="referencedPlaybooks")
    def referenced_playbooks(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="referencedTools")
    def referenced_tools(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tokenCount")
    def token_count(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
