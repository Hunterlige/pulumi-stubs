import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AssetTypeFormsInputArgs",
    "AssetTypeFormsInputArgsDict",
    "AssetTypeTimeoutsArgs",
    "AssetTypeTimeoutsArgsDict",
    "DomainSingleSignOnArgs",
    "DomainSingleSignOnArgsDict",
    "DomainTimeoutsArgs",
    "DomainTimeoutsArgsDict",
    "EnvironmentLastDeploymentArgs",
    "EnvironmentLastDeploymentArgsDict",
    "EnvironmentLastDeploymentFailureReasonArgs",
    "EnvironmentLastDeploymentFailureReasonArgsDict",
    "EnvironmentProfileUserParameterArgs",
    "EnvironmentProfileUserParameterArgsDict",
    "EnvironmentProvisionedResourceArgs",
    "EnvironmentProvisionedResourceArgsDict",
    "EnvironmentTimeoutsArgs",
    "EnvironmentTimeoutsArgsDict",
    "EnvironmentUserParameterArgs",
    "EnvironmentUserParameterArgsDict",
    "FormTypeImportArgs",
    "FormTypeImportArgsDict",
    "FormTypeModelArgs",
    "FormTypeModelArgsDict",
    "FormTypeTimeoutsArgs",
    "FormTypeTimeoutsArgsDict",
    "GlossaryTermTermRelationsArgs",
    "GlossaryTermTermRelationsArgsDict",
    "GlossaryTermTimeoutsArgs",
    "GlossaryTermTimeoutsArgsDict",
    "ProjectFailureReasonArgs",
    "ProjectFailureReasonArgsDict",
    "ProjectTimeoutsArgs",
    "ProjectTimeoutsArgsDict",
    "UserProfileDetailArgs",
    "UserProfileDetailArgsDict",
    "UserProfileDetailIamArgs",
    "UserProfileDetailIamArgsDict",
    "UserProfileDetailSsoArgs",
    "UserProfileDetailSsoArgsDict",
    "UserProfileTimeoutsArgs",
    "UserProfileTimeoutsArgsDict",
]

class AssetTypeFormsInputArgsDict(TypedDict):
    map_block_key: pulumi.Input[_builtins.str]
    type_identifier: pulumi.Input[_builtins.str]
    type_revision: pulumi.Input[_builtins.str]
    required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AssetTypeFormsInputArgs:
    def __init__(
        __self__,
        *,
        map_block_key: pulumi.Input[_builtins.str],
        type_identifier: pulumi.Input[_builtins.str],
        type_revision: pulumi.Input[_builtins.str],
        required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> pulumi.Input[_builtins.str]: ...
    @map_block_key.setter
    def map_block_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="typeIdentifier")
    def type_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @type_identifier.setter
    def type_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="typeRevision")
    def type_revision(self) -> pulumi.Input[_builtins.str]: ...
    @type_revision.setter
    def type_revision(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AssetTypeTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AssetTypeTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainSingleSignOnArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    user_assignment: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainSingleSignOnArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_assignment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignment")
    def user_assignment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assignment.setter
    def user_assignment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentLastDeploymentArgsDict(TypedDict):
    deployment_id: pulumi.Input[_builtins.str]
    deployment_status: pulumi.Input[_builtins.str]
    deployment_type: pulumi.Input[_builtins.str]
    failure_reasons: pulumi.Input[
        Sequence[pulumi.Input[EnvironmentLastDeploymentFailureReasonArgsDict]]
    ]
    is_deployment_complete: pulumi.Input[_builtins.bool]
    messages: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class EnvironmentLastDeploymentArgs:
    def __init__(
        __self__,
        *,
        deployment_id: pulumi.Input[_builtins.str],
        deployment_status: pulumi.Input[_builtins.str],
        deployment_type: pulumi.Input[_builtins.str],
        failure_reasons: pulumi.Input[
            Sequence[pulumi.Input[EnvironmentLastDeploymentFailureReasonArgs]]
        ],
        is_deployment_complete: pulumi.Input[_builtins.bool],
        messages: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[_builtins.str]: ...
    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Input[_builtins.str]: ...
    @deployment_status.setter
    def deployment_status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Input[_builtins.str]: ...
    @deployment_type.setter
    def deployment_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failureReasons")
    def failure_reasons(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EnvironmentLastDeploymentFailureReasonArgs]]
    ]: ...
    @failure_reasons.setter
    def failure_reasons(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[EnvironmentLastDeploymentFailureReasonArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDeploymentComplete")
    def is_deployment_complete(self) -> pulumi.Input[_builtins.bool]: ...
    @is_deployment_complete.setter
    def is_deployment_complete(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def messages(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @messages.setter
    def messages(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class EnvironmentLastDeploymentFailureReasonArgsDict(TypedDict):
    code: pulumi.Input[_builtins.str]
    message: pulumi.Input[_builtins.str]

@pulumi.input_type
class EnvironmentLastDeploymentFailureReasonArgs:
    def __init__(
        __self__,
        *,
        code: pulumi.Input[_builtins.str],
        message: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Input[_builtins.str]: ...
    @code.setter
    def code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> pulumi.Input[_builtins.str]: ...
    @message.setter
    def message(self, value: pulumi.Input[_builtins.str]): ...

class EnvironmentProfileUserParameterArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentProfileUserParameterArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentProvisionedResourceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    provider: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class EnvironmentProvisionedResourceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        provider: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]: ...
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class EnvironmentTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentUserParameterArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentUserParameterArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FormTypeImportArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    revision: pulumi.Input[_builtins.str]

@pulumi.input_type
class FormTypeImportArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        revision: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Input[_builtins.str]: ...
    @revision.setter
    def revision(self, value: pulumi.Input[_builtins.str]): ...

class FormTypeModelArgsDict(TypedDict):
    smithy: pulumi.Input[_builtins.str]

@pulumi.input_type
class FormTypeModelArgs:
    def __init__(__self__, *, smithy: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def smithy(self) -> pulumi.Input[_builtins.str]: ...
    @smithy.setter
    def smithy(self, value: pulumi.Input[_builtins.str]): ...

class FormTypeTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FormTypeTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GlossaryTermTermRelationsArgsDict(TypedDict):
    classifies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_as: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class GlossaryTermTermRelationsArgs:
    def __init__(
        __self__,
        *,
        classifies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        is_as: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classifies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @classifies.setter
    def classifies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAs")
    def is_as(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @is_as.setter
    def is_as(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GlossaryTermTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GlossaryTermTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectFailureReasonArgsDict(TypedDict):
    code: pulumi.Input[_builtins.str]
    message: pulumi.Input[_builtins.str]

@pulumi.input_type
class ProjectFailureReasonArgs:
    def __init__(
        __self__,
        *,
        code: pulumi.Input[_builtins.str],
        message: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Input[_builtins.str]: ...
    @code.setter
    def code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> pulumi.Input[_builtins.str]: ...
    @message.setter
    def message(self, value: pulumi.Input[_builtins.str]): ...

class ProjectTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserProfileDetailArgsDict(TypedDict):
    iams: pulumi.Input[Sequence[pulumi.Input[UserProfileDetailIamArgsDict]]]
    ssos: pulumi.Input[Sequence[pulumi.Input[UserProfileDetailSsoArgsDict]]]

@pulumi.input_type
class UserProfileDetailArgs:
    def __init__(
        __self__,
        *,
        iams: pulumi.Input[Sequence[pulumi.Input[UserProfileDetailIamArgs]]],
        ssos: pulumi.Input[Sequence[pulumi.Input[UserProfileDetailSsoArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iams(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[UserProfileDetailIamArgs]]]: ...
    @iams.setter
    def iams(
        self, value: pulumi.Input[Sequence[pulumi.Input[UserProfileDetailIamArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def ssos(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[UserProfileDetailSsoArgs]]]: ...
    @ssos.setter
    def ssos(
        self, value: pulumi.Input[Sequence[pulumi.Input[UserProfileDetailSsoArgs]]]
    ): ...

class UserProfileDetailIamArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserProfileDetailIamArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...

class UserProfileDetailSsoArgsDict(TypedDict):
    first_name: pulumi.Input[_builtins.str]
    last_name: pulumi.Input[_builtins.str]
    user_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserProfileDetailSsoArgs:
    def __init__(
        __self__,
        *,
        first_name: pulumi.Input[_builtins.str],
        last_name: pulumi.Input[_builtins.str],
        user_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[_builtins.str]: ...
    @first_name.setter
    def first_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[_builtins.str]: ...
    @last_name.setter
    def last_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]: ...
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): ...

class UserProfileTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserProfileTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...
