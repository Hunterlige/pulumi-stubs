import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkteamArgs", "Workteam"]

@pulumi.input_type
class WorkteamArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        member_definitions: pulumi.Input[
            Sequence[pulumi.Input[WorkteamMemberDefinitionArgs]]
        ],
        workteam_name: pulumi.Input[_builtins.str],
        notification_configuration: Optional[
            pulumi.Input[WorkteamNotificationConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        worker_access_configuration: Optional[
            pulumi.Input[WorkteamWorkerAccessConfigurationArgs]
        ] = ...,
        workforce_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="memberDefinitions")
    def member_definitions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[WorkteamMemberDefinitionArgs]]]: ...
    @member_definitions.setter
    def member_definitions(
        self, value: pulumi.Input[Sequence[pulumi.Input[WorkteamMemberDefinitionArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workteamName")
    def workteam_name(self) -> pulumi.Input[_builtins.str]: ...
    @workteam_name.setter
    def workteam_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkteamNotificationConfigurationArgs]]: ...
    @notification_configuration.setter
    def notification_configuration(
        self, value: Optional[pulumi.Input[WorkteamNotificationConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workerAccessConfiguration")
    def worker_access_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkteamWorkerAccessConfigurationArgs]]: ...
    @worker_access_configuration.setter
    def worker_access_configuration(
        self, value: Optional[pulumi.Input[WorkteamWorkerAccessConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workforce_name.setter
    def workforce_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _WorkteamState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        member_definitions: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkteamMemberDefinitionArgs]]]
        ] = ...,
        notification_configuration: Optional[
            pulumi.Input[WorkteamNotificationConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        subdomain: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        worker_access_configuration: Optional[
            pulumi.Input[WorkteamWorkerAccessConfigurationArgs]
        ] = ...,
        workforce_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workteam_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberDefinitions")
    def member_definitions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkteamMemberDefinitionArgs]]]
    ]: ...
    @member_definitions.setter
    def member_definitions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkteamMemberDefinitionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkteamNotificationConfigurationArgs]]: ...
    @notification_configuration.setter
    def notification_configuration(
        self, value: Optional[pulumi.Input[WorkteamNotificationConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workerAccessConfiguration")
    def worker_access_configuration(
        self,
    ) -> Optional[pulumi.Input[WorkteamWorkerAccessConfigurationArgs]]: ...
    @worker_access_configuration.setter
    def worker_access_configuration(
        self, value: Optional[pulumi.Input[WorkteamWorkerAccessConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workforce_name.setter
    def workforce_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workteamName")
    def workteam_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workteam_name.setter
    def workteam_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:sagemaker/workteam:Workteam")
class Workteam(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        member_definitions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkteamMemberDefinitionArgs,
                            WorkteamMemberDefinitionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        notification_configuration: Optional[
            pulumi.Input[
                Union[
                    WorkteamNotificationConfigurationArgs,
                    WorkteamNotificationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        worker_access_configuration: Optional[
            pulumi.Input[
                Union[
                    WorkteamWorkerAccessConfigurationArgs,
                    WorkteamWorkerAccessConfigurationArgsDict,
                ]
            ]
        ] = ...,
        workforce_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workteam_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkteamArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        member_definitions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkteamMemberDefinitionArgs,
                            WorkteamMemberDefinitionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        notification_configuration: Optional[
            pulumi.Input[
                Union[
                    WorkteamNotificationConfigurationArgs,
                    WorkteamNotificationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        subdomain: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        worker_access_configuration: Optional[
            pulumi.Input[
                Union[
                    WorkteamWorkerAccessConfigurationArgs,
                    WorkteamWorkerAccessConfigurationArgsDict,
                ]
            ]
        ] = ...,
        workforce_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workteam_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Workteam: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memberDefinitions")
    def member_definitions(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkteamMemberDefinition]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkteamNotificationConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subdomain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workerAccessConfiguration")
    def worker_access_configuration(
        self,
    ) -> pulumi.Output[outputs.WorkteamWorkerAccessConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="workforceName")
    def workforce_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workteamName")
    def workteam_name(self) -> pulumi.Output[_builtins.str]: ...
