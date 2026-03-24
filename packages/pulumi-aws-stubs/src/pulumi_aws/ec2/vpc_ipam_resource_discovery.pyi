import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VpcIpamResourceDiscoveryArgs", "VpcIpamResourceDiscovery"]

@pulumi.input_type
class VpcIpamResourceDiscoveryArgs:
    def __init__(
        __self__,
        *,
        operating_regions: pulumi.Input[
            Sequence[pulumi.Input[VpcIpamResourceDiscoveryOperatingRegionArgs]]
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        organizational_unit_exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[VpcIpamResourceDiscoveryOperatingRegionArgs]]
    ]: ...
    @operating_regions.setter
    def operating_regions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[VpcIpamResourceDiscoveryOperatingRegionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitExclusions")
    def organizational_unit_exclusions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs]
            ]
        ]
    ]: ...
    @organizational_unit_exclusions.setter
    def organizational_unit_exclusions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs
                    ]
                ]
            ]
        ],
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

@pulumi.input_type
class _VpcIpamResourceDiscoveryState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ipam_resource_discovery_region: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default: Optional[pulumi.Input[_builtins.bool]] = ...,
        operating_regions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VpcIpamResourceDiscoveryOperatingRegionArgs]]
            ]
        ] = ...,
        organizational_unit_exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs
                    ]
                ]
            ]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
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
    @pulumi.getter(name="ipamResourceDiscoveryRegion")
    def ipam_resource_discovery_region(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipam_resource_discovery_region.setter
    def ipam_resource_discovery_region(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VpcIpamResourceDiscoveryOperatingRegionArgs]]
        ]
    ]: ...
    @operating_regions.setter
    def operating_regions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VpcIpamResourceDiscoveryOperatingRegionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitExclusions")
    def organizational_unit_exclusions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs]
            ]
        ]
    ]: ...
    @organizational_unit_exclusions.setter
    def organizational_unit_exclusions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class VpcIpamResourceDiscovery(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        operating_regions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VpcIpamResourceDiscoveryOperatingRegionArgs,
                            VpcIpamResourceDiscoveryOperatingRegionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        organizational_unit_exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs,
                            VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VpcIpamResourceDiscoveryArgs,
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
        ipam_resource_discovery_region: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default: Optional[pulumi.Input[_builtins.bool]] = ...,
        operating_regions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VpcIpamResourceDiscoveryOperatingRegionArgs,
                            VpcIpamResourceDiscoveryOperatingRegionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        organizational_unit_exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgs,
                            VpcIpamResourceDiscoveryOrganizationalUnitExclusionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> VpcIpamResourceDiscovery: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipamResourceDiscoveryRegion")
    def ipam_resource_discovery_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(
        self,
    ) -> pulumi.Output[Sequence[outputs.VpcIpamResourceDiscoveryOperatingRegion]]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitExclusions")
    def organizational_unit_exclusions(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.VpcIpamResourceDiscoveryOrganizationalUnitExclusion]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
