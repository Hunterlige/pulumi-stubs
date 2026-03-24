import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CxPageArgs", "CxPage"]

@pulumi.input_type
class CxPageArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        advanced_settings: Optional[pulumi.Input[CxPageAdvancedSettingsArgs]] = ...,
        entry_fulfillment: Optional[pulumi.Input[CxPageEntryFulfillmentArgs]] = ...,
        event_handlers: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerArgs]]]
        ] = ...,
        form: Optional[pulumi.Input[CxPageFormArgs]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[CxPageKnowledgeConnectorSettingsArgs]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteArgs]]]
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
    ) -> Optional[pulumi.Input[CxPageAdvancedSettingsArgs]]: ...
    @advanced_settings.setter
    def advanced_settings(
        self, value: Optional[pulumi.Input[CxPageAdvancedSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="entryFulfillment")
    def entry_fulfillment(
        self,
    ) -> Optional[pulumi.Input[CxPageEntryFulfillmentArgs]]: ...
    @entry_fulfillment.setter
    def entry_fulfillment(
        self, value: Optional[pulumi.Input[CxPageEntryFulfillmentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerArgs]]]]: ...
    @event_handlers.setter
    def event_handlers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def form(self) -> Optional[pulumi.Input[CxPageFormArgs]]: ...
    @form.setter
    def form(self, value: Optional[pulumi.Input[CxPageFormArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsArgs]]: ...
    @knowledge_connector_settings.setter
    def knowledge_connector_settings(
        self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteArgs]]]]: ...
    @transition_routes.setter
    def transition_routes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteArgs]]]
        ],
    ): ...

@pulumi.input_type
class _CxPageState:
    def __init__(
        __self__,
        *,
        advanced_settings: Optional[pulumi.Input[CxPageAdvancedSettingsArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_fulfillment: Optional[pulumi.Input[CxPageEntryFulfillmentArgs]] = ...,
        event_handlers: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerArgs]]]
        ] = ...,
        form: Optional[pulumi.Input[CxPageFormArgs]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[CxPageKnowledgeConnectorSettingsArgs]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> Optional[pulumi.Input[CxPageAdvancedSettingsArgs]]: ...
    @advanced_settings.setter
    def advanced_settings(
        self, value: Optional[pulumi.Input[CxPageAdvancedSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryFulfillment")
    def entry_fulfillment(
        self,
    ) -> Optional[pulumi.Input[CxPageEntryFulfillmentArgs]]: ...
    @entry_fulfillment.setter
    def entry_fulfillment(
        self, value: Optional[pulumi.Input[CxPageEntryFulfillmentArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerArgs]]]]: ...
    @event_handlers.setter
    def event_handlers(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def form(self) -> Optional[pulumi.Input[CxPageFormArgs]]: ...
    @form.setter
    def form(self, value: Optional[pulumi.Input[CxPageFormArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsArgs]]: ...
    @knowledge_connector_settings.setter
    def knowledge_connector_settings(
        self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsArgs]]
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
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteArgs]]]]: ...
    @transition_routes.setter
    def transition_routes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteArgs]]]
        ],
    ): ...

@pulumi.type_token("gcp:diagflow/cxPage:CxPage")
class CxPage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_settings: Optional[
            pulumi.Input[
                Union[CxPageAdvancedSettingsArgs, CxPageAdvancedSettingsArgsDict]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_fulfillment: Optional[
            pulumi.Input[
                Union[CxPageEntryFulfillmentArgs, CxPageEntryFulfillmentArgsDict]
            ]
        ] = ...,
        event_handlers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxPageEventHandlerArgs, CxPageEventHandlerArgsDict]
                    ]
                ]
            ]
        ] = ...,
        form: Optional[pulumi.Input[Union[CxPageFormArgs, CxPageFormArgsDict]]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[
                Union[
                    CxPageKnowledgeConnectorSettingsArgs,
                    CxPageKnowledgeConnectorSettingsArgsDict,
                ]
            ]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxPageTransitionRouteArgs, CxPageTransitionRouteArgsDict]
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
        args: CxPageArgs,
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
                Union[CxPageAdvancedSettingsArgs, CxPageAdvancedSettingsArgsDict]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_fulfillment: Optional[
            pulumi.Input[
                Union[CxPageEntryFulfillmentArgs, CxPageEntryFulfillmentArgsDict]
            ]
        ] = ...,
        event_handlers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxPageEventHandlerArgs, CxPageEventHandlerArgsDict]
                    ]
                ]
            ]
        ] = ...,
        form: Optional[pulumi.Input[Union[CxPageFormArgs, CxPageFormArgsDict]]] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[
                Union[
                    CxPageKnowledgeConnectorSettingsArgs,
                    CxPageKnowledgeConnectorSettingsArgsDict,
                ]
            ]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_route_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transition_routes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxPageTransitionRouteArgs, CxPageTransitionRouteArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> CxPage: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxPageAdvancedSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entryFulfillment")
    def entry_fulfillment(
        self,
    ) -> pulumi.Output[Optional[outputs.CxPageEntryFulfillment]]: ...
    @_builtins.property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CxPageEventHandler]]]: ...
    @_builtins.property
    @pulumi.getter
    def form(self) -> pulumi.Output[Optional[outputs.CxPageForm]]: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxPageKnowledgeConnectorSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
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
    ) -> pulumi.Output[Optional[Sequence[outputs.CxPageTransitionRoute]]]: ...
