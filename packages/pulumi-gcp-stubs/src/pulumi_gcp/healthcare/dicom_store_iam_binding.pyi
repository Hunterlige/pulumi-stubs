

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DicomStoreIamBindingArgs', 'DicomStoreIamBinding']
@pulumi.input_type
class DicomStoreIamBindingArgs:
    def __init__(__self__, *, dicom_store_id: pulumi.Input[_builtins.str], members: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], role: pulumi.Input[_builtins.str], condition: Optional[pulumi.Input[DicomStoreIamBindingConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dicom_store_id.setter
    def dicom_store_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[DicomStoreIamBindingConditionArgs]]:
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[DicomStoreIamBindingConditionArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DicomStoreIamBindingState:
    def __init__(__self__, *, condition: Optional[pulumi.Input[DicomStoreIamBindingConditionArgs]] = ..., dicom_store_id: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[DicomStoreIamBindingConditionArgs]]:
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[DicomStoreIamBindingConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dicom_store_id.setter
    def dicom_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DicomStoreIamBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., condition: Optional[pulumi.Input[Union[DicomStoreIamBindingConditionArgs, DicomStoreIamBindingConditionArgsDict]]] = ..., dicom_store_id: Optional[pulumi.Input[_builtins.str]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DicomStoreIamBindingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., condition: Optional[pulumi.Input[Union[DicomStoreIamBindingConditionArgs, DicomStoreIamBindingConditionArgsDict]]] = ..., dicom_store_id: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> DicomStoreIamBinding:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.DicomStoreIamBindingCondition]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dicomStoreId")
    def dicom_store_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


