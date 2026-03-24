import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PlanArgs", "Plan"]

@pulumi.input_type
class PlanArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[Sequence[pulumi.Input[PlanRuleArgs]]],
        advanced_backup_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanAdvancedBackupSettingArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scan_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanScanSettingArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[PlanRuleArgs]]]: ...
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[PlanRuleArgs]]]): ...
    @_builtins.property
    @pulumi.getter(name="advancedBackupSettings")
    def advanced_backup_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlanAdvancedBackupSettingArgs]]]
    ]: ...
    @advanced_backup_settings.setter
    def advanced_backup_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanAdvancedBackupSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scanSettings")
    def scan_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanScanSettingArgs]]]]: ...
    @scan_settings.setter
    def scan_settings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanScanSettingArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _PlanState:
    def __init__(
        __self__,
        *,
        advanced_backup_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanAdvancedBackupSettingArgs]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[PlanRuleArgs]]]] = ...,
        scan_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanScanSettingArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedBackupSettings")
    def advanced_backup_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlanAdvancedBackupSettingArgs]]]
    ]: ...
    @advanced_backup_settings.setter
    def advanced_backup_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlanAdvancedBackupSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scanSettings")
    def scan_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanScanSettingArgs]]]]: ...
    @scan_settings.setter
    def scan_settings(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanScanSettingArgs]]]]
    ): ...
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
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:backup/plan:Plan")
class Plan(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_backup_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PlanAdvancedBackupSettingArgs,
                            PlanAdvancedBackupSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[PlanRuleArgs, PlanRuleArgsDict]]]]
        ] = ...,
        scan_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[PlanScanSettingArgs, PlanScanSettingArgsDict]]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PlanArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_backup_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PlanAdvancedBackupSettingArgs,
                            PlanAdvancedBackupSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[PlanRuleArgs, PlanRuleArgsDict]]]]
        ] = ...,
        scan_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[PlanScanSettingArgs, PlanScanSettingArgsDict]]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Plan: ...
    @_builtins.property
    @pulumi.getter(name="advancedBackupSettings")
    def advanced_backup_settings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PlanAdvancedBackupSetting]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence[outputs.PlanRule]]: ...
    @_builtins.property
    @pulumi.getter(name="scanSettings")
    def scan_settings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PlanScanSetting]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
