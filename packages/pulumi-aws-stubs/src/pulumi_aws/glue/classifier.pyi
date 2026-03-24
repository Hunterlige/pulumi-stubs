

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClassifierArgs', 'Classifier']
@pulumi.input_type
class ClassifierArgs:
    def __init__(__self__, *, csv_classifier: Optional[pulumi.Input[ClassifierCsvClassifierArgs]] = ..., grok_classifier: Optional[pulumi.Input[ClassifierGrokClassifierArgs]] = ..., json_classifier: Optional[pulumi.Input[ClassifierJsonClassifierArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., xml_classifier: Optional[pulumi.Input[ClassifierXmlClassifierArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvClassifier")
    def csv_classifier(self) -> Optional[pulumi.Input[ClassifierCsvClassifierArgs]]:
        
        ...
    
    @csv_classifier.setter
    def csv_classifier(self, value: Optional[pulumi.Input[ClassifierCsvClassifierArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grokClassifier")
    def grok_classifier(self) -> Optional[pulumi.Input[ClassifierGrokClassifierArgs]]:
        
        ...
    
    @grok_classifier.setter
    def grok_classifier(self, value: Optional[pulumi.Input[ClassifierGrokClassifierArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonClassifier")
    def json_classifier(self) -> Optional[pulumi.Input[ClassifierJsonClassifierArgs]]:
        
        ...
    
    @json_classifier.setter
    def json_classifier(self, value: Optional[pulumi.Input[ClassifierJsonClassifierArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xmlClassifier")
    def xml_classifier(self) -> Optional[pulumi.Input[ClassifierXmlClassifierArgs]]:
        
        ...
    
    @xml_classifier.setter
    def xml_classifier(self, value: Optional[pulumi.Input[ClassifierXmlClassifierArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ClassifierState:
    def __init__(__self__, *, csv_classifier: Optional[pulumi.Input[ClassifierCsvClassifierArgs]] = ..., grok_classifier: Optional[pulumi.Input[ClassifierGrokClassifierArgs]] = ..., json_classifier: Optional[pulumi.Input[ClassifierJsonClassifierArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., xml_classifier: Optional[pulumi.Input[ClassifierXmlClassifierArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvClassifier")
    def csv_classifier(self) -> Optional[pulumi.Input[ClassifierCsvClassifierArgs]]:
        
        ...
    
    @csv_classifier.setter
    def csv_classifier(self, value: Optional[pulumi.Input[ClassifierCsvClassifierArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grokClassifier")
    def grok_classifier(self) -> Optional[pulumi.Input[ClassifierGrokClassifierArgs]]:
        
        ...
    
    @grok_classifier.setter
    def grok_classifier(self, value: Optional[pulumi.Input[ClassifierGrokClassifierArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonClassifier")
    def json_classifier(self) -> Optional[pulumi.Input[ClassifierJsonClassifierArgs]]:
        
        ...
    
    @json_classifier.setter
    def json_classifier(self, value: Optional[pulumi.Input[ClassifierJsonClassifierArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xmlClassifier")
    def xml_classifier(self) -> Optional[pulumi.Input[ClassifierXmlClassifierArgs]]:
        
        ...
    
    @xml_classifier.setter
    def xml_classifier(self, value: Optional[pulumi.Input[ClassifierXmlClassifierArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:glue/classifier:Classifier")
class Classifier(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., csv_classifier: Optional[pulumi.Input[Union[ClassifierCsvClassifierArgs, ClassifierCsvClassifierArgsDict]]] = ..., grok_classifier: Optional[pulumi.Input[Union[ClassifierGrokClassifierArgs, ClassifierGrokClassifierArgsDict]]] = ..., json_classifier: Optional[pulumi.Input[Union[ClassifierJsonClassifierArgs, ClassifierJsonClassifierArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., xml_classifier: Optional[pulumi.Input[Union[ClassifierXmlClassifierArgs, ClassifierXmlClassifierArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ClassifierArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., csv_classifier: Optional[pulumi.Input[Union[ClassifierCsvClassifierArgs, ClassifierCsvClassifierArgsDict]]] = ..., grok_classifier: Optional[pulumi.Input[Union[ClassifierGrokClassifierArgs, ClassifierGrokClassifierArgsDict]]] = ..., json_classifier: Optional[pulumi.Input[Union[ClassifierJsonClassifierArgs, ClassifierJsonClassifierArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., xml_classifier: Optional[pulumi.Input[Union[ClassifierXmlClassifierArgs, ClassifierXmlClassifierArgsDict]]] = ...) -> Classifier:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csvClassifier")
    def csv_classifier(self) -> pulumi.Output[Optional[outputs.ClassifierCsvClassifier]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grokClassifier")
    def grok_classifier(self) -> pulumi.Output[Optional[outputs.ClassifierGrokClassifier]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonClassifier")
    def json_classifier(self) -> pulumi.Output[Optional[outputs.ClassifierJsonClassifier]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xmlClassifier")
    def xml_classifier(self) -> pulumi.Output[Optional[outputs.ClassifierXmlClassifier]]:
        
        ...
    


