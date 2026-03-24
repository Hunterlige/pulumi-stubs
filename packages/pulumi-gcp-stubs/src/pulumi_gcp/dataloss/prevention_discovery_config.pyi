import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PreventionDiscoveryConfigArgs", "PreventionDiscoveryConfig"]

@pulumi.input_type
class PreventionDiscoveryConfigArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigActionArgs]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inspect_templates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        org_config: Optional[
            pulumi.Input[PreventionDiscoveryConfigOrgConfigArgs]
        ] = ...,
        other_cloud_starting_location: Optional[
            pulumi.Input[PreventionDiscoveryConfigOtherCloudStartingLocationArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigTargetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigActionArgs]]]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplates")
    def inspect_templates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inspect_templates.setter
    def inspect_templates(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="orgConfig")
    def org_config(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigOrgConfigArgs]]: ...
    @org_config.setter
    def org_config(
        self, value: Optional[pulumi.Input[PreventionDiscoveryConfigOrgConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="otherCloudStartingLocation")
    def other_cloud_starting_location(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigOtherCloudStartingLocationArgs]
    ]: ...
    @other_cloud_starting_location.setter
    def other_cloud_starting_location(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigOtherCloudStartingLocationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigTargetArgs]]]
    ]: ...
    @targets.setter
    def targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigTargetArgs]]]
        ],
    ): ...

@pulumi.input_type
class _PreventionDiscoveryConfigState:
    def __init__(
        __self__,
        *,
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigActionArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigErrorArgs]]]
        ] = ...,
        inspect_templates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        last_run_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_config: Optional[
            pulumi.Input[PreventionDiscoveryConfigOrgConfigArgs]
        ] = ...,
        other_cloud_starting_location: Optional[
            pulumi.Input[PreventionDiscoveryConfigOtherCloudStartingLocationArgs]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigTargetArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigActionArgs]]]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigErrorArgs]]]
    ]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigErrorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplates")
    def inspect_templates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @inspect_templates.setter
    def inspect_templates(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastRunTime")
    def last_run_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_run_time.setter
    def last_run_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgConfig")
    def org_config(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigOrgConfigArgs]]: ...
    @org_config.setter
    def org_config(
        self, value: Optional[pulumi.Input[PreventionDiscoveryConfigOrgConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="otherCloudStartingLocation")
    def other_cloud_starting_location(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigOtherCloudStartingLocationArgs]
    ]: ...
    @other_cloud_starting_location.setter
    def other_cloud_starting_location(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigOtherCloudStartingLocationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigTargetArgs]]]
    ]: ...
    @targets.setter
    def targets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PreventionDiscoveryConfigTargetArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class PreventionDiscoveryConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PreventionDiscoveryConfigActionArgs,
                            PreventionDiscoveryConfigActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        inspect_templates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        org_config: Optional[
            pulumi.Input[
                Union[
                    PreventionDiscoveryConfigOrgConfigArgs,
                    PreventionDiscoveryConfigOrgConfigArgsDict,
                ]
            ]
        ] = ...,
        other_cloud_starting_location: Optional[
            pulumi.Input[
                Union[
                    PreventionDiscoveryConfigOtherCloudStartingLocationArgs,
                    PreventionDiscoveryConfigOtherCloudStartingLocationArgsDict,
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PreventionDiscoveryConfigTargetArgs,
                            PreventionDiscoveryConfigTargetArgsDict,
                        ]
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
        args: PreventionDiscoveryConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PreventionDiscoveryConfigActionArgs,
                            PreventionDiscoveryConfigActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PreventionDiscoveryConfigErrorArgs,
                            PreventionDiscoveryConfigErrorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        inspect_templates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        last_run_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        org_config: Optional[
            pulumi.Input[
                Union[
                    PreventionDiscoveryConfigOrgConfigArgs,
                    PreventionDiscoveryConfigOrgConfigArgsDict,
                ]
            ]
        ] = ...,
        other_cloud_starting_location: Optional[
            pulumi.Input[
                Union[
                    PreventionDiscoveryConfigOtherCloudStartingLocationArgs,
                    PreventionDiscoveryConfigOtherCloudStartingLocationArgsDict,
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PreventionDiscoveryConfigTargetArgs,
                            PreventionDiscoveryConfigTargetArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PreventionDiscoveryConfig: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PreventionDiscoveryConfigAction]]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> pulumi.Output[Sequence[outputs.PreventionDiscoveryConfigError]]: ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplates")
    def inspect_templates(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastRunTime")
    def last_run_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgConfig")
    def org_config(
        self,
    ) -> pulumi.Output[Optional[outputs.PreventionDiscoveryConfigOrgConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="otherCloudStartingLocation")
    def other_cloud_starting_location(
        self,
    ) -> pulumi.Output[
        Optional[outputs.PreventionDiscoveryConfigOtherCloudStartingLocation]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PreventionDiscoveryConfigTarget]]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
