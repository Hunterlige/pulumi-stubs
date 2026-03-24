import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AssetTypeArgs", "AssetType"]

@pulumi.input_type
class AssetTypeArgs:
    def __init__(
        __self__,
        *,
        domain_identifier: pulumi.Input[_builtins.str],
        owning_project_identifier: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        forms_inputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssetTypeFormsInputArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[AssetTypeTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="owningProjectIdentifier")
    def owning_project_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @owning_project_identifier.setter
    def owning_project_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="formsInputs")
    def forms_inputs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssetTypeFormsInputArgs]]]]: ...
    @forms_inputs.setter
    def forms_inputs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AssetTypeFormsInputArgs]]]],
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AssetTypeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AssetTypeTimeoutsArgs]]): ...

@pulumi.input_type
class _AssetTypeState:
    def __init__(
        __self__,
        *,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        forms_inputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssetTypeFormsInputArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owning_project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[AssetTypeTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_identifier.setter
    def domain_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="formsInputs")
    def forms_inputs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssetTypeFormsInputArgs]]]]: ...
    @forms_inputs.setter
    def forms_inputs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AssetTypeFormsInputArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="owningProjectIdentifier")
    def owning_project_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owning_project_identifier.setter
    def owning_project_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AssetTypeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AssetTypeTimeoutsArgs]]): ...

@pulumi.type_token("aws:datazone/assetType:AssetType")
class AssetType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        forms_inputs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AssetTypeFormsInputArgs, AssetTypeFormsInputArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owning_project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[AssetTypeTimeoutsArgs, AssetTypeTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AssetTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        forms_inputs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AssetTypeFormsInputArgs, AssetTypeFormsInputArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owning_project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[AssetTypeTimeoutsArgs, AssetTypeTimeoutsArgsDict]]
        ] = ...,
    ) -> AssetType: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="formsInputs")
    def forms_inputs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.AssetTypeFormsInput]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="owningProjectIdentifier")
    def owning_project_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AssetTypeTimeouts]]: ...
