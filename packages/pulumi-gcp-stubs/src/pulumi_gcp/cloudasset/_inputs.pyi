import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FolderFeedConditionArgs",
    "FolderFeedConditionArgsDict",
    "FolderFeedFeedOutputConfigArgs",
    "FolderFeedFeedOutputConfigArgsDict",
    "FolderFeedFeedOutputConfigPubsubDestinationArgs",
    ...,
    "OrganizationFeedConditionArgs",
    "OrganizationFeedConditionArgsDict",
    "OrganizationFeedFeedOutputConfigArgs",
    "OrganizationFeedFeedOutputConfigArgsDict",
    ...,
    ...,
    "ProjectFeedConditionArgs",
    "ProjectFeedConditionArgsDict",
    "ProjectFeedFeedOutputConfigArgs",
    "ProjectFeedFeedOutputConfigArgsDict",
    "ProjectFeedFeedOutputConfigPubsubDestinationArgs",
    ...,
]

class FolderFeedConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FolderFeedConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FolderFeedFeedOutputConfigArgsDict(TypedDict):
    pubsub_destination: pulumi.Input[
        FolderFeedFeedOutputConfigPubsubDestinationArgsDict
    ]
    ...

@pulumi.input_type
class FolderFeedFeedOutputConfigArgs:
    def __init__(
        __self__,
        *,
        pubsub_destination: pulumi.Input[
            FolderFeedFeedOutputConfigPubsubDestinationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(
        self,
    ) -> pulumi.Input[FolderFeedFeedOutputConfigPubsubDestinationArgs]: ...
    @pubsub_destination.setter
    def pubsub_destination(
        self, value: pulumi.Input[FolderFeedFeedOutputConfigPubsubDestinationArgs]
    ): ...

class FolderFeedFeedOutputConfigPubsubDestinationArgsDict(TypedDict):
    topic: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FolderFeedFeedOutputConfigPubsubDestinationArgs:
    def __init__(__self__, *, topic: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...

class OrganizationFeedConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OrganizationFeedConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OrganizationFeedFeedOutputConfigArgsDict(TypedDict):
    pubsub_destination: pulumi.Input[
        OrganizationFeedFeedOutputConfigPubsubDestinationArgsDict
    ]
    ...

@pulumi.input_type
class OrganizationFeedFeedOutputConfigArgs:
    def __init__(
        __self__,
        *,
        pubsub_destination: pulumi.Input[
            OrganizationFeedFeedOutputConfigPubsubDestinationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(
        self,
    ) -> pulumi.Input[OrganizationFeedFeedOutputConfigPubsubDestinationArgs]: ...
    @pubsub_destination.setter
    def pubsub_destination(
        self, value: pulumi.Input[OrganizationFeedFeedOutputConfigPubsubDestinationArgs]
    ): ...

class OrganizationFeedFeedOutputConfigPubsubDestinationArgsDict(TypedDict):
    topic: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OrganizationFeedFeedOutputConfigPubsubDestinationArgs:
    def __init__(__self__, *, topic: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...

class ProjectFeedConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProjectFeedConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectFeedFeedOutputConfigArgsDict(TypedDict):
    pubsub_destination: pulumi.Input[
        ProjectFeedFeedOutputConfigPubsubDestinationArgsDict
    ]
    ...

@pulumi.input_type
class ProjectFeedFeedOutputConfigArgs:
    def __init__(
        __self__,
        *,
        pubsub_destination: pulumi.Input[
            ProjectFeedFeedOutputConfigPubsubDestinationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pubsubDestination")
    def pubsub_destination(
        self,
    ) -> pulumi.Input[ProjectFeedFeedOutputConfigPubsubDestinationArgs]: ...
    @pubsub_destination.setter
    def pubsub_destination(
        self, value: pulumi.Input[ProjectFeedFeedOutputConfigPubsubDestinationArgs]
    ): ...

class ProjectFeedFeedOutputConfigPubsubDestinationArgsDict(TypedDict):
    topic: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ProjectFeedFeedOutputConfigPubsubDestinationArgs:
    def __init__(__self__, *, topic: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
