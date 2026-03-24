import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FhirStoreArgs", "FhirStore"]

@pulumi.input_type
class FhirStoreArgs:
    def __init__(
        __self__,
        *,
        dataset: pulumi.Input[_builtins.str],
        complex_data_type_reference_parsing: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        consent_config: Optional[pulumi.Input[FhirStoreConsentConfigArgs]] = ...,
        default_search_handling_strict: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_referential_integrity: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_resource_versioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_history_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_history_modifications: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_update_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_config: Optional[
            pulumi.Input[FhirStoreNotificationConfigArgs]
        ] = ...,
        notification_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreNotificationConfigArgs]]]
        ] = ...,
        stream_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreStreamConfigArgs]]]
        ] = ...,
        validation_config: Optional[pulumi.Input[FhirStoreValidationConfigArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[_builtins.str]: ...
    @dataset.setter
    def dataset(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="complexDataTypeReferenceParsing")
    def complex_data_type_reference_parsing(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @complex_data_type_reference_parsing.setter
    def complex_data_type_reference_parsing(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="consentConfig")
    def consent_config(self) -> Optional[pulumi.Input[FhirStoreConsentConfigArgs]]: ...
    @consent_config.setter
    def consent_config(
        self, value: Optional[pulumi.Input[FhirStoreConsentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSearchHandlingStrict")
    def default_search_handling_strict(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_search_handling_strict.setter
    def default_search_handling_strict(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableReferentialIntegrity")
    def disable_referential_integrity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_referential_integrity.setter
    def disable_referential_integrity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableResourceVersioning")
    def disable_resource_versioning(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_resource_versioning.setter
    def disable_resource_versioning(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableHistoryImport")
    def enable_history_import(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_history_import.setter
    def enable_history_import(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableHistoryModifications")
    def enable_history_modifications(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_history_modifications.setter
    def enable_history_modifications(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableUpdateCreate")
    def enable_update_create(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_update_create.setter
    def enable_update_create(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="notificationConfig")
    @_utilities.deprecated(...)
    def notification_config(
        self,
    ) -> Optional[pulumi.Input[FhirStoreNotificationConfigArgs]]: ...
    @notification_config.setter
    def notification_config(
        self, value: Optional[pulumi.Input[FhirStoreNotificationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FhirStoreNotificationConfigArgs]]]
    ]: ...
    @notification_configs.setter
    def notification_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreNotificationConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FhirStoreStreamConfigArgs]]]]: ...
    @stream_configs.setter
    def stream_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreStreamConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationConfig")
    def validation_config(
        self,
    ) -> Optional[pulumi.Input[FhirStoreValidationConfigArgs]]: ...
    @validation_config.setter
    def validation_config(
        self, value: Optional[pulumi.Input[FhirStoreValidationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FhirStoreState:
    def __init__(
        __self__,
        *,
        complex_data_type_reference_parsing: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        consent_config: Optional[pulumi.Input[FhirStoreConsentConfigArgs]] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        default_search_handling_strict: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_referential_integrity: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_resource_versioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_history_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_history_modifications: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_update_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_config: Optional[
            pulumi.Input[FhirStoreNotificationConfigArgs]
        ] = ...,
        notification_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreNotificationConfigArgs]]]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreStreamConfigArgs]]]
        ] = ...,
        validation_config: Optional[pulumi.Input[FhirStoreValidationConfigArgs]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complexDataTypeReferenceParsing")
    def complex_data_type_reference_parsing(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @complex_data_type_reference_parsing.setter
    def complex_data_type_reference_parsing(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="consentConfig")
    def consent_config(self) -> Optional[pulumi.Input[FhirStoreConsentConfigArgs]]: ...
    @consent_config.setter
    def consent_config(
        self, value: Optional[pulumi.Input[FhirStoreConsentConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultSearchHandlingStrict")
    def default_search_handling_strict(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_search_handling_strict.setter
    def default_search_handling_strict(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableReferentialIntegrity")
    def disable_referential_integrity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_referential_integrity.setter
    def disable_referential_integrity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableResourceVersioning")
    def disable_resource_versioning(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_resource_versioning.setter
    def disable_resource_versioning(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter(name="enableHistoryImport")
    def enable_history_import(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_history_import.setter
    def enable_history_import(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableHistoryModifications")
    def enable_history_modifications(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_history_modifications.setter
    def enable_history_modifications(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableUpdateCreate")
    def enable_update_create(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_update_create.setter
    def enable_update_create(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="notificationConfig")
    @_utilities.deprecated(...)
    def notification_config(
        self,
    ) -> Optional[pulumi.Input[FhirStoreNotificationConfigArgs]]: ...
    @notification_config.setter
    def notification_config(
        self, value: Optional[pulumi.Input[FhirStoreNotificationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FhirStoreNotificationConfigArgs]]]
    ]: ...
    @notification_configs.setter
    def notification_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreNotificationConfigArgs]]]
        ],
    ): ...
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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FhirStoreStreamConfigArgs]]]]: ...
    @stream_configs.setter
    def stream_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FhirStoreStreamConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationConfig")
    def validation_config(
        self,
    ) -> Optional[pulumi.Input[FhirStoreValidationConfigArgs]]: ...
    @validation_config.setter
    def validation_config(
        self, value: Optional[pulumi.Input[FhirStoreValidationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:healthcare/fhirStore:FhirStore")
class FhirStore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        complex_data_type_reference_parsing: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        consent_config: Optional[
            pulumi.Input[
                Union[FhirStoreConsentConfigArgs, FhirStoreConsentConfigArgsDict]
            ]
        ] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        default_search_handling_strict: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_referential_integrity: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_resource_versioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_history_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_history_modifications: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_update_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_config: Optional[
            pulumi.Input[
                Union[
                    FhirStoreNotificationConfigArgs, FhirStoreNotificationConfigArgsDict
                ]
            ]
        ] = ...,
        notification_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FhirStoreNotificationConfigArgs,
                            FhirStoreNotificationConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        stream_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[FhirStoreStreamConfigArgs, FhirStoreStreamConfigArgsDict]
                    ]
                ]
            ]
        ] = ...,
        validation_config: Optional[
            pulumi.Input[
                Union[FhirStoreValidationConfigArgs, FhirStoreValidationConfigArgsDict]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FhirStoreArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        complex_data_type_reference_parsing: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        consent_config: Optional[
            pulumi.Input[
                Union[FhirStoreConsentConfigArgs, FhirStoreConsentConfigArgsDict]
            ]
        ] = ...,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        default_search_handling_strict: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_referential_integrity: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_resource_versioning: Optional[pulumi.Input[_builtins.bool]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_history_import: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_history_modifications: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_update_create: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_config: Optional[
            pulumi.Input[
                Union[
                    FhirStoreNotificationConfigArgs, FhirStoreNotificationConfigArgsDict
                ]
            ]
        ] = ...,
        notification_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FhirStoreNotificationConfigArgs,
                            FhirStoreNotificationConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[FhirStoreStreamConfigArgs, FhirStoreStreamConfigArgsDict]
                    ]
                ]
            ]
        ] = ...,
        validation_config: Optional[
            pulumi.Input[
                Union[FhirStoreValidationConfigArgs, FhirStoreValidationConfigArgsDict]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FhirStore: ...
    @_builtins.property
    @pulumi.getter(name="complexDataTypeReferenceParsing")
    def complex_data_type_reference_parsing(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consentConfig")
    def consent_config(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirStoreConsentConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultSearchHandlingStrict")
    def default_search_handling_strict(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="disableReferentialIntegrity")
    def disable_referential_integrity(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="disableResourceVersioning")
    def disable_resource_versioning(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHistoryImport")
    def enable_history_import(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableHistoryModifications")
    def enable_history_modifications(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableUpdateCreate")
    def enable_update_create(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    @_utilities.deprecated(...)
    def notification_config(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirStoreNotificationConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationConfigs")
    def notification_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FhirStoreNotificationConfig]]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamConfigs")
    def stream_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FhirStoreStreamConfig]]]: ...
    @_builtins.property
    @pulumi.getter(name="validationConfig")
    def validation_config(
        self,
    ) -> pulumi.Output[Optional[outputs.FhirStoreValidationConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
