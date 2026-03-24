import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "MirroringEndpointGroupAssociationInitArgs",
    "MirroringEndpointGroupAssociation",
]

@pulumi.input_type
class MirroringEndpointGroupAssociationInitArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        mirroring_endpoint_group: pulumi.Input[_builtins.str],
        network: pulumi.Input[_builtins.str],
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        mirroring_endpoint_group_association_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroup")
    def mirroring_endpoint_group(self) -> pulumi.Input[_builtins.str]: ...
    @mirroring_endpoint_group.setter
    def mirroring_endpoint_group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroupAssociationId")
    def mirroring_endpoint_group_association_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mirroring_endpoint_group_association_id.setter
    def mirroring_endpoint_group_association_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MirroringEndpointGroupAssociationState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MirroringEndpointGroupAssociationLocationArgs]]
            ]
        ] = ...,
        locations_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[MirroringEndpointGroupAssociationLocationsDetailArgs]
                ]
            ]
        ] = ...,
        mirroring_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ...,
        mirroring_endpoint_group_association_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MirroringEndpointGroupAssociationLocationArgs]]
        ]
    ]: ...
    @locations.setter
    def locations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MirroringEndpointGroupAssociationLocationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="locationsDetails")
    @_utilities.deprecated(...)
    def locations_details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MirroringEndpointGroupAssociationLocationsDetailArgs]]
        ]
    ]: ...
    @locations_details.setter
    def locations_details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[MirroringEndpointGroupAssociationLocationsDetailArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroup")
    def mirroring_endpoint_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mirroring_endpoint_group.setter
    def mirroring_endpoint_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroupAssociationId")
    def mirroring_endpoint_group_association_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mirroring_endpoint_group_association_id.setter
    def mirroring_endpoint_group_association_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class MirroringEndpointGroupAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mirroring_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ...,
        mirroring_endpoint_group_association_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MirroringEndpointGroupAssociationInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        locations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MirroringEndpointGroupAssociationLocationArgs,
                            MirroringEndpointGroupAssociationLocationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        locations_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MirroringEndpointGroupAssociationLocationsDetailArgs,
                            MirroringEndpointGroupAssociationLocationsDetailArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        mirroring_endpoint_group: Optional[pulumi.Input[_builtins.str]] = ...,
        mirroring_endpoint_group_association_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MirroringEndpointGroupAssociation: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> pulumi.Output[Sequence[outputs.MirroringEndpointGroupAssociationLocation]]: ...
    @_builtins.property
    @pulumi.getter(name="locationsDetails")
    @_utilities.deprecated(...)
    def locations_details(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.MirroringEndpointGroupAssociationLocationsDetail]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroup")
    def mirroring_endpoint_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mirroringEndpointGroupAssociationId")
    def mirroring_endpoint_group_association_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
