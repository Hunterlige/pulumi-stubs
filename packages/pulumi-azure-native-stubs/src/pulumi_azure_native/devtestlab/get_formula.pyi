import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFormulaResult",
    "AwaitableGetFormulaResult",
    "get_formula",
    "get_formula_output",
]

@pulumi.output_type
class GetFormulaResult:
    def __init__(
        __self__,
        author=...,
        azure_api_version=...,
        creation_date=...,
        description=...,
        formula_content=...,
        id=...,
        location=...,
        name=...,
        os_type=...,
        provisioning_state=...,
        system_data=...,
        tags=...,
        type=...,
        unique_identifier=...,
        vm=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="formulaContent")
    def formula_content(
        self,
    ) -> Optional[outputs.LabVirtualMachineCreationParameterResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vm(self) -> Optional[outputs.FormulaPropertiesFromVmResponse]: ...

class AwaitableGetFormulaResult(GetFormulaResult):
    def __await__(self): ...

def get_formula(
    expand: Optional[_builtins.str] = ...,
    lab_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFormulaResult: ...
def get_formula_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFormulaResult]: ...
