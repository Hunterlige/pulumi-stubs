

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FolderCustomModuleCustomConfigArgs', 'FolderCustomModuleCustomConfigArgsDict', 'FolderCustomModuleCustomConfigCustomOutputArgs', 'FolderCustomModuleCustomConfigCustomOutputArgsDict', ..., ..., ..., ..., 'FolderCustomModuleCustomConfigPredicateArgs', 'FolderCustomModuleCustomConfigPredicateArgsDict', 'FolderCustomModuleCustomConfigResourceSelectorArgs', ..., 'FolderNotificationConfigStreamingConfigArgs', 'FolderNotificationConfigStreamingConfigArgsDict', 'InstanceIamBindingConditionArgs', 'InstanceIamBindingConditionArgsDict', 'InstanceIamMemberConditionArgs', 'InstanceIamMemberConditionArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'NotificationConfigStreamingConfigArgs', 'NotificationConfigStreamingConfigArgsDict', 'OrganizationCustomModuleCustomConfigArgs', 'OrganizationCustomModuleCustomConfigArgsDict', ..., ..., ..., ..., ..., ..., 'OrganizationCustomModuleCustomConfigPredicateArgs', ..., ..., ..., 'ProjectCustomModuleCustomConfigArgs', 'ProjectCustomModuleCustomConfigArgsDict', 'ProjectCustomModuleCustomConfigCustomOutputArgs', ..., ..., ..., ..., ..., 'ProjectCustomModuleCustomConfigPredicateArgs', 'ProjectCustomModuleCustomConfigPredicateArgsDict', ..., ..., 'ProjectNotificationConfigStreamingConfigArgs', 'ProjectNotificationConfigStreamingConfigArgsDict', 'SourceIamBindingConditionArgs', 'SourceIamBindingConditionArgsDict', 'SourceIamMemberConditionArgs', 'SourceIamMemberConditionArgsDict', 'V2FolderNotificationConfigStreamingConfigArgs', 'V2FolderNotificationConfigStreamingConfigArgsDict', ..., ..., 'V2OrganizationSourceIamBindingConditionArgs', 'V2OrganizationSourceIamBindingConditionArgsDict', 'V2OrganizationSourceIamMemberConditionArgs', 'V2OrganizationSourceIamMemberConditionArgsDict', 'V2ProjectNotificationConfigStreamingConfigArgs', 'V2ProjectNotificationConfigStreamingConfigArgsDict']
class FolderCustomModuleCustomConfigArgsDict(TypedDict):
    predicate: pulumi.Input[FolderCustomModuleCustomConfigPredicateArgsDict]
    recommendation: pulumi.Input[_builtins.str]
    resource_selector: pulumi.Input[FolderCustomModuleCustomConfigResourceSelectorArgsDict]
    severity: pulumi.Input[_builtins.str]
    custom_output: NotRequired[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FolderCustomModuleCustomConfigArgs:
    def __init__(__self__, *, predicate: pulumi.Input[FolderCustomModuleCustomConfigPredicateArgs], recommendation: pulumi.Input[_builtins.str], resource_selector: pulumi.Input[FolderCustomModuleCustomConfigResourceSelectorArgs], severity: pulumi.Input[_builtins.str], custom_output: Optional[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> pulumi.Input[FolderCustomModuleCustomConfigPredicateArgs]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: pulumi.Input[FolderCustomModuleCustomConfigPredicateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @recommendation.setter
    def recommendation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(self) -> pulumi.Input[FolderCustomModuleCustomConfigResourceSelectorArgs]:
        
        ...
    
    @resource_selector.setter
    def resource_selector(self, value: pulumi.Input[FolderCustomModuleCustomConfigResourceSelectorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(self) -> Optional[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputArgs]]:
        
        ...
    
    @custom_output.setter
    def custom_output(self, value: Optional[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FolderCustomModuleCustomConfigCustomOutputArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyArgsDict]]]]


@pulumi.input_type
class FolderCustomModuleCustomConfigCustomOutputArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyArgs]]]]): # -> None:
        ...
    


class FolderCustomModuleCustomConfigCustomOutputPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value_expression: NotRequired[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict]]


@pulumi.input_type
class FolderCustomModuleCustomConfigCustomOutputPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value_expression: Optional[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(self) -> Optional[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]:
        
        ...
    
    @value_expression.setter
    def value_expression(self, value: Optional[pulumi.Input[FolderCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]): # -> None:
        ...
    


class FolderCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FolderCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FolderCustomModuleCustomConfigPredicateArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FolderCustomModuleCustomConfigPredicateArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FolderCustomModuleCustomConfigResourceSelectorArgsDict(TypedDict):
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class FolderCustomModuleCustomConfigResourceSelectorArgs:
    def __init__(__self__, *, resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class FolderNotificationConfigStreamingConfigArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]


@pulumi.input_type
class FolderNotificationConfigStreamingConfigArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class InstanceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigArgsDict(TypedDict):
    custom_output: NotRequired[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    predicate: NotRequired[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgsDict]]
    recommendation: NotRequired[pulumi.Input[_builtins.str]]
    resource_selector: NotRequired[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgsDict]]
    severity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigArgs:
    def __init__(__self__, *, custom_output: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., predicate: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs]] = ..., recommendation: Optional[pulumi.Input[_builtins.str]] = ..., resource_selector: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs]] = ..., severity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(self) -> Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]]:
        
        ...
    
    @custom_output.setter
    def custom_output(self, value: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs]]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recommendation.setter
    def recommendation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(self) -> Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs]]:
        
        ...
    
    @resource_selector.setter
    def resource_selector(self, value: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgsDict]]]]


@pulumi.input_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]]): # -> None:
        ...
    


class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value_expression: NotRequired[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict]]


@pulumi.input_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value_expression: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(self) -> Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]:
        
        ...
    
    @value_expression.setter
    def value_expression(self, value: Optional[pulumi.Input[ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]): # -> None:
        ...
    


class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgsDict(TypedDict):
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ManagementFolderSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs:
    def __init__(__self__, *, resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgsDict(TypedDict):
    predicate: pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgsDict]
    recommendation: pulumi.Input[_builtins.str]
    resource_selector: pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgsDict]
    severity: pulumi.Input[_builtins.str]
    custom_output: NotRequired[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigArgs:
    def __init__(__self__, *, predicate: pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs], recommendation: pulumi.Input[_builtins.str], resource_selector: pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs], severity: pulumi.Input[_builtins.str], custom_output: Optional[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @recommendation.setter
    def recommendation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(self) -> pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs]:
        
        ...
    
    @resource_selector.setter
    def resource_selector(self, value: pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(self) -> Optional[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]]:
        
        ...
    
    @custom_output.setter
    def custom_output(self, value: Optional[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgsDict]]]]


@pulumi.input_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]]): # -> None:
        ...
    


class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value_expression: NotRequired[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict]]


@pulumi.input_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value_expression: Optional[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(self) -> Optional[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]:
        
        ...
    
    @value_expression.setter
    def value_expression(self, value: Optional[pulumi.Input[ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]): # -> None:
        ...
    


class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgsDict(TypedDict):
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ManagementOrganizationSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs:
    def __init__(__self__, *, resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigArgsDict(TypedDict):
    predicate: pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgsDict]
    recommendation: pulumi.Input[_builtins.str]
    resource_selector: pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgsDict]
    severity: pulumi.Input[_builtins.str]
    custom_output: NotRequired[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigArgs:
    def __init__(__self__, *, predicate: pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs], recommendation: pulumi.Input[_builtins.str], resource_selector: pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs], severity: pulumi.Input[_builtins.str], custom_output: Optional[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @recommendation.setter
    def recommendation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(self) -> pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs]:
        
        ...
    
    @resource_selector.setter
    def resource_selector(self, value: pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(self) -> Optional[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]]:
        
        ...
    
    @custom_output.setter
    def custom_output(self, value: Optional[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgsDict]]]]


@pulumi.input_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs]]]]): # -> None:
        ...
    


class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value_expression: NotRequired[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict]]


@pulumi.input_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value_expression: Optional[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(self) -> Optional[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]:
        
        ...
    
    @value_expression.setter
    def value_expression(self, value: Optional[pulumi.Input[ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]): # -> None:
        ...
    


class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigPredicateArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgsDict(TypedDict):
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ManagementProjectSecurityHealthAnalyticsCustomModuleCustomConfigResourceSelectorArgs:
    def __init__(__self__, *, resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class NotificationConfigStreamingConfigArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]


@pulumi.input_type
class NotificationConfigStreamingConfigArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class OrganizationCustomModuleCustomConfigArgsDict(TypedDict):
    predicate: pulumi.Input[OrganizationCustomModuleCustomConfigPredicateArgsDict]
    recommendation: pulumi.Input[_builtins.str]
    resource_selector: pulumi.Input[OrganizationCustomModuleCustomConfigResourceSelectorArgsDict]
    severity: pulumi.Input[_builtins.str]
    custom_output: NotRequired[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OrganizationCustomModuleCustomConfigArgs:
    def __init__(__self__, *, predicate: pulumi.Input[OrganizationCustomModuleCustomConfigPredicateArgs], recommendation: pulumi.Input[_builtins.str], resource_selector: pulumi.Input[OrganizationCustomModuleCustomConfigResourceSelectorArgs], severity: pulumi.Input[_builtins.str], custom_output: Optional[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> pulumi.Input[OrganizationCustomModuleCustomConfigPredicateArgs]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: pulumi.Input[OrganizationCustomModuleCustomConfigPredicateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @recommendation.setter
    def recommendation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(self) -> pulumi.Input[OrganizationCustomModuleCustomConfigResourceSelectorArgs]:
        
        ...
    
    @resource_selector.setter
    def resource_selector(self, value: pulumi.Input[OrganizationCustomModuleCustomConfigResourceSelectorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(self) -> Optional[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputArgs]]:
        
        ...
    
    @custom_output.setter
    def custom_output(self, value: Optional[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OrganizationCustomModuleCustomConfigCustomOutputArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyArgsDict]]]]


@pulumi.input_type
class OrganizationCustomModuleCustomConfigCustomOutputArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyArgs]]]]): # -> None:
        ...
    


class OrganizationCustomModuleCustomConfigCustomOutputPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value_expression: NotRequired[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict]]


@pulumi.input_type
class OrganizationCustomModuleCustomConfigCustomOutputPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value_expression: Optional[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(self) -> Optional[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]:
        
        ...
    
    @value_expression.setter
    def value_expression(self, value: Optional[pulumi.Input[OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]): # -> None:
        ...
    


class OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OrganizationCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OrganizationCustomModuleCustomConfigPredicateArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OrganizationCustomModuleCustomConfigPredicateArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OrganizationCustomModuleCustomConfigResourceSelectorArgsDict(TypedDict):
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class OrganizationCustomModuleCustomConfigResourceSelectorArgs:
    def __init__(__self__, *, resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ProjectCustomModuleCustomConfigArgsDict(TypedDict):
    predicate: pulumi.Input[ProjectCustomModuleCustomConfigPredicateArgsDict]
    recommendation: pulumi.Input[_builtins.str]
    resource_selector: pulumi.Input[ProjectCustomModuleCustomConfigResourceSelectorArgsDict]
    severity: pulumi.Input[_builtins.str]
    custom_output: NotRequired[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProjectCustomModuleCustomConfigArgs:
    def __init__(__self__, *, predicate: pulumi.Input[ProjectCustomModuleCustomConfigPredicateArgs], recommendation: pulumi.Input[_builtins.str], resource_selector: pulumi.Input[ProjectCustomModuleCustomConfigResourceSelectorArgs], severity: pulumi.Input[_builtins.str], custom_output: Optional[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> pulumi.Input[ProjectCustomModuleCustomConfigPredicateArgs]:
        
        ...
    
    @predicate.setter
    def predicate(self, value: pulumi.Input[ProjectCustomModuleCustomConfigPredicateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @recommendation.setter
    def recommendation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(self) -> pulumi.Input[ProjectCustomModuleCustomConfigResourceSelectorArgs]:
        
        ...
    
    @resource_selector.setter
    def resource_selector(self, value: pulumi.Input[ProjectCustomModuleCustomConfigResourceSelectorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(self) -> Optional[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputArgs]]:
        
        ...
    
    @custom_output.setter
    def custom_output(self, value: Optional[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProjectCustomModuleCustomConfigCustomOutputArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Sequence[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyArgsDict]]]]


@pulumi.input_type
class ProjectCustomModuleCustomConfigCustomOutputArgs:
    def __init__(__self__, *, properties: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyArgs]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyArgs]]]]): # -> None:
        ...
    


class ProjectCustomModuleCustomConfigCustomOutputPropertyArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value_expression: NotRequired[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict]]


@pulumi.input_type
class ProjectCustomModuleCustomConfigCustomOutputPropertyArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value_expression: Optional[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(self) -> Optional[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]:
        
        ...
    
    @value_expression.setter
    def value_expression(self, value: Optional[pulumi.Input[ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs]]): # -> None:
        ...
    


class ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProjectCustomModuleCustomConfigCustomOutputPropertyValueExpressionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProjectCustomModuleCustomConfigPredicateArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProjectCustomModuleCustomConfigPredicateArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProjectCustomModuleCustomConfigResourceSelectorArgsDict(TypedDict):
    resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ProjectCustomModuleCustomConfigResourceSelectorArgs:
    def __init__(__self__, *, resource_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @resource_types.setter
    def resource_types(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ProjectNotificationConfigStreamingConfigArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]


@pulumi.input_type
class ProjectNotificationConfigStreamingConfigArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SourceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SourceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SourceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SourceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2FolderNotificationConfigStreamingConfigArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]


@pulumi.input_type
class V2FolderNotificationConfigStreamingConfigArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class V2OrganizationNotificationConfigStreamingConfigArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]


@pulumi.input_type
class V2OrganizationNotificationConfigStreamingConfigArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class V2OrganizationSourceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2OrganizationSourceIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2OrganizationSourceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2OrganizationSourceIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2ProjectNotificationConfigStreamingConfigArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]


@pulumi.input_type
class V2ProjectNotificationConfigStreamingConfigArgs:
    def __init__(__self__, *, filter: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


