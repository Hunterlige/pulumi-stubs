import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CxFlowArgs", "CxFlow"]

@pulumi.input_type
class CxFlowArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        advanced_settings: Optional[pulumi.Input[CxFlowAdvancedSettingsArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        event_handlers: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerArgs]]]
        ] = ...,
        is_default_start_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[CxFlowKnowledgeConnectorSettingsArgs]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        nlu_settings: Optional[pulumi.Input[CxFlowNluSettingsArgs]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> Optional[pulumi.Input[CxFlowAdvancedSettingsArgs]]: ...
    @advanced_settings.setter
    def advanced_settings(
        self, value: Optional[pulumi.Input[CxFlowAdvancedSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerArgs]]]]: ...
    @event_handlers.setter
    def event_handlers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDefaultStartFlow")
    def is_default_start_flow(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default_start_flow.setter
    def is_default_start_flow(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsArgs]]: ...
    @knowledge_connector_settings.setter
    def knowledge_connector_settings(
        self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nluSettings")
    def nlu_settings(self) -> Optional[pulumi.Input[CxFlowNluSettingsArgs]]: ...
    @nlu_settings.setter
    def nlu_settings(self, value: Optional[pulumi.Input[CxFlowNluSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitionRouteGroups")
    def transition_route_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @transition_route_groups.setter
    def transition_route_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitionRoutes")
    def transition_routes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteArgs]]]]: ...
    @transition_routes.setter
    def transition_routes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteArgs]]]
        ],
    ): ...

@pulumi.input_type
class _CxFlowState:
    def __init__(
        __self__,
        *,
        advanced_settings: Optional[pulumi.Input[CxFlowAdvancedSettingsArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        event_handlers: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerArgs]]]
        ] = ...,
        is_default_start_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[CxFlowKnowledgeConnectorSettingsArgs]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        nlu_settings: Optional[pulumi.Input[CxFlowNluSettingsArgs]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> Optional[pulumi.Input[CxFlowAdvancedSettingsArgs]]: ...
    @advanced_settings.setter
    def advanced_settings(
        self, value: Optional[pulumi.Input[CxFlowAdvancedSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerArgs]]]]: ...
    @event_handlers.setter
    def event_handlers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDefaultStartFlow")
    def is_default_start_flow(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default_start_flow.setter
    def is_default_start_flow(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsArgs]]: ...
    @knowledge_connector_settings.setter
    def knowledge_connector_settings(
        self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nluSettings")
    def nlu_settings(self) -> Optional[pulumi.Input[CxFlowNluSettingsArgs]]: ...
    @nlu_settings.setter
    def nlu_settings(self, value: Optional[pulumi.Input[CxFlowNluSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitionRouteGroups")
    def transition_route_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @transition_route_groups.setter
    def transition_route_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitionRoutes")
    def transition_routes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteArgs]]]]: ...
    @transition_routes.setter
    def transition_routes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteArgs]]]
        ],
    ): ...

@pulumi.type_token("gcp:diagflow/cxFlow:CxFlow")
class CxFlow(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_settings: Optional[
            pulumi.Input[
                Union[CxFlowAdvancedSettingsArgs, CxFlowAdvancedSettingsArgsDict]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        event_handlers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxFlowEventHandlerArgs, CxFlowEventHandlerArgsDict]
                    ]
                ]
            ]
        ] = ...,
        is_default_start_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[
                Union[
                    CxFlowKnowledgeConnectorSettingsArgs,
                    CxFlowKnowledgeConnectorSettingsArgsDict,
                ]
            ]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        nlu_settings: Optional[
            pulumi.Input[Union[CxFlowNluSettingsArgs, CxFlowNluSettingsArgsDict]]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxFlowTransitionRouteArgs, CxFlowTransitionRouteArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CxFlowArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_settings: Optional[
            pulumi.Input[
                Union[CxFlowAdvancedSettingsArgs, CxFlowAdvancedSettingsArgsDict]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        event_handlers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxFlowEventHandlerArgs, CxFlowEventHandlerArgsDict]
                    ]
                ]
            ]
        ] = ...,
        is_default_start_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[
                Union[
                    CxFlowKnowledgeConnectorSettingsArgs,
                    CxFlowKnowledgeConnectorSettingsArgsDict,
                ]
            ]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        nlu_settings: Optional[
            pulumi.Input[Union[CxFlowNluSettingsArgs, CxFlowNluSettingsArgsDict]]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxFlowTransitionRouteArgs, CxFlowTransitionRouteArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> CxFlow: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxFlowAdvancedSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(self) -> pulumi.Output[Sequence[outputs.CxFlowEventHandler]]: ...
    @_builtins.property
    @pulumi.getter(name="isDefaultStartFlow")
    def is_default_start_flow(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxFlowKnowledgeConnectorSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nluSettings")
    def nlu_settings(self) -> pulumi.Output[Optional[outputs.CxFlowNluSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitionRouteGroups")
    def transition_route_groups(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="transitionRoutes")
    def transition_routes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CxFlowTransitionRoute]]]: ...
