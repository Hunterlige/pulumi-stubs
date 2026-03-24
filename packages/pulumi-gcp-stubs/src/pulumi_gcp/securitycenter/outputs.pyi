import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FolderCustomModuleCustomConfig",
    "FolderCustomModuleCustomConfigCustomOutput",
    "FolderCustomModuleCustomConfigCustomOutputProperty",
    ...,
    "FolderCustomModuleCustomConfigPredicate",
    "FolderCustomModuleCustomConfigResourceSelector",
    "FolderNotificationConfigStreamingConfig",
    "InstanceIamBindingCondition",
    "InstanceIamMemberCondition",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "NotificationConfigStreamingConfig",
    "OrganizationCustomModuleCustomConfig",
    "OrganizationCustomModuleCustomConfigCustomOutput",
    ...,
    ...,
    "OrganizationCustomModuleCustomConfigPredicate",
    ...,
    "ProjectCustomModuleCustomConfig",
    "ProjectCustomModuleCustomConfigCustomOutput",
    ...,
    ...,
    "ProjectCustomModuleCustomConfigPredicate",
    "ProjectCustomModuleCustomConfigResourceSelector",
    "ProjectNotificationConfigStreamingConfig",
    "SourceIamBindingCondition",
    "SourceIamMemberCondition",
    "V2FolderNotificationConfigStreamingConfig",
    "V2OrganizationNotificationConfigStreamingConfig",
    "V2OrganizationSourceIamBindingCondition",
    "V2OrganizationSourceIamMemberCondition",
    "V2ProjectNotificationConfigStreamingConfig",
]

@pulumi.output_type
class FolderCustomModuleCustomConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predicate: outputs.FolderCustomModuleCustomConfigPredicate,
        recommendation: _builtins.str,
        resource_selector: outputs.FolderCustomModuleCustomConfigResourceSelector,
        severity: _builtins.str,
        custom_output: Optional[
            outputs.FolderCustomModuleCustomConfigCustomOutput
        ] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> outputs.FolderCustomModuleCustomConfigPredicate: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(
        self,
    ) -> outputs.FolderCustomModuleCustomConfigResourceSelector: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(
        self,
    ) -> Optional[outputs.FolderCustomModuleCustomConfigCustomOutput]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FolderCustomModuleCustomConfigCustomOutput(dict):
    def __init__(
        __self__,
        *,
        properties: Optional[
            Sequence[outputs.FolderCustomModuleCustomConfigCustomOutputProperty]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[outputs.FolderCustomModuleCustomConfigCustomOutputProperty]
    ]: ...

@pulumi.output_type
class FolderCustomModuleCustomConfigCustomOutputProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value_expression: Optional[
            outputs.FolderCustomModuleCustomConfigCustomOutputPropertyValueExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(
        self,
    ) -> Optional[
        outputs.FolderCustomModuleCustomConfigCustomOutputPropertyValueExpression
    ]: ...

@pulumi.output_type
class FolderCustomModuleCustomConfigCustomOutputPropertyValueExpression(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FolderCustomModuleCustomConfigPredicate(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FolderCustomModuleCustomConfigResourceSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class FolderNotificationConfigStreamingConfig(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_output: Optional[
            outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput
        ] = ...,
        description: Optional[_builtins.str] = ...,
        predicate: Optional[
            outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicate
        ] = ...,
        recommendation: Optional[_builtins.str] = ...,
        resource_selector: Optional[
            outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector
        ] = ...,
        severity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(
        self,
    ) -> Optional[
        outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def predicate(
        self,
    ) -> Optional[
        outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicate
    ]: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(
        self,
    ) -> Optional[
        outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector
    ]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput(dict):
    def __init__(
        __self__,
        *,
        properties: Optional[
            Sequence[
                outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty
        ]
    ]: ...

@pulumi.output_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value_expression: Optional[
            outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(
        self,
    ) -> Optional[
        outputs.ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression
    ]: ...

@pulumi.output_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression(
    dict
):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicate(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predicate: outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicate,
        recommendation: _builtins.str,
        resource_selector: outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector,
        severity: _builtins.str,
        custom_output: Optional[
            outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput
        ] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def predicate(
        self,
    ) -> outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicate: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(
        self,
    ) -> outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(
        self,
    ) -> Optional[
        outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput(
    dict
):
    def __init__(
        __self__,
        *,
        properties: Optional[
            Sequence[
                outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty
        ]
    ]: ...

@pulumi.output_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value_expression: Optional[
            outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(
        self,
    ) -> Optional[
        outputs.ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression
    ]: ...

@pulumi.output_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression(
    dict
):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicate(
    dict
):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predicate: outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicate,
        recommendation: _builtins.str,
        resource_selector: outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector,
        severity: _builtins.str,
        custom_output: Optional[
            outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput
        ] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def predicate(
        self,
    ) -> outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicate: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(
        self,
    ) -> outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(
        self,
    ) -> Optional[
        outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutput(
    dict
):
    def __init__(
        __self__,
        *,
        properties: Optional[
            Sequence[
                outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[
            outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty
        ]
    ]: ...

@pulumi.output_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputProperty(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value_expression: Optional[
            outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(
        self,
    ) -> Optional[
        outputs.ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression
    ]: ...

@pulumi.output_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpression(
    dict
):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicate(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class NotificationConfigStreamingConfig(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class OrganizationCustomModuleCustomConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predicate: outputs.OrganizationCustomModuleCustomConfigPredicate,
        recommendation: _builtins.str,
        resource_selector: outputs.OrganizationCustomModuleCustomConfigResourceSelector,
        severity: _builtins.str,
        custom_output: Optional[
            outputs.OrganizationCustomModuleCustomConfigCustomOutput
        ] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> outputs.OrganizationCustomModuleCustomConfigPredicate: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(
        self,
    ) -> outputs.OrganizationCustomModuleCustomConfigResourceSelector: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(
        self,
    ) -> Optional[outputs.OrganizationCustomModuleCustomConfigCustomOutput]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationCustomModuleCustomConfigCustomOutput(dict):
    def __init__(
        __self__,
        *,
        properties: Optional[
            Sequence[outputs.OrganizationCustomModuleCustomConfigCustomOutputProperty]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[outputs.OrganizationCustomModuleCustomConfigCustomOutputProperty]
    ]: ...

@pulumi.output_type
class OrganizationCustomModuleCustomConfigCustomOutputProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value_expression: Optional[
            outputs.OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(
        self,
    ) -> Optional[
        outputs.OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpression
    ]: ...

@pulumi.output_type
class OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpression(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationCustomModuleCustomConfigPredicate(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationCustomModuleCustomConfigResourceSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ProjectCustomModuleCustomConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predicate: outputs.ProjectCustomModuleCustomConfigPredicate,
        recommendation: _builtins.str,
        resource_selector: outputs.ProjectCustomModuleCustomConfigResourceSelector,
        severity: _builtins.str,
        custom_output: Optional[
            outputs.ProjectCustomModuleCustomConfigCustomOutput
        ] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> outputs.ProjectCustomModuleCustomConfigPredicate: ...
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(
        self,
    ) -> outputs.ProjectCustomModuleCustomConfigResourceSelector: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(
        self,
    ) -> Optional[outputs.ProjectCustomModuleCustomConfigCustomOutput]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectCustomModuleCustomConfigCustomOutput(dict):
    def __init__(
        __self__,
        *,
        properties: Optional[
            Sequence[outputs.ProjectCustomModuleCustomConfigCustomOutputProperty]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        Sequence[outputs.ProjectCustomModuleCustomConfigCustomOutputProperty]
    ]: ...

@pulumi.output_type
class ProjectCustomModuleCustomConfigCustomOutputProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value_expression: Optional[
            outputs.ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpression
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(
        self,
    ) -> Optional[
        outputs.ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpression
    ]: ...

@pulumi.output_type
class ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpression(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectCustomModuleCustomConfigPredicate(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectCustomModuleCustomConfigResourceSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_types: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ProjectNotificationConfigStreamingConfig(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class SourceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SourceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2FolderNotificationConfigStreamingConfig(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class V2OrganizationNotificationConfigStreamingConfig(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class V2OrganizationSourceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2OrganizationSourceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2ProjectNotificationConfigStreamingConfig(dict):
    def __init__(__self__, *, filter: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
