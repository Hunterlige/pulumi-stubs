import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiHubInstanceConfigArgs",
    "ApiHubInstanceConfigArgsDict",
    "CurationEndpointArgs",
    "CurationEndpointArgsDict",
    ...,
    ...,
    "CurationPluginInstanceActionArgs",
    "CurationPluginInstanceActionArgsDict",
    "PluginActionsConfigArgs",
    "PluginActionsConfigArgsDict",
    "PluginConfigTemplateArgs",
    "PluginConfigTemplateArgsDict",
    "PluginConfigTemplateAdditionalConfigTemplateArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "PluginConfigTemplateAuthConfigTemplateArgs",
    "PluginConfigTemplateAuthConfigTemplateArgsDict",
    ...,
    ...,
    "PluginDocumentationArgs",
    "PluginDocumentationArgsDict",
    "PluginHostingServiceArgs",
    "PluginHostingServiceArgsDict",
    "PluginInstanceActionArgs",
    "PluginInstanceActionArgsDict",
    "PluginInstanceActionCurationConfigArgs",
    "PluginInstanceActionCurationConfigArgsDict",
    ...,
    ...,
    "PluginInstanceActionHubInstanceActionArgs",
    "PluginInstanceActionHubInstanceActionArgsDict",
    ...,
    ...,
    "PluginInstanceAuthConfigArgs",
    "PluginInstanceAuthConfigArgsDict",
    "PluginInstanceAuthConfigApiKeyConfigArgs",
    "PluginInstanceAuthConfigApiKeyConfigArgsDict",
    "PluginInstanceAuthConfigApiKeyConfigApiKeyArgs",
    "PluginInstanceAuthConfigApiKeyConfigApiKeyArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PluginInstanceAuthConfigUserPasswordConfigArgs",
    "PluginInstanceAuthConfigUserPasswordConfigArgsDict",
    ...,
    ...,
]

class ApiHubInstanceConfigArgsDict(TypedDict):
    cmek_key_name: NotRequired[pulumi.Input[_builtins.str]]
    disable_search: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    vertex_location: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ApiHubInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        cmek_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_search: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vertex_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cmekKeyName")
    def cmek_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cmek_key_name.setter
    def cmek_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableSearch")
    def disable_search(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_search.setter
    def disable_search(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vertexLocation")
    def vertex_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vertex_location.setter
    def vertex_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CurationEndpointArgsDict(TypedDict):
    application_integration_endpoint_details: pulumi.Input[
        CurationEndpointApplicationIntegrationEndpointDetailsArgsDict
    ]
    ...

@pulumi.input_type
class CurationEndpointArgs:
    def __init__(
        __self__,
        *,
        application_integration_endpoint_details: pulumi.Input[
            CurationEndpointApplicationIntegrationEndpointDetailsArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationIntegrationEndpointDetails")
    def application_integration_endpoint_details(
        self,
    ) -> pulumi.Input[CurationEndpointApplicationIntegrationEndpointDetailsArgs]: ...
    @application_integration_endpoint_details.setter
    def application_integration_endpoint_details(
        self,
        value: pulumi.Input[CurationEndpointApplicationIntegrationEndpointDetailsArgs],
    ): ...

class CurationEndpointApplicationIntegrationEndpointDetailsArgsDict(TypedDict):
    trigger_id: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class CurationEndpointApplicationIntegrationEndpointDetailsArgs:
    def __init__(
        __self__,
        *,
        trigger_id: pulumi.Input[_builtins.str],
        uri: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="triggerId")
    def trigger_id(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_id.setter
    def trigger_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...

class CurationPluginInstanceActionArgsDict(TypedDict):
    action_id: NotRequired[pulumi.Input[_builtins.str]]
    plugin_instance: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CurationPluginInstanceActionArgs:
    def __init__(
        __self__,
        *,
        action_id: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin_instance: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_id.setter
    def action_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pluginInstance")
    def plugin_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugin_instance.setter
    def plugin_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginActionsConfigArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    trigger_mode: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginActionsConfigArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        trigger_mode: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="triggerMode")
    def trigger_mode(self) -> pulumi.Input[_builtins.str]: ...
    @trigger_mode.setter
    def trigger_mode(self, value: pulumi.Input[_builtins.str]): ...

class PluginConfigTemplateArgsDict(TypedDict):
    additional_config_templates: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PluginConfigTemplateAdditionalConfigTemplateArgsDict]]
        ]
    ]
    auth_config_template: NotRequired[
        pulumi.Input[PluginConfigTemplateAuthConfigTemplateArgsDict]
    ]
    ...

@pulumi.input_type
class PluginConfigTemplateArgs:
    def __init__(
        __self__,
        *,
        additional_config_templates: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PluginConfigTemplateAdditionalConfigTemplateArgs]]
            ]
        ] = ...,
        auth_config_template: Optional[
            pulumi.Input[PluginConfigTemplateAuthConfigTemplateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalConfigTemplates")
    def additional_config_templates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PluginConfigTemplateAdditionalConfigTemplateArgs]]
        ]
    ]: ...
    @additional_config_templates.setter
    def additional_config_templates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PluginConfigTemplateAdditionalConfigTemplateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authConfigTemplate")
    def auth_config_template(
        self,
    ) -> Optional[pulumi.Input[PluginConfigTemplateAuthConfigTemplateArgs]]: ...
    @auth_config_template.setter
    def auth_config_template(
        self, value: Optional[pulumi.Input[PluginConfigTemplateAuthConfigTemplateArgs]]
    ): ...

class PluginConfigTemplateAdditionalConfigTemplateArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    value_type: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enum_options: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PluginConfigTemplateAdditionalConfigTemplateEnumOptionArgsDict
                ]
            ]
        ]
    ]
    multi_select_options: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PluginConfigTemplateAdditionalConfigTemplateMultiSelectOptionArgsDict
                ]
            ]
        ]
    ]
    required: NotRequired[pulumi.Input[_builtins.bool]]
    validation_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PluginConfigTemplateAdditionalConfigTemplateArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        value_type: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enum_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PluginConfigTemplateAdditionalConfigTemplateEnumOptionArgs
                    ]
                ]
            ]
        ] = ...,
        multi_select_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PluginConfigTemplateAdditionalConfigTemplateMultiSelectOptionArgs
                    ]
                ]
            ]
        ] = ...,
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
        validation_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Input[_builtins.str]: ...
    @value_type.setter
    def value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enumOptions")
    def enum_options(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PluginConfigTemplateAdditionalConfigTemplateEnumOptionArgs]
            ]
        ]
    ]: ...
    @enum_options.setter
    def enum_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PluginConfigTemplateAdditionalConfigTemplateEnumOptionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiSelectOptions")
    def multi_select_options(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PluginConfigTemplateAdditionalConfigTemplateMultiSelectOptionArgs
                ]
            ]
        ]
    ]: ...
    @multi_select_options.setter
    def multi_select_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PluginConfigTemplateAdditionalConfigTemplateMultiSelectOptionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="validationRegex")
    def validation_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @validation_regex.setter
    def validation_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginConfigTemplateAdditionalConfigTemplateEnumOptionArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PluginConfigTemplateAdditionalConfigTemplateEnumOptionArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginConfigTemplateAdditionalConfigTemplateMultiSelectOptionArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PluginConfigTemplateAdditionalConfigTemplateMultiSelectOptionArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginConfigTemplateAuthConfigTemplateArgsDict(TypedDict):
    supported_auth_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    service_account: NotRequired[
        pulumi.Input[PluginConfigTemplateAuthConfigTemplateServiceAccountArgsDict]
    ]
    ...

@pulumi.input_type
class PluginConfigTemplateAuthConfigTemplateArgs:
    def __init__(
        __self__,
        *,
        supported_auth_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        service_account: Optional[
            pulumi.Input[PluginConfigTemplateAuthConfigTemplateServiceAccountArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportedAuthTypes")
    def supported_auth_types(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @supported_auth_types.setter
    def supported_auth_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(
        self,
    ) -> Optional[
        pulumi.Input[PluginConfigTemplateAuthConfigTemplateServiceAccountArgs]
    ]: ...
    @service_account.setter
    def service_account(
        self,
        value: Optional[
            pulumi.Input[PluginConfigTemplateAuthConfigTemplateServiceAccountArgs]
        ],
    ): ...

class PluginConfigTemplateAuthConfigTemplateServiceAccountArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginConfigTemplateAuthConfigTemplateServiceAccountArgs:
    def __init__(__self__, *, service_account: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...

class PluginDocumentationArgsDict(TypedDict):
    external_uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PluginDocumentationArgs:
    def __init__(
        __self__, *, external_uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalUri")
    def external_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_uri.setter
    def external_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginHostingServiceArgsDict(TypedDict):
    service_uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PluginHostingServiceArgs:
    def __init__(
        __self__, *, service_uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_uri.setter
    def service_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginInstanceActionArgsDict(TypedDict):
    action_id: pulumi.Input[_builtins.str]
    curation_config: NotRequired[
        pulumi.Input[PluginInstanceActionCurationConfigArgsDict]
    ]
    hub_instance_actions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PluginInstanceActionHubInstanceActionArgsDict]]
        ]
    ]
    schedule_cron_expression: NotRequired[pulumi.Input[_builtins.str]]
    schedule_time_zone: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PluginInstanceActionArgs:
    def __init__(
        __self__,
        *,
        action_id: pulumi.Input[_builtins.str],
        curation_config: Optional[
            pulumi.Input[PluginInstanceActionCurationConfigArgs]
        ] = ...,
        hub_instance_actions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PluginInstanceActionHubInstanceActionArgs]]
            ]
        ] = ...,
        schedule_cron_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> pulumi.Input[_builtins.str]: ...
    @action_id.setter
    def action_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="curationConfig")
    def curation_config(
        self,
    ) -> Optional[pulumi.Input[PluginInstanceActionCurationConfigArgs]]: ...
    @curation_config.setter
    def curation_config(
        self, value: Optional[pulumi.Input[PluginInstanceActionCurationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hubInstanceActions")
    def hub_instance_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PluginInstanceActionHubInstanceActionArgs]]]
    ]: ...
    @hub_instance_actions.setter
    def hub_instance_actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PluginInstanceActionHubInstanceActionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleCronExpression")
    def schedule_cron_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_cron_expression.setter
    def schedule_cron_expression(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduleTimeZone")
    def schedule_time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_time_zone.setter
    def schedule_time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginInstanceActionCurationConfigArgsDict(TypedDict):
    curation_type: NotRequired[pulumi.Input[_builtins.str]]
    custom_curation: NotRequired[
        pulumi.Input[PluginInstanceActionCurationConfigCustomCurationArgsDict]
    ]
    ...

@pulumi.input_type
class PluginInstanceActionCurationConfigArgs:
    def __init__(
        __self__,
        *,
        curation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_curation: Optional[
            pulumi.Input[PluginInstanceActionCurationConfigCustomCurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="curationType")
    def curation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @curation_type.setter
    def curation_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customCuration")
    def custom_curation(
        self,
    ) -> Optional[
        pulumi.Input[PluginInstanceActionCurationConfigCustomCurationArgs]
    ]: ...
    @custom_curation.setter
    def custom_curation(
        self,
        value: Optional[
            pulumi.Input[PluginInstanceActionCurationConfigCustomCurationArgs]
        ],
    ): ...

class PluginInstanceActionCurationConfigCustomCurationArgsDict(TypedDict):
    curation: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginInstanceActionCurationConfigCustomCurationArgs:
    def __init__(__self__, *, curation: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def curation(self) -> pulumi.Input[_builtins.str]: ...
    @curation.setter
    def curation(self, value: pulumi.Input[_builtins.str]): ...

class PluginInstanceActionHubInstanceActionArgsDict(TypedDict):
    current_execution_state: NotRequired[pulumi.Input[_builtins.str]]
    last_executions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PluginInstanceActionHubInstanceActionLastExecutionArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PluginInstanceActionHubInstanceActionArgs:
    def __init__(
        __self__,
        *,
        current_execution_state: Optional[pulumi.Input[_builtins.str]] = ...,
        last_executions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PluginInstanceActionHubInstanceActionLastExecutionArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentExecutionState")
    def current_execution_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_execution_state.setter
    def current_execution_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastExecutions")
    def last_executions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PluginInstanceActionHubInstanceActionLastExecutionArgs]
            ]
        ]
    ]: ...
    @last_executions.setter
    def last_executions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PluginInstanceActionHubInstanceActionLastExecutionArgs]
                ]
            ]
        ],
    ): ...

class PluginInstanceActionHubInstanceActionLastExecutionArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    error_message: NotRequired[pulumi.Input[_builtins.str]]
    result: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PluginInstanceActionHubInstanceActionLastExecutionArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        error_message: Optional[pulumi.Input[_builtins.str]] = ...,
        result: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @result.setter
    def result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PluginInstanceAuthConfigArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    api_key_config: NotRequired[
        pulumi.Input[PluginInstanceAuthConfigApiKeyConfigArgsDict]
    ]
    google_service_account_config: NotRequired[
        pulumi.Input[PluginInstanceAuthConfigGoogleServiceAccountConfigArgsDict]
    ]
    oauth2_client_credentials_config: NotRequired[
        pulumi.Input[PluginInstanceAuthConfigOauth2ClientCredentialsConfigArgsDict]
    ]
    user_password_config: NotRequired[
        pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigArgsDict]
    ]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        api_key_config: Optional[
            pulumi.Input[PluginInstanceAuthConfigApiKeyConfigArgs]
        ] = ...,
        google_service_account_config: Optional[
            pulumi.Input[PluginInstanceAuthConfigGoogleServiceAccountConfigArgs]
        ] = ...,
        oauth2_client_credentials_config: Optional[
            pulumi.Input[PluginInstanceAuthConfigOauth2ClientCredentialsConfigArgs]
        ] = ...,
        user_password_config: Optional[
            pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(
        self,
    ) -> Optional[pulumi.Input[PluginInstanceAuthConfigApiKeyConfigArgs]]: ...
    @api_key_config.setter
    def api_key_config(
        self, value: Optional[pulumi.Input[PluginInstanceAuthConfigApiKeyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleServiceAccountConfig")
    def google_service_account_config(
        self,
    ) -> Optional[
        pulumi.Input[PluginInstanceAuthConfigGoogleServiceAccountConfigArgs]
    ]: ...
    @google_service_account_config.setter
    def google_service_account_config(
        self,
        value: Optional[
            pulumi.Input[PluginInstanceAuthConfigGoogleServiceAccountConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentialsConfig")
    def oauth2_client_credentials_config(
        self,
    ) -> Optional[
        pulumi.Input[PluginInstanceAuthConfigOauth2ClientCredentialsConfigArgs]
    ]: ...
    @oauth2_client_credentials_config.setter
    def oauth2_client_credentials_config(
        self,
        value: Optional[
            pulumi.Input[PluginInstanceAuthConfigOauth2ClientCredentialsConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPasswordConfig")
    def user_password_config(
        self,
    ) -> Optional[pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigArgs]]: ...
    @user_password_config.setter
    def user_password_config(
        self,
        value: Optional[pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigArgs]],
    ): ...

class PluginInstanceAuthConfigApiKeyConfigArgsDict(TypedDict):
    api_key: pulumi.Input[PluginInstanceAuthConfigApiKeyConfigApiKeyArgsDict]
    http_element_location: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigApiKeyConfigArgs:
    def __init__(
        __self__,
        *,
        api_key: pulumi.Input[PluginInstanceAuthConfigApiKeyConfigApiKeyArgs],
        http_element_location: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(
        self,
    ) -> pulumi.Input[PluginInstanceAuthConfigApiKeyConfigApiKeyArgs]: ...
    @api_key.setter
    def api_key(
        self, value: pulumi.Input[PluginInstanceAuthConfigApiKeyConfigApiKeyArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpElementLocation")
    def http_element_location(self) -> pulumi.Input[_builtins.str]: ...
    @http_element_location.setter
    def http_element_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PluginInstanceAuthConfigApiKeyConfigApiKeyArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigApiKeyConfigApiKeyArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class PluginInstanceAuthConfigGoogleServiceAccountConfigArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigGoogleServiceAccountConfigArgs:
    def __init__(__self__, *, service_account: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...

class PluginInstanceAuthConfigOauth2ClientCredentialsConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[
        PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecretArgsDict
    ]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigOauth2ClientCredentialsConfigArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[
            PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecretArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> pulumi.Input[
        PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecretArgs
    ]: ...
    @client_secret.setter
    def client_secret(
        self,
        value: pulumi.Input[
            PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecretArgs
        ],
    ): ...

class PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecretArgsDict(
    TypedDict
):
    secret_version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigOauth2ClientCredentialsConfigClientSecretArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class PluginInstanceAuthConfigUserPasswordConfigArgsDict(TypedDict):
    password: pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigPasswordArgsDict]
    username: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigUserPasswordConfigArgs:
    def __init__(
        __self__,
        *,
        password: pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigPasswordArgs],
        username: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(
        self,
    ) -> pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigPasswordArgs]: ...
    @password.setter
    def password(
        self,
        value: pulumi.Input[PluginInstanceAuthConfigUserPasswordConfigPasswordArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class PluginInstanceAuthConfigUserPasswordConfigPasswordArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PluginInstanceAuthConfigUserPasswordConfigPasswordArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...
