

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
__all__ = ['NoteArgs', 'Note']
@pulumi.input_type
class NoteArgs:
    def __init__(__self__, *, attestation_authority: pulumi.Input[NoteAttestationAuthorityArgs], expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., related_note_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., related_urls: Optional[pulumi.Input[Sequence[pulumi.Input[NoteRelatedUrlArgs]]]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> pulumi.Input[NoteAttestationAuthorityArgs]:
        
        ...
    
    @attestation_authority.setter
    def attestation_authority(self, value: pulumi.Input[NoteAttestationAuthorityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @long_description.setter
    def long_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedNoteNames")
    def related_note_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @related_note_names.setter
    def related_note_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedUrls")
    def related_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NoteRelatedUrlArgs]]]]:
        
        ...
    
    @related_urls.setter
    def related_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NoteRelatedUrlArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_description.setter
    def short_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _NoteState:
    def __init__(__self__, *, attestation_authority: Optional[pulumi.Input[NoteAttestationAuthorityArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., related_note_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., related_urls: Optional[pulumi.Input[Sequence[pulumi.Input[NoteRelatedUrlArgs]]]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> Optional[pulumi.Input[NoteAttestationAuthorityArgs]]:
        
        ...
    
    @attestation_authority.setter
    def attestation_authority(self, value: Optional[pulumi.Input[NoteAttestationAuthorityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @long_description.setter
    def long_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedNoteNames")
    def related_note_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @related_note_names.setter
    def related_note_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedUrls")
    def related_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NoteRelatedUrlArgs]]]]:
        
        ...
    
    @related_urls.setter
    def related_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NoteRelatedUrlArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_description.setter
    def short_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:containeranalysis/note:Note")
class Note(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attestation_authority: Optional[pulumi.Input[Union[NoteAttestationAuthorityArgs, NoteAttestationAuthorityArgsDict]]] = ..., expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., related_note_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., related_urls: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NoteRelatedUrlArgs, NoteRelatedUrlArgsDict]]]]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NoteArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attestation_authority: Optional[pulumi.Input[Union[NoteAttestationAuthorityArgs, NoteAttestationAuthorityArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., long_description: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., related_note_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., related_urls: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NoteRelatedUrlArgs, NoteRelatedUrlArgsDict]]]]] = ..., short_description: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Note:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attestationAuthority")
    def attestation_authority(self) -> pulumi.Output[outputs.NoteAttestationAuthority]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedNoteNames")
    def related_note_names(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedUrls")
    def related_urls(self) -> pulumi.Output[Optional[Sequence[outputs.NoteRelatedUrl]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


