import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FeatureMembershipArgs", "FeatureMembership"]

@pulumi.input_type
class FeatureMembershipArgs:
    def __init__(
        __self__,
        *,
        feature: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        membership: pulumi.Input[_builtins.str],
        configmanagement: Optional[
            pulumi.Input[FeatureMembershipConfigmanagementArgs]
        ] = ...,
        membership_location: Optional[pulumi.Input[_builtins.str]] = ...,
        mesh: Optional[pulumi.Input[FeatureMembershipMeshArgs]] = ...,
        policycontroller: Optional[
            pulumi.Input[FeatureMembershipPolicycontrollerArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> pulumi.Input[_builtins.str]: ...
    @feature.setter
    def feature(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> pulumi.Input[_builtins.str]: ...
    @membership.setter
    def membership(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configmanagement(
        self,
    ) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementArgs]]: ...
    @configmanagement.setter
    def configmanagement(
        self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_location.setter
    def membership_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input[FeatureMembershipMeshArgs]]: ...
    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input[FeatureMembershipMeshArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def policycontroller(
        self,
    ) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerArgs]]: ...
    @policycontroller.setter
    def policycontroller(
        self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _FeatureMembershipState:
    def __init__(
        __self__,
        *,
        configmanagement: Optional[
            pulumi.Input[FeatureMembershipConfigmanagementArgs]
        ] = ...,
        feature: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_location: Optional[pulumi.Input[_builtins.str]] = ...,
        mesh: Optional[pulumi.Input[FeatureMembershipMeshArgs]] = ...,
        policycontroller: Optional[
            pulumi.Input[FeatureMembershipPolicycontrollerArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configmanagement(
        self,
    ) -> Optional[pulumi.Input[FeatureMembershipConfigmanagementArgs]]: ...
    @configmanagement.setter
    def configmanagement(
        self, value: Optional[pulumi.Input[FeatureMembershipConfigmanagementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature.setter
    def feature(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_location.setter
    def membership_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input[FeatureMembershipMeshArgs]]: ...
    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input[FeatureMembershipMeshArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def policycontroller(
        self,
    ) -> Optional[pulumi.Input[FeatureMembershipPolicycontrollerArgs]]: ...
    @policycontroller.setter
    def policycontroller(
        self, value: Optional[pulumi.Input[FeatureMembershipPolicycontrollerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:gkehub/featureMembership:FeatureMembership")
class FeatureMembership(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configmanagement: Optional[
            pulumi.Input[
                Union[
                    FeatureMembershipConfigmanagementArgs,
                    FeatureMembershipConfigmanagementArgsDict,
                ]
            ]
        ] = ...,
        feature: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_location: Optional[pulumi.Input[_builtins.str]] = ...,
        mesh: Optional[
            pulumi.Input[
                Union[FeatureMembershipMeshArgs, FeatureMembershipMeshArgsDict]
            ]
        ] = ...,
        policycontroller: Optional[
            pulumi.Input[
                Union[
                    FeatureMembershipPolicycontrollerArgs,
                    FeatureMembershipPolicycontrollerArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FeatureMembershipArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        configmanagement: Optional[
            pulumi.Input[
                Union[
                    FeatureMembershipConfigmanagementArgs,
                    FeatureMembershipConfigmanagementArgsDict,
                ]
            ]
        ] = ...,
        feature: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_location: Optional[pulumi.Input[_builtins.str]] = ...,
        mesh: Optional[
            pulumi.Input[
                Union[FeatureMembershipMeshArgs, FeatureMembershipMeshArgsDict]
            ]
        ] = ...,
        policycontroller: Optional[
            pulumi.Input[
                Union[
                    FeatureMembershipPolicycontrollerArgs,
                    FeatureMembershipPolicycontrollerArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FeatureMembership: ...
    @_builtins.property
    @pulumi.getter
    def configmanagement(
        self,
    ) -> pulumi.Output[Optional[outputs.FeatureMembershipConfigmanagement]]: ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="membershipLocation")
    def membership_location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> pulumi.Output[Optional[outputs.FeatureMembershipMesh]]: ...
    @_builtins.property
    @pulumi.getter
    def policycontroller(
        self,
    ) -> pulumi.Output[Optional[outputs.FeatureMembershipPolicycontroller]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
