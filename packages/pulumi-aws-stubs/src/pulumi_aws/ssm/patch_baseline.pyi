import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PatchBaselineArgs", "PatchBaseline"]

@pulumi.input_type
class PatchBaselineArgs:
    def __init__(
        __self__,
        *,
        approval_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineApprovalRuleArgs]]]
        ] = ...,
        approved_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approved_patches_compliance_level: Optional[pulumi.Input[_builtins.str]] = ...,
        approved_patches_enable_non_security: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        available_security_updates_compliance_status: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        global_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineGlobalFilterArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejected_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rejected_patches_action: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineSourceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRules")
    def approval_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PatchBaselineApprovalRuleArgs]]]
    ]: ...
    @approval_rules.setter
    def approval_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineApprovalRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvedPatches")
    def approved_patches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @approved_patches.setter
    def approved_patches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availableSecurityUpdatesComplianceStatus")
    def available_security_updates_compliance_status(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @available_security_updates_compliance_status.setter
    def available_security_updates_compliance_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="globalFilters")
    def global_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PatchBaselineGlobalFilterArgs]]]
    ]: ...
    @global_filters.setter
    def global_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineGlobalFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rejectedPatches")
    def rejected_patches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @rejected_patches.setter
    def rejected_patches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rejectedPatchesAction")
    def rejected_patches_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rejected_patches_action.setter
    def rejected_patches_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PatchBaselineSourceArgs]]]]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PatchBaselineSourceArgs]]]],
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
class _PatchBaselineState:
    def __init__(
        __self__,
        *,
        approval_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineApprovalRuleArgs]]]
        ] = ...,
        approved_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approved_patches_compliance_level: Optional[pulumi.Input[_builtins.str]] = ...,
        approved_patches_enable_non_security: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        available_security_updates_compliance_status: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        global_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineGlobalFilterArgs]]]
        ] = ...,
        json: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejected_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rejected_patches_action: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineSourceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRules")
    def approval_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PatchBaselineApprovalRuleArgs]]]
    ]: ...
    @approval_rules.setter
    def approval_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineApprovalRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvedPatches")
    def approved_patches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @approved_patches.setter
    def approved_patches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availableSecurityUpdatesComplianceStatus")
    def available_security_updates_compliance_status(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @available_security_updates_compliance_status.setter
    def available_security_updates_compliance_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="globalFilters")
    def global_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PatchBaselineGlobalFilterArgs]]]
    ]: ...
    @global_filters.setter
    def global_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PatchBaselineGlobalFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @json.setter
    def json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rejectedPatches")
    def rejected_patches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @rejected_patches.setter
    def rejected_patches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rejectedPatchesAction")
    def rejected_patches_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rejected_patches_action.setter
    def rejected_patches_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PatchBaselineSourceArgs]]]]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PatchBaselineSourceArgs]]]],
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

@pulumi.type_token("aws:ssm/patchBaseline:PatchBaseline")
class PatchBaseline(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        approval_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PatchBaselineApprovalRuleArgs,
                            PatchBaselineApprovalRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        approved_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approved_patches_compliance_level: Optional[pulumi.Input[_builtins.str]] = ...,
        approved_patches_enable_non_security: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        available_security_updates_compliance_status: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        global_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PatchBaselineGlobalFilterArgs,
                            PatchBaselineGlobalFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejected_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rejected_patches_action: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PatchBaselineSourceArgs, PatchBaselineSourceArgsDict]
                    ]
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
        args: Optional[PatchBaselineArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        approval_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PatchBaselineApprovalRuleArgs,
                            PatchBaselineApprovalRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        approved_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        approved_patches_compliance_level: Optional[pulumi.Input[_builtins.str]] = ...,
        approved_patches_enable_non_security: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        available_security_updates_compliance_status: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        global_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PatchBaselineGlobalFilterArgs,
                            PatchBaselineGlobalFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        json: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_system: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejected_patches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        rejected_patches_action: Optional[pulumi.Input[_builtins.str]] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PatchBaselineSourceArgs, PatchBaselineSourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> PatchBaseline: ...
    @_builtins.property
    @pulumi.getter(name="approvalRules")
    def approval_rules(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PatchBaselineApprovalRule]]]: ...
    @_builtins.property
    @pulumi.getter(name="approvedPatches")
    def approved_patches(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availableSecurityUpdatesComplianceStatus")
    def available_security_updates_compliance_status(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="globalFilters")
    def global_filters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PatchBaselineGlobalFilter]]]: ...
    @_builtins.property
    @pulumi.getter
    def json(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rejectedPatches")
    def rejected_patches(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="rejectedPatchesAction")
    def rejected_patches_action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PatchBaselineSource]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
