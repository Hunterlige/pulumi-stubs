import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssessmentAssessmentReportsDestinationArgs",
    "AssessmentAssessmentReportsDestinationArgsDict",
    "AssessmentRoleArgs",
    "AssessmentRoleArgsDict",
    "AssessmentRolesAllArgs",
    "AssessmentRolesAllArgsDict",
    "AssessmentScopeArgs",
    "AssessmentScopeArgsDict",
    "AssessmentScopeAwsAccountArgs",
    "AssessmentScopeAwsAccountArgsDict",
    "AssessmentScopeAwsServiceArgs",
    "AssessmentScopeAwsServiceArgsDict",
    "ControlControlMappingSourceArgs",
    "ControlControlMappingSourceArgsDict",
    "ControlControlMappingSourceSourceKeywordArgs",
    "ControlControlMappingSourceSourceKeywordArgsDict",
    "FrameworkControlSetArgs",
    "FrameworkControlSetArgsDict",
    "FrameworkControlSetControlArgs",
    "FrameworkControlSetControlArgsDict",
]

class AssessmentAssessmentReportsDestinationArgsDict(TypedDict):
    destination: pulumi.Input[_builtins.str]
    destination_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AssessmentAssessmentReportsDestinationArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[_builtins.str],
        destination_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Input[_builtins.str]: ...
    @destination_type.setter
    def destination_type(self, value: pulumi.Input[_builtins.str]): ...

class AssessmentRoleArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    role_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AssessmentRoleArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        role_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Input[_builtins.str]: ...
    @role_type.setter
    def role_type(self, value: pulumi.Input[_builtins.str]): ...

class AssessmentRolesAllArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    role_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AssessmentRolesAllArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        role_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Input[_builtins.str]: ...
    @role_type.setter
    def role_type(self, value: pulumi.Input[_builtins.str]): ...

class AssessmentScopeArgsDict(TypedDict):
    aws_accounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsAccountArgsDict]]]
    ]
    aws_services: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsServiceArgsDict]]]
    ]
    ...

@pulumi.input_type
class AssessmentScopeArgs:
    def __init__(
        __self__,
        *,
        aws_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsAccountArgs]]]
        ] = ...,
        aws_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsServiceArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccounts")
    def aws_accounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsAccountArgs]]]
    ]: ...
    @aws_accounts.setter
    def aws_accounts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsAccountArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="awsServices")
    def aws_services(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsServiceArgs]]]
    ]: ...
    @aws_services.setter
    def aws_services(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssessmentScopeAwsServiceArgs]]]
        ],
    ): ...

class AssessmentScopeAwsAccountArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AssessmentScopeAwsAccountArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class AssessmentScopeAwsServiceArgsDict(TypedDict):
    service_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AssessmentScopeAwsServiceArgs:
    def __init__(__self__, *, service_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...

class ControlControlMappingSourceArgsDict(TypedDict):
    source_name: pulumi.Input[_builtins.str]
    source_set_up_option: pulumi.Input[_builtins.str]
    source_type: pulumi.Input[_builtins.str]
    source_description: NotRequired[pulumi.Input[_builtins.str]]
    source_frequency: NotRequired[pulumi.Input[_builtins.str]]
    source_id: NotRequired[pulumi.Input[_builtins.str]]
    source_keyword: NotRequired[
        pulumi.Input[ControlControlMappingSourceSourceKeywordArgsDict]
    ]
    troubleshooting_text: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ControlControlMappingSourceArgs:
    def __init__(
        __self__,
        *,
        source_name: pulumi.Input[_builtins.str],
        source_set_up_option: pulumi.Input[_builtins.str],
        source_type: pulumi.Input[_builtins.str],
        source_description: Optional[pulumi.Input[_builtins.str]] = ...,
        source_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_keyword: Optional[
            pulumi.Input[ControlControlMappingSourceSourceKeywordArgs]
        ] = ...,
        troubleshooting_text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_name.setter
    def source_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceSetUpOption")
    def source_set_up_option(self) -> pulumi.Input[_builtins.str]: ...
    @source_set_up_option.setter
    def source_set_up_option(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Input[_builtins.str]: ...
    @source_type.setter
    def source_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDescription")
    def source_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_description.setter
    def source_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFrequency")
    def source_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_frequency.setter
    def source_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceKeyword")
    def source_keyword(
        self,
    ) -> Optional[pulumi.Input[ControlControlMappingSourceSourceKeywordArgs]]: ...
    @source_keyword.setter
    def source_keyword(
        self,
        value: Optional[pulumi.Input[ControlControlMappingSourceSourceKeywordArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="troubleshootingText")
    def troubleshooting_text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @troubleshooting_text.setter
    def troubleshooting_text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ControlControlMappingSourceSourceKeywordArgsDict(TypedDict):
    keyword_input_type: pulumi.Input[_builtins.str]
    keyword_value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ControlControlMappingSourceSourceKeywordArgs:
    def __init__(
        __self__,
        *,
        keyword_input_type: pulumi.Input[_builtins.str],
        keyword_value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keywordInputType")
    def keyword_input_type(self) -> pulumi.Input[_builtins.str]: ...
    @keyword_input_type.setter
    def keyword_input_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keywordValue")
    def keyword_value(self) -> pulumi.Input[_builtins.str]: ...
    @keyword_value.setter
    def keyword_value(self, value: pulumi.Input[_builtins.str]): ...

class FrameworkControlSetArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    controls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FrameworkControlSetControlArgsDict]]]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FrameworkControlSetArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        controls: Optional[
            pulumi.Input[Sequence[pulumi.Input[FrameworkControlSetControlArgs]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def controls(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FrameworkControlSetControlArgs]]]
    ]: ...
    @controls.setter
    def controls(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FrameworkControlSetControlArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FrameworkControlSetControlArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FrameworkControlSetControlArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
