import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FormTypeArgs", "FormType"]

@pulumi.input_type
class FormTypeArgs:
    def __init__(
        __self__,
        *,
        domain_identifier: pulumi.Input[_builtins.str],
        model: pulumi.Input[FormTypeModelArgs],
        owning_project_identifier: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[FormTypeTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Input[FormTypeModelArgs]: ...
    @model.setter
    def model(self, value: pulumi.Input[FormTypeModelArgs]): ...
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[FormTypeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[FormTypeTimeoutsArgs]]): ...

@pulumi.input_type
class _FormTypeState:
    def __init__(
        __self__,
        *,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_by: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        imports: Optional[
            pulumi.Input[Sequence[pulumi.Input[FormTypeImportArgs]]]
        ] = ...,
        model: Optional[pulumi.Input[FormTypeModelArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owning_project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[FormTypeTimeoutsArgs]] = ...,
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
    @pulumi.getter
    def imports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FormTypeImportArgs]]]]: ...
    @imports.setter
    def imports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FormTypeImportArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[FormTypeModelArgs]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[FormTypeModelArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originDomainId")
    def origin_domain_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_domain_id.setter
    def origin_domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originProjectId")
    def origin_project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin_project_id.setter
    def origin_project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[FormTypeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[FormTypeTimeoutsArgs]]): ...

@pulumi.type_token("aws:datazone/formType:FormType")
class FormType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        model: Optional[
            pulumi.Input[Union[FormTypeModelArgs, FormTypeModelArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owning_project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[FormTypeTimeoutsArgs, FormTypeTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FormTypeArgs,
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
        imports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[FormTypeImportArgs, FormTypeImportArgsDict]]
                ]
            ]
        ] = ...,
        model: Optional[
            pulumi.Input[Union[FormTypeModelArgs, FormTypeModelArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        origin_project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        owning_project_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[FormTypeTimeoutsArgs, FormTypeTimeoutsArgsDict]]
        ] = ...,
    ) -> FormType: ...
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
    @pulumi.getter
    def imports(self) -> pulumi.Output[Sequence[outputs.FormTypeImport]]: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Output[outputs.FormTypeModel]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originDomainId")
    def origin_domain_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originProjectId")
    def origin_project_id(self) -> pulumi.Output[_builtins.str]: ...
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
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.FormTypeTimeouts]]: ...
