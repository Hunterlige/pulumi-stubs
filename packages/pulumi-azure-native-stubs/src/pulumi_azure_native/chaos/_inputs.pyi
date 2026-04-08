import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BranchArgs",
    "BranchArgsDict",
    "ContinuousActionArgs",
    "ContinuousActionArgsDict",
    "CustomerDataStoragePropertiesArgs",
    "CustomerDataStoragePropertiesArgsDict",
    "DelayActionArgs",
    "DelayActionArgsDict",
    "DiscreteActionArgs",
    "DiscreteActionArgsDict",
    "ExperimentIdentityArgs",
    "ExperimentIdentityArgsDict",
    "ExperimentPropertiesArgs",
    "ExperimentPropertiesArgsDict",
    "KeyValuePairArgs",
    "KeyValuePairArgsDict",
    "ListSelectorArgs",
    "ListSelectorArgsDict",
    "QuerySelectorArgs",
    "QuerySelectorArgsDict",
    "SimpleFilterParametersArgs",
    "SimpleFilterParametersArgsDict",
    "SimpleFilterArgs",
    "SimpleFilterArgsDict",
    "StepArgs",
    "StepArgsDict",
    "TargetReferenceArgs",
    "TargetReferenceArgsDict",
]

class BranchArgsDict(TypedDict):
    actions: pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[
                    ContinuousActionArgsDict,
                    DelayActionArgsDict,
                    DiscreteActionArgsDict,
                ]
            ]
        ]
    ]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class BranchArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[ContinuousActionArgs, DelayActionArgs, DiscreteActionArgs]
                ]
            ]
        ],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                Union[ContinuousActionArgs, DelayActionArgs, DiscreteActionArgs]
            ]
        ]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[ContinuousActionArgs, DelayActionArgs, DiscreteActionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ContinuousActionArgsDict(TypedDict):
    duration: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgsDict]]]
    selector_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ContinuousActionArgs:
    def __init__(
        __self__,
        *,
        duration: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        parameters: pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgs]]],
        selector_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.str]: ...
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgs]]]: ...
    @parameters.setter
    def parameters(
        self, value: pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectorId")
    def selector_id(self) -> pulumi.Input[_builtins.str]: ...
    @selector_id.setter
    def selector_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class CustomerDataStoragePropertiesArgsDict(TypedDict):
    blob_container_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomerDataStoragePropertiesArgs:
    def __init__(
        __self__,
        *,
        blob_container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blob_container_name.setter
    def blob_container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_id.setter
    def storage_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class DelayActionArgsDict(TypedDict):
    duration: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class DelayActionArgs:
    def __init__(
        __self__,
        *,
        duration: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.str]: ...
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class DiscreteActionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgsDict]]]
    selector_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class DiscreteActionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        parameters: pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgs]]],
        selector_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgs]]]: ...
    @parameters.setter
    def parameters(
        self, value: pulumi.Input[Sequence[pulumi.Input[KeyValuePairArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectorId")
    def selector_id(self) -> pulumi.Input[_builtins.str]: ...
    @selector_id.setter
    def selector_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ExperimentIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ExperimentIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ExperimentPropertiesArgsDict(TypedDict):
    selectors: pulumi.Input[
        Sequence[pulumi.Input[Union[ListSelectorArgsDict, QuerySelectorArgsDict]]]
    ]
    steps: pulumi.Input[Sequence[pulumi.Input[StepArgsDict]]]
    customer_data_storage: NotRequired[
        pulumi.Input[CustomerDataStoragePropertiesArgsDict]
    ]

@pulumi.input_type
class ExperimentPropertiesArgs:
    def __init__(
        __self__,
        *,
        selectors: pulumi.Input[
            Sequence[pulumi.Input[Union[ListSelectorArgs, QuerySelectorArgs]]]
        ],
        steps: pulumi.Input[Sequence[pulumi.Input[StepArgs]]],
        customer_data_storage: Optional[
            pulumi.Input[CustomerDataStoragePropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def selectors(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[Union[ListSelectorArgs, QuerySelectorArgs]]]
    ]: ...
    @selectors.setter
    def selectors(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[Union[ListSelectorArgs, QuerySelectorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> pulumi.Input[Sequence[pulumi.Input[StepArgs]]]: ...
    @steps.setter
    def steps(self, value: pulumi.Input[Sequence[pulumi.Input[StepArgs]]]): ...
    @_builtins.property
    @pulumi.getter(name="customerDataStorage")
    def customer_data_storage(
        self,
    ) -> Optional[pulumi.Input[CustomerDataStoragePropertiesArgs]]: ...
    @customer_data_storage.setter
    def customer_data_storage(
        self, value: Optional[pulumi.Input[CustomerDataStoragePropertiesArgs]]
    ): ...

class KeyValuePairArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class KeyValuePairArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ListSelectorArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    targets: pulumi.Input[Sequence[pulumi.Input[TargetReferenceArgsDict]]]
    type: pulumi.Input[_builtins.str]
    filter: NotRequired[pulumi.Input[SimpleFilterArgsDict]]

@pulumi.input_type
class ListSelectorArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        targets: pulumi.Input[Sequence[pulumi.Input[TargetReferenceArgs]]],
        type: pulumi.Input[_builtins.str],
        filter: Optional[pulumi.Input[SimpleFilterArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input[TargetReferenceArgs]]]: ...
    @targets.setter
    def targets(
        self, value: pulumi.Input[Sequence[pulumi.Input[TargetReferenceArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[SimpleFilterArgs]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[SimpleFilterArgs]]): ...

class QuerySelectorArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    query_string: pulumi.Input[_builtins.str]
    subscription_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]
    filter: NotRequired[pulumi.Input[SimpleFilterArgsDict]]

@pulumi.input_type
class QuerySelectorArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        query_string: pulumi.Input[_builtins.str],
        subscription_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        type: pulumi.Input[_builtins.str],
        filter: Optional[pulumi.Input[SimpleFilterArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Input[_builtins.str]: ...
    @query_string.setter
    def query_string(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionIds")
    def subscription_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subscription_ids.setter
    def subscription_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[SimpleFilterArgs]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[SimpleFilterArgs]]): ...

class SimpleFilterParametersArgsDict(TypedDict):
    zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SimpleFilterParametersArgs:
    def __init__(
        __self__,
        *,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SimpleFilterArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[SimpleFilterParametersArgsDict]]

@pulumi.input_type
class SimpleFilterArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        parameters: Optional[pulumi.Input[SimpleFilterParametersArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[SimpleFilterParametersArgs]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[SimpleFilterParametersArgs]]): ...

class StepArgsDict(TypedDict):
    branches: pulumi.Input[Sequence[pulumi.Input[BranchArgsDict]]]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class StepArgs:
    def __init__(
        __self__,
        *,
        branches: pulumi.Input[Sequence[pulumi.Input[BranchArgs]]],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def branches(self) -> pulumi.Input[Sequence[pulumi.Input[BranchArgs]]]: ...
    @branches.setter
    def branches(self, value: pulumi.Input[Sequence[pulumi.Input[BranchArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class TargetReferenceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, TargetReferenceType]]

@pulumi.input_type
class TargetReferenceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, TargetReferenceType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, TargetReferenceType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, TargetReferenceType]]): ...
