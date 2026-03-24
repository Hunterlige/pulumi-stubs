

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPermissionsResult', 'AwaitableGetPermissionsResult', 'get_permissions', 'get_permissions_output']
@pulumi.output_type
class GetPermissionsResult:
    
    def __init__(__self__, catalog_id=..., catalog_resource=..., data_cells_filter=..., data_location=..., database=..., id=..., lf_tag=..., lf_tag_policy=..., permissions=..., permissions_with_grant_options=..., principal=..., region=..., table=..., table_with_columns=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogResource")
    def catalog_resource(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCellsFilter")
    def data_cells_filter(self) -> outputs.GetPermissionsDataCellsFilterResult:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> outputs.GetPermissionsDataLocationResult:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> outputs.GetPermissionsDatabaseResult:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTag")
    def lf_tag(self) -> outputs.GetPermissionsLfTagResult:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lfTagPolicy")
    def lf_tag_policy(self) -> outputs.GetPermissionsLfTagPolicyResult:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionsWithGrantOptions")
    def permissions_with_grant_options(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> outputs.GetPermissionsTableResult:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> outputs.GetPermissionsTableWithColumnsResult:
        ...
    


class AwaitableGetPermissionsResult(GetPermissionsResult):
    def __await__(self): # -> Generator[Never, Any, GetPermissionsResult]:
        ...
    


def get_permissions(catalog_id: Optional[_builtins.str] = ..., catalog_resource: Optional[_builtins.bool] = ..., data_cells_filter: Optional[Union[GetPermissionsDataCellsFilterArgs, GetPermissionsDataCellsFilterArgsDict]] = ..., data_location: Optional[Union[GetPermissionsDataLocationArgs, GetPermissionsDataLocationArgsDict]] = ..., database: Optional[Union[GetPermissionsDatabaseArgs, GetPermissionsDatabaseArgsDict]] = ..., lf_tag: Optional[Union[GetPermissionsLfTagArgs, GetPermissionsLfTagArgsDict]] = ..., lf_tag_policy: Optional[Union[GetPermissionsLfTagPolicyArgs, GetPermissionsLfTagPolicyArgsDict]] = ..., principal: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., table: Optional[Union[GetPermissionsTableArgs, GetPermissionsTableArgsDict]] = ..., table_with_columns: Optional[Union[GetPermissionsTableWithColumnsArgs, GetPermissionsTableWithColumnsArgsDict]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPermissionsResult:
    
    ...

def get_permissions_output(catalog_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., catalog_resource: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., data_cells_filter: Optional[pulumi.Input[Optional[Union[GetPermissionsDataCellsFilterArgs, GetPermissionsDataCellsFilterArgsDict]]]] = ..., data_location: Optional[pulumi.Input[Optional[Union[GetPermissionsDataLocationArgs, GetPermissionsDataLocationArgsDict]]]] = ..., database: Optional[pulumi.Input[Optional[Union[GetPermissionsDatabaseArgs, GetPermissionsDatabaseArgsDict]]]] = ..., lf_tag: Optional[pulumi.Input[Optional[Union[GetPermissionsLfTagArgs, GetPermissionsLfTagArgsDict]]]] = ..., lf_tag_policy: Optional[pulumi.Input[Optional[Union[GetPermissionsLfTagPolicyArgs, GetPermissionsLfTagPolicyArgsDict]]]] = ..., principal: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., table: Optional[pulumi.Input[Optional[Union[GetPermissionsTableArgs, GetPermissionsTableArgsDict]]]] = ..., table_with_columns: Optional[pulumi.Input[Optional[Union[GetPermissionsTableWithColumnsArgs, GetPermissionsTableWithColumnsArgsDict]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPermissionsResult]:
    
    ...

